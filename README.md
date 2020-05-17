# Simple-Rover-Dashboard
A simple Flask/Socket.io Python app with a vanilla web front-end.

![alt text](https://github.com/ddelago/Simple-Rover-Dashboard/blob/master/media/dashboard.PNG)

## Installing
1. `git clone https://github.com/ddelago/Simple-Rover-Dashboard.git`
2. `pip install -r requirements.txt`

## Running
### Starting the camera server
1. `cd camera_server`
2. Make sure you have a `CameraCalibration.pckl` file. 
    - [See here on how to properly create one.](https://github.com/ddelago/Aruco-Marker-Calibration-and-Pose-Estimation) for more information on how to properly calibrate your camera.)
3. `python webstreaming.py`
4. The camera server can now be viewed at [http://localhost:6006](http://localhost:6006).
    - Ensure that a webcam is connected and that the correct camera is being sourced (line 20).

### Starting the main server
1. Open up a new terminal
2. `python server.py`
3. Navigate to [http://localhost:1337](http://localhost:1337) to view the dashboard.

### Displaying the map
- The map page is static and will be rendered using the saved map tiles.
- The tile data is located in `map_generation/map_server/tiles`.
- The map icons are located in `map_generation/map_server/images`.

#### Generating Map Tiles
1. To generate a new set of map tiles, first get a set of long/lat points that represents a bounding box. (2 pairs of points)
    - [Using this website will be helpful.](http://tools.geofabrik.de/calc/#type=geofabrik_standard&bbox=-97.151475,32.709637,-97.062211,32.749782&tab=1&proj=EPSG:4326&places=2)
2. Have Visual Studio installed. 
3. Open the `map_generation/GenerateTiles/GenerateTilesProject.sln` file in Visual Studio.
4. Update the coordinates you would like in the `Main` function of `GenerateTiles.cs` as well as the zoom levels you want.
5. Run the project in Visual Studio. This will create a folder called `tile-urls` with the urls that will be used to fetch map tiles from the osm server.
6. Run the `request_tiles.py` program from the `GenerateTiles` directory.
7. This will fetch the map tiles using the urls and create the appropriate map tile folder structure in `map_generation/mapServer/tiles` 
    - This process may take a very long time depending on your coordinates and the zoom levels that you requested.
8. Once all tiles have been downloaded. You can open the `index.html` file in a browser and view your offline map!
    - You can also embed this static website into other websites such as a dashboard.
9. To customize the usage of your map, such as feeding it coordinates to track, you can use the leaflet library included in `mapServer` to do so.
    - [More about leaflet here.](https://leafletjs.com/)

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
