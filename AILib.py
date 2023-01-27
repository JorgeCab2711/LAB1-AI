from PIL import Image
from PIL import ImageOps
import numpy as np


class AIL():
    # Initializer of the AIL object
    def __init__(self, path):
        # Image
        self.PATH = path
        self.image = self.checkImage(path)
        self.pixel_coords = self.image.load()
        # Image height and width
        self.height, self.width = self.image.size
        # Tile size
        self.tile_width = 10
        self.tile_height = 10
        self.genTiles(self.tile_width, self.tile_height)

    # Function to check if image is valid bmp format if not convert it to bmp
    def checkImage(self, path):
        newPath = ''
        im = Image.open(path)
        if ".bmp" not in path:
            with Image.open(path) as im:
                im.convert("1")
                if 'png' in path:
                    newPath = path.replace('png', 'bmp')
                    im.save(''+newPath)
                elif 'jpg' in path:
                    newPath = im.save(path.replace('jpg', 'bmp'))
                    im.save(newPath)
                if path != newPath:
                    im = Image.open(newPath)
        return im

    # Funciton generates an array with all pixel information -> cami_pixel = ((x,y), (R,G,B))
    def genPixInfList(self):
        cam_pixels = []
        for x in range(self.width):
            for y in range(self.height):
                cam_pixels.append(((x, y), (self.pixel_coords[x, y])))
        return cam_pixels

    # simple use of the save function to output the image on the desired folder
    def imageFinish(self):
        self.image.save('output/Result.bmp')

    # Map the image by tiles and return the resulting image
    def genTiles(self, tile_width, tile_height):
        # Specify the size of the tiles
        tile_size = (tile_width, tile_height)

        # Calculate the number of tiles
        n_tiles = (self.image.width //
                   tile_size[0] + 1, self.image.height // tile_size[1] + 1)

        tile_list = []

        for i in range(n_tiles[0]):
            for j in range(n_tiles[1]):
                x = i * tile_size[0]
                y = j * tile_size[1]
                tile = self.image.crop(
                    (x, y, x + tile_size[0], y + tile_size[1]))
                pixels = tile.getdata()
                # Number of pixels of each color by tile
                pixel_colors = np.array([self.get_color(pixel)
                                        for pixel in pixels])
                red_pixels = np.count_nonzero(pixel_colors == 'red')
                green_pixels = np.count_nonzero(pixel_colors == 'green')
                black_pixels = np.count_nonzero(pixel_colors == 'black')
                # total pixels
                total_pixels = len(pixels)
                # Percentage of color of pixels by tile
                black_percent = black_pixels / total_pixels
                green_percent = green_pixels / total_pixels
                red_percent = red_pixels / total_pixels
                if black_percent > 0.9:
                    tile = Image.new('RGB', tile_size, (0, 0, 0))

                elif green_percent > 0.9:
                    tile = Image.new('RGB', tile_size, (0, 255, 0))

                elif red_percent > 0.9:
                    tile = Image.new('RGB', tile_size, (255, 0, 0))

                elif black_percent < 0.9:
                    tile = Image.new('RGB', tile_size, (255, 255, 255))

                self.image.paste(tile, (x, y))

    # Gets the color from the pixel range in a general range
    def get_color(self, color):
        r, g, b = color
        if g < r/2 and b < r/2:
            return "red"
        elif r < g/2 and b < g/2:
            return "green"
        elif r < b/2 and g < b/2:
            return "blue"
        elif r < 50 and g < 50 and b < 50:
            return 'black'
        elif r < 200 and g < 200 and b < 200:
            return 'white'
