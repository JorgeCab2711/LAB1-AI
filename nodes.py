from PIL import Image


class nodes():
    def __init__(self, tile: Image, parent):
        self.visited = False
        self.parent = parent

    def setVisited(self):
        self.visited = True
        self.color = (204, 100, 100)
