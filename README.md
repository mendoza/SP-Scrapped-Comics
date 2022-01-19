# SP-Scrapped-Comics

Scott Pilgrim's comics scrapped from [viewcomiconline](https://viewcomiconline.com/) and turned into pdfs (Could work with any comic, with some changes!), worked at the moment of the last download (January 10 06:38 PM CST)

# How to run

```bash
# Sync dependencies
pipenv sync

# Access shell with installed dependencies
pipenv shell

# Get JSON files with images urls.
scrapy runspider spider.py

# Download all images from all the JSON files.
python imageDownloader.py

# Generate a PDF for each comic.
python pdfGenerator.py
```

PDFs should be in the pdf folder
