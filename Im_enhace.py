from PIL import Image, ImageEnhance, ImageFilter
import os


# Cambio direccion OS
os.chdir(r'C:\Users\mfgon\Pictures')

path = '.\imgs' #carpeta de imágenes a editar
pathOut = '.\editedImgs' #carpeta almacenaje imagenes editadas

#
''' rgb2xyz = (
    0.412453, 0.357580, 0.180423, 0,
    0.212671, 0.715160, 0.072169, 0,
    0.019334, 0.119193, 0.950227, 0)
'''
#Sepia
rgb2xyz = (
    0.393, 0.769, 0.189, 0,
    0.349, 0.686, 0.168, 0,
    0.272, 0.534, 0.131, 0.5)


for filename in os.listdir(path):
    img = Image.open(f"{path}\{filename}")
    edit = img.filter(ImageFilter.EDGE_ENHANCE_MORE).convert('RGB',rgb2xyz)
    
    #edit = img.filter(ImageFilter.SHARPEN).convert('L') #Escala de grises
    # .EDGE_ENHANCE #.EDGE_ENHANCE_MORE 
    factor  = 1.5
    enhacer = ImageEnhance.Contrast(edit)
    edit = enhacer.enhance(factor)
    clean_name = os.path.splitext(filename)[0]
    edit.save(f'{pathOut}\{clean_name}_edited3.jpg') 
    #Si existe una imagen con el mismo nombre, la reescribe