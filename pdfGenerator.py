import os
from tqdm import tqdm
from fpdf import FPDF
IMG_FOLDER_NAME = "IMAGES"
PDF_FOLDER_NAME = "PDFS"
COMIC_PREFIX = "COMIC_"
A4_WIDTH = 210
A4_HEIGHT = 297

print('Started generating all pdfs...')
for i in range(6):
    print(f'Generating comic #{str(i)} pdf...')
    pdf = FPDF()
    lista = os.listdir(f'{IMG_FOLDER_NAME}/{COMIC_PREFIX}{str(i)}')
    lista.sort(key=lambda x: int(x.replace(".jpg", "")))
    for img in lista:
        imagePath = f'{IMG_FOLDER_NAME}/{COMIC_PREFIX}{str(i)}/{img}'
        pdf.add_page()
        pdf.image(imagePath, x=0, y=0, w=A4_WIDTH, h=A4_HEIGHT)
    fileName = f'{PDF_FOLDER_NAME}/Scott Pilgrim - {str(i+1)}.pdf'
    os.makedirs(os.path.dirname(fileName), exist_ok=True)
    pdf.output(fileName, 'F')
    print(f'Finished generating comic #{str(i+1)} pdf!')
print(f'Finished generating all pdfs!')
