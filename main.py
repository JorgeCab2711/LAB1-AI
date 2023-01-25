import modules as mod
from PIL import Image

# TODO change this to input
PATH = "Images\\test.bmp"
im = Image.open(PATH)

# Setting and normalizing coordinates
width, height = im.size

# pixel coordinates
pixel_coords = im.load()
start = []
end = []
wall = []

# cami_pixel = ((x,y), (R,G,B))
# Iterarar la lista de pixeles y agregar todas sus caracteristicas en una lista de tuplas
cam_pixels = []
for x in range(width):
    for y in range(height):
        cam_pixels.append(((x, y), (pixel_coords[x, y])))

# obterner los pixeles que tienen color verde, estos marcaran los puntos de inicio
for i in cam_pixels:
    gamma = mod.get_color(i[1])
    if gamma == 'green':
        start.append(i[0])
        print(gamma)

# obterner los puntos
for i in cam_pixels:
    gamma = mod.get_color(i[1])
    if gamma == 'green':
        start.append(i[0])
        print(gamma)


# END
# im.show()
