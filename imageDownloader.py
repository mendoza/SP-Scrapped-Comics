import requests
import json
import os
from tqdm import tqdm
FOLDER_NAME = "IMAGES"
COMIC_PREFIX = "COMIC_"

print('Started downloading all images...')
for i in range(6):
    print(f'Downloading  comic\'s #{str(i+1)} images...')
    with open(f"Comic-{str(i+1)}.json", 'r') as images:
        images = json.load(images)
        for img in tqdm(images['images']):
            num = round(images['images'].index(img), 2)
            fileName = f'{FOLDER_NAME}/{COMIC_PREFIX}{str(i)}/{num}.jpg'
            os.makedirs(os.path.dirname(fileName), exist_ok=True)
            with open(fileName, 'wb') as f:
                f.write(requests.get(img).content)
    print(f'Finished  downloading comic\'s #{str(i)} images!')
print('Finished  downloading all images!')
