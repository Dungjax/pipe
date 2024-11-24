from enums import State, Direction
from setting import WINDOW, Vector2, WIDTH, HEIGHT, GRID_SIZE
from sprite import import_sprite, background
from pipe import Pipe, StartPipe, Wall, pipes, endPipes
from node import walls, NodeType
from path_finding import findPath
from grid import toLocalPoint
from button import Button, buttons

start = StartPipe(Vector2(2, 2))

end = Pipe(Vector2(13, 7))

startPipeButton = Button(Vector2(900, 100))
endPipeButton = Button(Vector2(900, 200))
addWallButton = Button(Vector2(900, 300))

class Scene:
    def __init__(self) -> None:
        self.state = State.READY
        pass

    def input(self, _isPressed, _mousePosition):
        if _isPressed:
            localMousePosition = toLocalPoint(_mousePosition)

            if localMousePosition.x < GRID_SIZE:
                if startPipeButton.isActive:
                    start.position = localMousePosition
                    findPath(start, end)

                if endPipeButton.isActive:
                    
                    end.position = localMousePosition
                    findPath(start, end)

                if addWallButton.isActive:
                    
                    if walls.get(tuple(localMousePosition)).__class__ != Wall:
                        print(9)
                        wall = Wall(localMousePosition)
                        walls[tuple(wall.position)] = wall
                    else:
                        walls.pop(tuple(localMousePosition))
                        pass
                    
                    
        
        for button in buttons:
            button.input(_isPressed, _mousePosition)
        pass

    def update(self):
        pass
    
    def draw(self):

        backgroundPosition = Vector2(0, 0)
        WINDOW.blit(background, backgroundPosition)

        for pipe in pipes:
            pipe.draw()

        for wall in walls:
            walls.get(wall).draw()

        for button in buttons:
            button.draw()
        pass