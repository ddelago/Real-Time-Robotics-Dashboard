# import the necessary packages
import time
import threading
import cv2
from imutils.video import VideoStream
from flask import Flask, render_template, Response
from detect_aruco import ArucoDetection

# initialize the output frame and a lock used to ensure thread-safe
# exchanges of the output frames (useful for multiple browsers/tabs
# are viewing the stream)
OUTPUT_FRAME = None
LOCK = threading.Lock()
ARUCO_DETECTION = ArucoDetection()

# initialize a flask object
APP = Flask(__name__)

# initialize the video stream and allow the camera sensor to warmup
VS = VideoStream(src=0).start()
time.sleep(2.0)

@APP.route("/")
def index():
    """
    return the rendered template
    """
    return render_template("index.html")

def stream_camera():
    """
    loop over frames from the video stream
    """
    global VS, OUTPUT_FRAME, LOCK

    while True:
        frame = VS.read()

        ARUCO_DETECTION.detect_aruco(frame)

        # acquire the lock, set the output frame, and release the lock
        with LOCK:
            OUTPUT_FRAME = frame.copy()

def generate():
    """
    Get the output frame and encode it.
    """
    # grab global references to the output frame and lock variables
    global OUTPUT_FRAME, LOCK

    # Continuously get the output frame
    while True:
        # wait until the lock is acquired
        with LOCK:
            # check if the output frame is available
            if OUTPUT_FRAME is None:
                continue

            # encode the frame in JPEG format
            (flag, encoded_image) = cv2.imencode(".jpg", OUTPUT_FRAME)

            # ensure the frame was successfully encoded
            if not flag:
                continue

        # yield the output frame in the byte format
        yield b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + bytearray(encoded_image) + b'\r\n'

@APP.route("/video_feed")
def video_feed():
    """
    Return the encoded video frame.
    """
    return Response(generate(), mimetype="multipart/x-mixed-replace; boundary=frame")

if __name__ == '__main__':
    # start a thread that will stream the camera
    STREAM = threading.Thread(target=stream_camera, daemon=True)
    STREAM.start()

    # start the flask app
    APP.run(host="0.0.0.0", port="6006", debug=True,
            threaded=True, use_reloader=False)

# release the video stream pointer
VS.stop()
