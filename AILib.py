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
        # Mapping all the tiles
        self.mapped_coords = self.map_image()
        # Mapped Tile lists
        self.tile_list = self.map_image()
        self.wall_tiles = []
        self.green_tiles = []
        self.red_tiles = []
        # Tile size
        '''
        NOTE:   play with the tile size if the border density is too big, the lower the size, 
                the better the image quality, but this affects performance a lot.
        '''
        self.tile_width = 10
        self.tile_height = 10
        # Correct the image to tiles
        self.genTiles(self.tile_width, self.tile_height)
        # set the borders
        self.setBorders()
        # set the start and end tiles randomly
        self.start_tile = self.get_start()
        self.end_tile = self.get_end()

        print(self.end_tile, ' end tile')
        print(self.start_tile, ' start tile')

        # clean the matrix
        matrix = self.cleanMatrix()

        # Start the AI
        # print(matrix)

        path = GraphSearch.dfs(matrix, self.start_tile, self.end_tile)
        print(path)
        for i in path:
            newImage = Image.new('RGB', self.tile_size, (255,100,100))
            self.image.paste(newImage, )

    # Setting the labrynth's borders

    def setBorders(self):
        # Loop through all the tiles in the image
        for i in range(0, self.width, self.tile_width):
            for j in range(0, self.height, self.tile_height):
                # If the tile is a border tile
                if i == 0 or i == self.width-self.tile_width or j == 0 or j == self.height-self.tile_height:
                    # Paint the tile black
                    for k in range(self.tile_width):
                        for l in range(self.tile_height):
                            self.image.putpixel((i+k, j+l), (0, 0, 0))

        # Save the new image
        self.image.save("./output/Result.bmp")

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

    # Map the image by tiles and return the resulting image

    def genTiles(self, tile_width, tile_height):

        # Specify the size of the tiles
        self.tile_size = (tile_width, tile_height)
        # Calculate the number of tiles
        n_tiles = (self.image.width //
                   self.tile_size[0] + 1, self.image.height // self.tile_size[1] + 1)

        for i in range(n_tiles[0]):
            for j in range(n_tiles[1]):
                x = i * self.tile_size[0]
                y = j * self.tile_size[1]
                tile = self.image.crop(
                    (x, y, x + self.tile_size[0], y + self.tile_size[1]))
                pixels = tile.getdata()
                self.tile_list.append(tile)

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
                    tile = Image.new('RGB', self.tile_size, (0, 0, 0))
                    # Map the tile to: (x cord, y cord, (color))
                    mapped_tile = ((x, y))
                    self.wall_tiles.append(mapped_tile)

                elif green_percent > 0.9:
                    tile = Image.new('RGB', self.tile_size, (0, 255, 0))
                    # Map the tile to: (x cord, y cord, (color))
                    self.green_tiles.append((x, y))

                elif red_percent > 0.9:
                    tile = Image.new('RGB', self.tile_size, (255, 0, 0))
                    # Map the tile to: (x cord, y cord, (color))
                    self.red_tiles.append((x, y))

                elif black_percent < 0.9:
                    tile = Image.new('RGB', self.tile_size, (255, 255, 255))

                self.image.paste(tile, (x, y))

    # Funciton generates an array with all pixel information -> cami_pixel = ((x,y), (R,G,B))
    def map_image(self):
        cam_pixels = []
        for x in range(self.width):
            for y in range(self.height):
                cam_pixels.append((x, y))
        return cam_pixels

    # sets the initial tile where it will start randomly
    def get_start(self):
        start = self.green_tiles
        return start[random.randint(0, len(start)-1)]

    def get_end(self):
        end = self.red_tiles
        return end[random.randint(0, len(end)-1)]

    def cleanMatrix(self):
        clMatrix = self.mapped_coords
        for i in self.wall_tiles:
            if i in clMatrix:
                clMatrix.remove(i)
            else:
                pass
        return clMatrix
