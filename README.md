# SP-Scrapped-Comics

Scott Pilgrim's comics scrapped from [viewcomiconline](https://viewcomiconline.com/) and turned into pdfs, worked at the moment of the last download (January 10 06:38 PM CST)

# Dependecies

- pipenv
- scrapy
- requests
- fpdf
- tqdm

# How to run

```bash
pipenv sync
pipenv shell
scrapy runspider spider.py
python imageDownloader.py
python pdfGenerator.py
# Pdfs will be in the pdf folder...
```
