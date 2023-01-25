from PIL import Image
from PIL import ImageOps
import numpy as np


class AIL():
    def __init__(self, path):
        # Image
        self.PATH = path
        self.image = Image.open(path).convert('L')
        self.pixel_coords = self.image.load()
        # Image height and width
        self.height, self.width = self.image.size
        # Segment size
        self.segment_width = 20
        self.segment_height = 20
        self.segments = self.setSegments(
            self.segment_width, self.segment_height
        )
        self.segmented_img = self.image.quantize(colors=4)

    # Function sets the segment limits on image

    def setSegments(self, segmentW, segmentH):
        segments = []
        for y in range(0, self.height, segmentH):
            for x in range(0, self.width, segmentW):
                segment = self.image.crop((x, y, x + segmentW, y + segmentH))
                segments.append(segment)

    # Funciton generates an array with all pixel information -> cami_pixel = ((x,y), (R,G,B))
    def genPixInfList(self):
        cam_pixels = []
        for x in range(self.width):
            for y in range(self.height):
                cam_pixels.append(((x, y), (self.pixel_coords[x, y])))
        return cam_pixels

    def modSegments(self):
        color_count = self.segmented_img.getcolors(
            self.segmented_img.size[0]*self.segmented_img.size[1])
        segment_colors = []
        for count, color in color_count:
            segment_colors.append(color)

    def imageFinish(self):
        self.image.save('Result.bmp')


# Gets the color from the pixel range in a general range
def get_color(color):
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
        return 'black'
