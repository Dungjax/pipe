from pygame import image, transform
from os import walk

def import_image(_path):
    return image.load(_path)

def import_sprite(_path):
    origin = image.load(_path).convert_alpha()
    
    width = origin.get_width()
    height = origin.get_height()
    collums = width // height
    
    return [origin.subsurface((i * height, 0, width // collums, height)).convert_alpha() for i in range(collums)]

background = import_image("assets/bg.png").convert()

pipeSprites = {
    "DL" : import_sprite("assets/D_Ls.png"),
    "DR" : import_sprite("assets/D_Rs.png"),
    "DT" : import_sprite("assets/D_Ts.png"),
    "LD" : import_sprite("assets/L_Ds.png"),
    "LR" : import_sprite("assets/L_Rs.png"),
    "LT" : import_sprite("assets/L_Ts.png"),
    "RD" : import_sprite("assets/R_Ds.png"),
    "RL" : import_sprite("assets/R_Ls.png"),
    "RT" : import_sprite("assets/R_Ts.png"),
    "TD" : import_sprite("assets/T_Ds.png"),
    "TL" : import_sprite("assets/T_Ls.png"),
    "TR" : import_sprite("assets/T_Rs.png"),
    "TT" : import_sprite("assets/T_Ts.png"),

}

startPipeSprites = {
    "D" : import_sprite("assets/START_D.png"),
    "L" : import_sprite("assets/START_L.png"),
    "R" : import_sprite("assets/START_R.png"),
    "T" : import_sprite("assets/START_T.png")
}

endPipeSprites = {
    "D" : import_sprite("assets/END_D.png"),
    "L" : import_sprite("assets/END_L.png"),
    "R" : import_sprite("assets/END_R.png"),
    "T" : import_sprite("assets/END_T.png")
}


wallSprite = import_image("assets/wall.png").convert()
playSprite = import_image("assets/play.png").convert()
findSprite = import_image("assets/find.png").convert()

pipeButtonSprite = import_image("assets/wall.png")