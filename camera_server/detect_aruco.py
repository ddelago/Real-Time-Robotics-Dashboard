# The following code is used to watch a video stream, detect Aruco markers, and use
# a set of markers to determine the posture of the camera in relation to the plane
# of markers.

import numpy as np
import cv2
import cv2.aruco as aruco
import sys
import os
import pickle

class ArucoDetection:

    output_frame = None

    def __init__(self):
        # Check for camera calibration data
        if not os.path.exists('./calibration/CameraCalibration.pckl'):
            print("You need to calibrate the camera you'll be using. See calibration project directory for details.")
            exit()
        else:
            f = open('./calibration/CameraCalibration.pckl', 'rb')
            (cameraMatrix, distCoeffs, _, _) = pickle.load(f)
            f.close()
            if cameraMatrix is None or distCoeffs is None:
                print("Calibration issue. Remove ./calibration/CameraCalibration.pckl and recalibrate your camera with calibration_ChAruco.py.")
                exit()
            
            self.cameraMatrix = cameraMatrix
            self.distCoeffs = distCoeffs

        # Constant parameters used in Aruco methods
        self.ARUCO_PARAMETERS = aruco.DetectorParameters_create()
        self.ARUCO_DICT = aruco.Dictionary_get(aruco.DICT_5X5_50)

        # Create grid board object we're using in our stream
        self.board = aruco.GridBoard_create(
                markersX=1,
                markersY=1,
                markerLength=0.09,
                markerSeparation=0.01,
                dictionary=self.ARUCO_DICT)

        # Create vectors we'll be using for rotations and translations for postures
        self.rotation_vectors, self.translation_vectors = None, None
        self.axis = np.float32([[-.5,-.5,0], [-.5,.5,0], [.5,.5,0], [.5,-.5,0],
                        [-.5,-.5,1],[-.5,.5,1],[.5,.5,1],[.5,-.5,1] ])

    def drawCube(self, img, corners, imgpts):
        imgpts = np.int32(imgpts).reshape(-1,2)

        # draw ground floor in green
        # img = cv2.drawContours(img, [imgpts[:4]],-1,(0,255,0),-3)

        # draw pillars in blue color
        for i,j in zip(range(4),range(4,8)):
            img = cv2.line(img, tuple(imgpts[i]), tuple(imgpts[j]),(255),3)

        # draw top layer in red color
        img = cv2.drawContours(img, [imgpts[4:]],-1,(0,0,255),3)

        return img

    def detect_aruco(self, ProjectImage):
        # grayscale image
        gray = cv2.cvtColor(ProjectImage, cv2.COLOR_BGR2GRAY)
        
        # Detect Aruco markers
        corners, ids, rejectedImgPoints = aruco.detectMarkers(gray, self.ARUCO_DICT, parameters=self.ARUCO_PARAMETERS)

        # Refine detected markers
        # Eliminates markers not part of our board, adds missing markers to the board
        corners, ids, rejectedImgPoints, recoveredIds = aruco.refineDetectedMarkers(
                image = gray,
                board = self.board,
                detectedCorners = corners,
                detectedIds = ids,
                rejectedCorners = rejectedImgPoints,
                cameraMatrix = self.cameraMatrix,
                distCoeffs = self.distCoeffs)   

        # Outline all of the markers detected in our image
        # Uncomment below to show ids as well
        # ProjectImage = aruco.drawDetectedMarkers(ProjectImage, corners, ids, borderColor=(0, 0, 255))
        ProjectImage = aruco.drawDetectedMarkers(ProjectImage, corners, borderColor=(0, 0, 255))

        # Draw the Charuco board we've detected to show our calibrator the board was properly detected
        # Require at least 1 marker before drawing axis
        if ids is not None and len(ids) > 0:
            # Estimate the posture per each Aruco marker
            self.rotation_vectors, self.translation_vectors, _objPoints = aruco.estimatePoseSingleMarkers(corners, 1, self.cameraMatrix, self.distCoeffs)
            
            for rvec, tvec in zip(self.rotation_vectors, self.translation_vectors):
                if len(sys.argv) == 2 and sys.argv[1] == 'cube':
                    try:
                        imgpts, jac = cv2.projectPoints(self.axis, rvec, tvec, self.cameraMatrix, self.distCoeffs)
                        ProjectImage = self.drawCube(ProjectImage, corners, imgpts)
                    except:
                        continue
                else:    
                    ProjectImage = aruco.drawAxis(ProjectImage, self.cameraMatrix, self.distCoeffs, rvec, tvec, 1)

        return ProjectImage
