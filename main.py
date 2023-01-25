import modules as mod
from PIL import Image

#TODO change this to input
PATH = "Images\lab1.bmp"
im = Image.open(PATH)

    
pixels = list(im.getdata())
width, height = im.size
pixels = [pixels[i * width:(i + 1) * width] for i in range(height)]

pixel_cords = []
start = []




# for pixel in pixels:
#     if mod.get_color(pixel) == ('green'):
#         start.append(pixel)
        

#END
#im.show()