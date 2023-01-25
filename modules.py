

#Gets the color from the pixel range in a general range
def get_color(color):
    r,g,b = color
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