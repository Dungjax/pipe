
from setting import *
from scene import Scene

display.init()

class Game:
    def __init__(self) -> None:
        self.clock = time.Clock()
        self.fps = 60
        
        self.isRunning = True

        self.isPressed = False
        self.mousePosition = Vector2(0, 0)

        self.currentScene = Scene()
        pass

    def input(self):
        for ev in event.get():
            if ev.type == QUIT:
                self.isRunning = False

            elif ev.type == MOUSEBUTTONDOWN:
                self.isPressed = True
                self.mousePosition = Vector2(mouse.get_pos())

            else:
                self.isPressed = False

            self.currentScene.input(self.isPressed, self.mousePosition)  
    
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
