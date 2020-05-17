# The following code is used to watch a video stream, detect Aruco markers, and use
# a set of markers to determine the posture of the camera in relation to the plane
# of markers.

import sys
import os
import pickle
import cv2
import cv2.aruco as aruco
import numpy as np

class ArucoDetection:
    """
    Used to init Aruco module and detect markers.
    """
    output_frame = None

    def __init__(self):
        # Check for camera calibration data
        if not os.path.exists('./calibration/CameraCalibration.pckl'):
            print("You need to calibrate the camera you'll be using. See calibration project directory for details.")
            exit()
        else:
            calib = open('./calibration/CameraCalibration.pckl', 'rb')
            (camera_matrix, dist_coeffs, _, _) = pickle.load(calib)
            calib.close()
            if camera_matrix is None or dist_coeffs is None:
                print("Calibration issue. Remove ./calibration/CameraCalibration.pckl and recalibrate your camera with calibration_ChAruco.py.")
                exit()

            self.camera_matrix = camera_matrix
            self.dist_coeffs = dist_coeffs

        # Constant parameters used in Aruco methods
        self.aruco_params = aruco.DetectorParameters_create()
        self.aruco_dict = aruco.Dictionary_get(aruco.DICT_5X5_50)

        # Create grid board object we're using in our stream
        self.board = aruco.GridBoard_create(
            markersX=1,
            markersY=1,
            markerLength=0.09,
            markerSeparation=0.01,
            dictionary=self.aruco_dict)

        # Create vectors we'll be using for rotations and translations for postures
        self.rotation_vectors, self.translation_vectors = None, None
        self.axis = np.float32([
            [-.5, -.5, 0], [-.5, .5, 0], [.5, .5, 0], [.5, -.5, 0],
            [-.5, -.5, 1], [-.5, .5, 1], [.5, .5, 1], [.5, -.5, 1]
        ])

    def draw_cube(self, img, corners, imgpts):
        """
        Draw a graphic over Aruco markers.
        """
        imgpts = np.int32(imgpts).reshape(-1, 2)

        # draw ground floor in green
        # img = cv2.drawContours(img, [imgpts[:4]],-1,(0,255,0),-3)

        # draw pillars in blue color
        for i, j in zip(range(4), range(4, 8)):
            img = cv2.line(img, tuple(imgpts[i]), tuple(imgpts[j]), (255), 3)

        # draw top layer in red color
        img = cv2.drawContours(img, [imgpts[4:]], -1, (0, 0, 255), 3)

        return img

    def detect_aruco(self, ProjectImage):
        """
        Search for Aruco markers in an image.
        """
        # grayscale image
        gray = cv2.cvtColor(ProjectImage, cv2.COLOR_BGR2GRAY)

        # Detect Aruco markers
        corners, ids, rejected_img_points = aruco.detectMarkers(gray, self.aruco_dict, parameters=self.aruco_params)

        # Refine detected markers
        # Eliminates markers not part of our board, adds missing markers to the board
        corners, ids, rejected_img_points, recovered_ids = aruco.refineDetectedMarkers(
            image=gray,
            board=self.board,
            detectedCorners=corners,
            detectedIds=ids,
            rejectedCorners=rejected_img_points,
            camera_matrix=self.camera_matrix,
            dist_coeffs=self.dist_coeffs)   

        # Outline all of the markers detected in our image
        # Uncomment below to show ids as well
        # ProjectImage = aruco.drawDetectedMarkers(ProjectImage, corners, ids, borderColor=(0, 0, 255))
        ProjectImage = aruco.drawDetectedMarkers(ProjectImage, corners, borderColor=(0, 0, 255))

        # Draw the Charuco board we've detected to show our calibrator the board was properly detected
        # Require at least 1 marker before drawing axis
        if ids is not None and len(ids) > 0:
            # Estimate the posture per each Aruco marker
            self.rotation_vectors, self.translation_vectors, _obj_points = aruco.estimatePoseSingleMarkers(corners, 1, self.camera_matrix, self.dist_coeffs)

            # For each marker detected, outline it.
            for rvec, tvec in zip(self.rotation_vectors, self.translation_vectors):
                if len(sys.argv) == 2 and sys.argv[1] == 'cube':
                    try:
                        imgpts, jac = cv2.projectPoints(self.axis, rvec, tvec, self.camera_matrix, self.dist_coeffs)
                        ProjectImage = self.draw_cube(ProjectImage, corners, imgpts)
                    except:
                        continue
                else:
                    ProjectImage = aruco.drawAxis(ProjectImage, self.camera_matrix, self.dist_coeffs, rvec, tvec, 1)

        return ProjectImage
