from pygame import image, transform
from os import walk

def import_image(_path):
    return image.load(_path)

def import_sprite(_path):
    origin = image.load(_path)
    
    width = origin.get_width()
    height = origin.get_height()
    collums = width // height
    
    return [origin.subsurface((i * height, 0, width // collums, height)) for i in range(collums)]

background = import_image("assets/bg.png")