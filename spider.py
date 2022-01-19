import scrapy
import json


class BlogSpider(scrapy.Spider):
    name = 'Scott Pilgrim'
    start_urls = [
        "https://viewcomiconline.com/scott-pilgrim-vol-1-of-6-scott-pilgrims-precious-little-life-2012-2/",
        "https://viewcomiconline.com/scott-pilgrim-vol-2-of-6-scott-pilgrim-vs-the-world-2012/",
        "https://viewcomiconline.com/scott-pilgrim-vol-3-of-6-scott-pilgrim-and-the-infinite-sadness-2013/",
        "https://viewcomiconline.com/scott-pilgrim-vol-4-of-6-scott-pilgrim-gets-it-together-2013/",
        "https://viewcomiconline.com/scott-pilgrim-vol-5-of-6-scott-pilgrim-vs-the-universe-2014/",
        "https://viewcomiconline.com/scott-pilgrim-vol-6-of-6-in-his-finest-hour-2015/"
    ]

    def parse(self, response):
        images_Dict = {"images": []}
        images = response.css('#chapter-c>img')
        print(f'response url: {response.url}')
        with open(f"Comic-{self.start_urls.index(response.url)}.json", 'w') as f:
            for img in images:
                images_Dict['images'].append(img.attrib["src"])
            f.write(json.dumps(images_Dict))
