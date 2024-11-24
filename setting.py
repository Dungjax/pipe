from pygame import display, transform, event, time, Vector2, MOUSEBUTTONDOWN, MOUSEBUTTONUP, QUIT, mouse, font

font.init()

WIDTH = 1000
HEIGHT = 800

GRID_SIZE = 16

WINDOW = display.set_mode((WIDTH, HEIGHT))

TILE_SIZE = 50

defaultFont = font.Font(None, 20)

RED = (255, 0, 0)
BLACK = (0, 0, 0)

def drawText(_text, position):
    text = defaultFont.render(str(_text), True, BLACK)
    WINDOW.blit(text, position * TILE_SIZE)