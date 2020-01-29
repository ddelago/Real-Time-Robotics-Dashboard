# Socket-and-Flask-GUI
A simple multithreaded Flask app with Socket connections.

## Running
1. `npm install`
2. `python server.py`
3. `python dummySocketClient.py`

## Controller inputs
Controller input using an Xbox 360 USB controller

Axis
0: Left stick horizontal
1: Left stick vertical
2: Left trigger (positive) and Right trigger (negative)
3: Right stick vertical
4: Right stick horizontal

Buttons:
0: A
1: B
2: X
3: Y
4: Left bumper
5: Right bumper
6: Back
7: Start
8: Left stick press
9: Right stick press

Hat (d-pad):
Left press: (-1, 0)
Right press: (1, 0)
Down press: (0, -1)
Up press: (0, 1)