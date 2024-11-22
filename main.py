
from pygame import gfxdraw
from setting import *
from sprite import background
from scene import Scene

from enums import Direction
from pipe import Pipe, StartPipe


display.init()

class Game:
    def __init__(self) -> None:
        self.clock = time.Clock()
        self.fps = 60
        
        self.isRunning = True
        self.mousePosition = Vector2(0, 0)
        self.currentScene = Scene()
        pass

    def input(self):
        for ev in event.get():
            if ev.type == QUIT:
                self.isRunning = False

            elif ev.type == MOUSEBUTTONDOWN:
                self.mousePosition = Vector2(mouse.get_pos())        
    
    def update(self):
        self.currentScene.update()
        pass

    def draw(self):
        self.currentScene.draw()
        pass
    
    def run(self):
        while self.isRunning:
            self.clock.tick(self.fps)

            self.input()
            self.update()
            self.draw()

            display.update()

if __name__ == "__main__":
    game = Game()
    game.run()
