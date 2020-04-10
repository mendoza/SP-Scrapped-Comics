# SP-Scrapped-Comics

Scott Pilgrim's comics scrapped from [viewcomiconline](https://viewcomiconline.com/) and turn to pdfs, worked at the moment of making it (April 10 2:40 AM)

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
scrapy spider spider.py
python imageDownloader.py
python pdfGenerator.py
# Pdfs will be in the pdf folder...
```
