from urllib3 import PoolManager
from PIL import Image
import os
import io

user_agent = {'user-agent': 'My program name and version number contact myname@myuni.ac.uk'}
http = PoolManager(headers=user_agent)

for zoom in os.listdir('tile-urls'):
    with open(f'tile-urls/{zoom}', 'r') as reader:
        for url in reader:
            stripped_url = url.strip().split('/')
            try:
                response = http.request('GET', url.strip())
                
                z = stripped_url[-3]
                x = stripped_url[-2]
                y = stripped_url[-1]
                img = Image.open(io.BytesIO(response.data))
                
                if not os.path.exists(f"../tiles/{z}/{x}"):
                    os.makedirs(f"../tiles/{z}/{x}")
                img.save(f"../tiles/{z}/{x}/{y}")
            except:
                print(f'Skipped {url}')
                continue


