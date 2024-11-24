from pygame import MOUSEBUTTONDOWN, Vector2, display, event
from button import Button

display.init()

WIDTH = 800
HEIGHT = 800

WINDOW = display.set_mode((WIDTH, HEIGHT))

isRunning = True

nodeButton = Button(Vector2())

while isRunning:
    for ev in event.get():
        if ev.type == MOUSEBUTTONDOWN:
            pass

        
    WINDOW.fill((0, 0, 0))

    display.update()



class Node:
    def __init__(self, _position) -> None:
        self.position = _position
        pass