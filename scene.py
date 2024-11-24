from enums import State, Direction
from setting import WINDOW, Vector2, WIDTH, HEIGHT, GRID_SIZE, drawText
from sprite import import_sprite, background, wallSprite, playSprite, findSprite
from pipe import Pipe, StartPipe, EndPipe, Wall, pipes, endPipes
from node import walls, NodeType
from path_finding import findPath, nodes
from grid import toLocalPoint, grids
from button import Button, buttons

start = StartPipe(Vector2(5, 5), Direction.LEFT, Direction.RIGHT)
start.setSprite()

end = EndPipe(Vector2(9, 9), Direction.DOWN, Direction.TOP)
end.setSprite()
#walls[tuple(end.position)] = end

wall = Wall(Vector2(7, 7))
walls[tuple(wall.position)] = wall
grids[tuple(wall.position)] = wall
wall = Wall(Vector2(7, 6))
walls[tuple(wall.position)] = wall
grids[tuple(wall.position)] = wall
wall = Wall(Vector2(7, 5))
walls[tuple(wall.position)] = wall
grids[tuple(wall.position)] = wall

findPath(start, end)
n1 = []
for n in nodes:
    n1.append(n.position)

startPipeButton = Button(Vector2(900, 200), playSprite)
endPipeButton = Button(Vector2(900, 300), findSprite)
addWallButton = Button(Vector2(900, 400), wallSprite)

for i in range(len(nodes)):
    nodes[i].position = Vector2(175, 80)

class Scene:
    def __init__(self) -> None:
        self.state = State.READY
        self.c = 0
        self.stage = 1
        pass

    def input(self, _isPressed, _mousePosition):
        for button in buttons:
            button.input(_isPressed, _mousePosition)

        if _isPressed:
            localMousePosition = toLocalPoint(_mousePosition)

            if endPipeButton.isActive:
                findPath(start, end)

            if localMousePosition.x < GRID_SIZE:
                if self.stage == 1:
                    if self.c < len(nodes):
                        if localMousePosition == n1[self.c]:
                            nodes[self.c].position = localMousePosition
                            self.c += 1

                if walls.get(tuple(localMousePosition)) == None:

                    if addWallButton.isActive:
                        wall = Wall(localMousePosition)
                        walls[tuple(wall.position)] = wall
                        grids[tuple(wall.position)] = wall

                elif grids.get(tuple(localMousePosition)).__class__ == Wall:
                    grids.pop(tuple(localMousePosition))
                    walls.pop(tuple(localMousePosition))
        pass

    def update(self):
        if len(nodes) > 0:
            if nodes[len(nodes) - 1].isFinish == True:
                start.position = Vector2(0, 0)
                end.position = Vector2(15, 15)

                nodes.clear()
                pipes.clear()
                walls.clear()

                self.stage += 1
        
        if self.stage != 1:
            self.c = len(nodes)
        pass
    
    def draw(self):

        backgroundPosition = Vector2(0, 0)
        WINDOW.blit(background, backgroundPosition)

        drawText(self.c, Vector2(900, 100))

        for i in range(3):
            if i + self.c < len(nodes):
                WINDOW.blit(nodes[i + self.c].sprite[0], Vector2(900, 500 + i * 50))
            
                

        start.draw(startPipeButton.isActive)
        end.draw(startPipeButton.isActive)
        for pipe in pipes:
            pipe.draw(startPipeButton.isActive)

        for wall in walls:
            walls.get(wall).draw()

        for button in buttons:
            button.draw()
        pass