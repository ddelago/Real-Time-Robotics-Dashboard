# import the necessary packages
from imutils.video import VideoStream
from flask import Flask, render_template, Response
from detect_aruco import ArucoDetection
import threading
import argparse
import datetime
import time
import cv2

# initialize the output frame and a lock used to ensure thread-safe
# exchanges of the output frames (useful for multiple browsers/tabs
# are viewing the stream)
outputFrame = None
lock = threading.Lock()
aruco_detection = ArucoDetection()

# initialize a flask object
app = Flask(__name__)

# initialize the video stream and allow the camera sensor to warmup
vs = VideoStream(src=1).start()
time.sleep(2.0)

@app.route("/")
def index():
	# return the rendered template
	return render_template("index.html")

def stream_camera():
	global vs, outputFrame, lock

	# loop over frames from the video stream
	while True:
		frame = vs.read()

		aruco_detection.detect_aruco(frame)

		# acquire the lock, set the output frame, and release the lock
		with lock:
			outputFrame = frame.copy()
		
def generate():
	# grab global references to the output frame and lock variables
	global outputFrame, lock

	# loop over frames from the output stream
	while True:
		# wait until the lock is acquired
		with lock:
			# check if the output frame is available, otherwise skip
			# the iteration of the loop
			if outputFrame is None:
				continue

			# encode the frame in JPEG format
			(flag, encodedImage) = cv2.imencode(".jpg", outputFrame)

			# ensure the frame was successfully encoded
			if not flag:
				continue

		# yield the output frame in the byte format
		yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + 
			bytearray(encodedImage) + b'\r\n')

@app.route("/video_feed")
def video_feed():
	return Response(generate(),
		mimetype = "multipart/x-mixed-replace; boundary=frame")

if __name__ == '__main__':

	# start a thread that will stream the camera
	t = threading.Thread(target=stream_camera, daemon=True)
	t.start()

	# start the flask app
	app.run(host="0.0.0.0", port="6006", debug=True,
		threaded=True, use_reloader=False)

# release the video stream pointer
vs.stop()