from PIL import Image, ImageEnhance, ImageFilter

import os

# Get the current working directory

os.chdir(r'C:\Users\mfgon\Pictures')

path = '.\imgs'
pathOut = '.\editedImgs'

for filename in os.listdir(path):
    img = Image.open(f"{path}\{filename}")
    edit = img.filter(ImageFilter.SHARPEN).convert('L')
    factor  = 1.5
    enhacer = ImageEnhance.Contrast(edit)
    edit = enhacer.enhance(factor)
    clean_name = os.path.splitext(filename)[0]
    edit.save(f'{pathOut}\{clean_name}_edited.jpg')