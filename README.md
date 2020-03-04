# Simple-Rover-Dashboard
A simple Flask/Socket.io Python app with a vanilla web front-end.

![alt text](https://github.com/ddelago/Simple-Rover-Dashboard/blob/master/media/dashboard.PNG)

## Installing
1. `git clone https://github.com/ddelago/Simple-Rover-Dashboard.git`
2. `pip install -r requirements.txt`

## Running
### Starting the camera server
1. `cd camera_server`
2. `python webstreaming.py`

### Starting the main server
1. Open up a new terminal
2. `python server.py`

## Interacting with the Dashboard
You first need to connect to the rover server in order to send commands.
1. Enter the rover IP addess and port on the main dashboard and press submit.
2. Check the server terminal to ensure there were no errors.
3. Test the connection by pressing the `Activate LED` command button a few times.

## Controller inputs
Controller input using an Xbox 360 USB controller

Axis
- 0: Left stick horizontal
- 1: Left stick vertical
- 2: Left trigger (positive) and Right trigger (negative)
- 3: Right stick vertical
- 4: Right stick horizontal

Buttons:
- 0: A
- 1: B
- 2: X
- 3: Y
- 4: Left bumper
- 5: Right bumper
- 6: Back
- 7: Start
- 8: Left stick press
- 9: Right stick press

Hat (d-pad):
- Left press: (-1, 0)
- Right press: (1, 0)
- Down press: (0, -1)
- Up press: (0, 1)
