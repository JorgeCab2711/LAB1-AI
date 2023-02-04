'''
Universidad del Valle de Guatemala
Inteligencia Artificial
Laboratorio 1
Autor: Jorge Caballeros Perez
Purpose: Create an AI that can solve a labrynth using BFS, DFS, and Euristics
'''

from PIL import Image
import numpy as np
import random
from framework import GraphSearch


class AIL():
    # Initializer of the AIL object
    def __init__(self, path):
        # Image
        self.PATH = path
        self.image = self.checkImage(path)
        self.pixel_coords = self.image.load()
        # Image height and width
        self.height, self.width = self.image.size

        # Mapped Tile lists
        self.path_tiles = []
        self.wall_tiles = []
        self.green_tiles = []
        self.red_tiles = []
        # Initialize an empty matrix with the defined size
        self.matrix = []

        # Tile size
        '''
        NOTE:   play with the tile size if the border density is too big, the lower the size,
                the better the image quality, but this affects performance a lot.
        '''
        self.tile_width = 10
        self.tile_height = 10
        # Correct the image to tiles
        self.genTiles(self.tile_width, self.tile_height)
        self.start = self.get_start()
        self.end = self.get_end()

        # Start the AI
        gs = GraphSearch()
        path = gs.dfs(self.matrix, self.start, self.end)
        print(path)
        print(max(path, key=lambda tup: tup[0]))
        self.paintPath(path)

    # Map the image by tiles and return the resulting image

    def genTiles(self, tile_width, tile_height):

        # Specify the size of the tiles
        self.tile_size = (tile_width, tile_height)
        # Calculate the number of tiles
        n_tiles = (self.image.width //
                   self.tile_size[0] + 1, self.image.height // self.tile_size[1] + 1)

        self.matrix = [[0 for x in range((n_tiles[0]*10)-9)]
                       for y in range((n_tiles[1]*10)-9)]

        for i in range(n_tiles[0]):
            for j in range(n_tiles[1]):
                x = i * self.tile_size[0]
                y = j * self.tile_size[1]
                tile = self.image.crop(
                    (x, y, x + self.tile_size[0], y + self.tile_size[1]))
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

                # If tile is black
                if black_percent > 0.9:
                    tile = Image.new('RGB', self.tile_size, (0, 0, 0))
                    self.matrix[x][y] = 1
                    # Map the tile to: (x cord, y cord)
                    self.wall_tiles.append((x, y))
                    self.path_tiles.append((x, y))
                # If tile is green
                elif green_percent > 0.9:
                    self.matrix[x][y] = 0
                    tile = Image.new('RGB', self.tile_size, (0, 255, 0))
                    # Map the tile to: (x cord, y cord)
                    self.green_tiles.append((x, y))
                    self.path_tiles.append((x, y))
                # If tile is red
                elif red_percent > 0.9:
                    self.matrix[x][y] = 0
                    tile = Image.new('RGB', self.tile_size, (255, 0, 0))
                    # Map the tile to: (x cord, y cord)
                    self.red_tiles.append((x, y))
                    self.path_tiles.append((x, y))

                # If tile is white
                else:
                    self.matrix[x][y] = 0
                    self.path_tiles.append((x, y))
                    tile = Image.new('RGB', self.tile_size, (255, 255, 255))

                self.image.paste(tile, (x, y))

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

    # simple use of the save function to output the image on the desired folder
    def imageFinish(self):
        self.image.save('output/Result.bmp')

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

    # paint the path tiles
    def paintPath(self, matrix):
        for x, y in matrix:
            newImage = Image.new('RGB', self.tile_size, (204, 90, 90))
            self.image.paste(newImage, (int(x), int(y)))

    def get_start(self):
        start = self.green_tiles
        return start[random.randint(0, len(start)-1)]

    def get_end(self):
        end = self.red_tiles
        return end[random.randint(0, len(end)-1)]
