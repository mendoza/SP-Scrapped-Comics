import os
from tqdm import tqdm
from fpdf import FPDF
IMG_FOLDER_NAME = "IMAGES"
PDF_FOLDER_NAME = "PDFS"
COMIC_NAME = "COMIC_"
A4_WIDTH = 210
A4_HEIGHT = 297

print('Started generating all pdfs...')
for i in range(6):
    print(f'Generating comic\'s #%s pdf... %d' % i+1)
    pdf = FPDF()
    lista = os.listdir(f'%s/%s%d' % (IMG_FOLDER_NAME, COMIC_NAME, i))
    lista.sort(key=lambda x: int(x.replace(".jpg", "")))
    for img in lista:
        imagePath = f'%s/%s%d/%s' % (IMG_FOLDER_NAME, COMIC_NAME, i+1, img)
        pdf.add_page()
        pdf.image(imagePath, x=0, y=0, w=A4_WIDTH, h=A4_HEIGHT)
    fileName = f'%s/Scott Pilgrim - %d.pdf' % (PDF_FOLDER_NAME, i+1)
    os.makedirs(os.path.dirname(fileName), exist_ok=True)
    pdf.output(fileName, 'F')
    print(f'Finished generating comic\'s #%d pdfs!' % i+1)
print(f'Finished generating all pdfs!')
