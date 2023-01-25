import AILib as ai
from PIL import Image
import numpy as np
# TODO change this to input
PATH = "Images\\test.bmp"


im = Image.open(PATH)


# Specify the size of the tiles
tile_size = (15, 15)

# Calculate the number of tiles
n_tiles = (im.width // tile_size[0] + 1, im.height // tile_size[1] + 1)

tile_list = []

for i in range(n_tiles[0]):
    for j in range(n_tiles[1]):
        x = i * tile_size[0]
        y = j * tile_size[1]
        tile = im.crop((x, y, x + tile_size[0], y + tile_size[1]))
        pixels = tile.getdata()
        # Number of pixels of each color by tile
        red_pixels = sum(1 for pixel in pixels if pixel == (255, 0, 0))
        green_pixels = sum(1 for pixel in pixels if pixel == (0, 255, 0))
        black_pixels = sum(1 for pixel in pixels if pixel == (0, 0, 0))
        # total pixels
        total_pixels = len(pixels)
        # Percentage of color of pixels by tile
        black_percent = black_pixels / total_pixels
        green_percent = green_pixels / total_pixels
        red_percent = red_pixels / total_pixels
        if black_percent > 0.8:
            tile = Image.new('RGB', tile_size, (0, 0, 0))

        elif green_percent > 0.8:
            tile = Image.new('RGB', tile_size, (0, 255, 0))

        elif red_percent > 0.8:
            tile = Image.new('RGB', tile_size, (255, 0, 0))

        elif black_percent < 0.8:
            tile = Image.new('RGB', tile_size, (255, 255, 255))

        im.paste(tile, (x, y))

im.save('Result.bmp')
