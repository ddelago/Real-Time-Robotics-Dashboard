import os
import io
from urllib3 import PoolManager
from PIL import Image

user_agent = {'user-agent': 'My program name and version number contact myname@myuni.ac.uk'}
http = PoolManager(headers=user_agent)

for zoom in os.listdir('tile-urls'):
    # For each zoom level, get the associated map tiles
    with open(f'tile-urls/{zoom}', 'r') as reader:
        for url in reader:
            stripped_url = url.strip().split('/')
            try:
                # Extract the tile coords
                z = stripped_url[-3]
                x = stripped_url[-2]
                y = stripped_url[-1]

                # Check if zoom dir exists
                if not os.path.exists(f'../mapServer/tiles/{z}/{x}'):
                    os.makedirs(f'../mapServer/tiles/{z}/{x}')

                # Check if tile exists
                if not os.path.exists(f'../mapServer/tiles/{z}/{x}/{y}'):
                    # Send a request for a specific map tile
                    response = http.request('GET', url.strip())
                    img = Image.open(io.BytesIO(response.data))

                    # Save the tile
                    img.save(f'../mapServer/tiles/{z}/{x}/{y}')
                    print(f'... got {z}/{x}/{y} tile')
                else:
                    print(f'... found {z}/{x}/{y} tile')
            except:
                print(f'Skipped {url}')
                continue
