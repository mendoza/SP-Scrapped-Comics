import requests
import json
import os
from tqdm import tqdm
FOLDER_NAME = "IMAGES"
COMIC_NAME = "COMIC_"

print('Started downloading all images...')
for i in range(6):
    print(f'Downloading  comic\'s #%s images...' % str(i))
    with open(f"Comic-%s.json" % str(i), 'r') as images:
        images = json.load(images)
        for img in tqdm(images['images']):
            fileName = f'%s/%s%s/%.2d.jpg' % (FOLDER_NAME,
                                              COMIC_NAME, str(i), images['images'].index(img))
            os.makedirs(os.path.dirname(fileName), exist_ok=True)
            with open(fileName, 'wb') as f:
                f.write(requests.get(img).content)
    print(f'Finished  downloading comic\'s #%s images!' % str(i))
print('Finished  downloading all images!')
