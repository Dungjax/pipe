from enums import State, Direction
from setting import WINDOW, Vector2, nodes
from sprite import import_sprite, background
from pipe import Pipe, StartPipe
from node import Node
from path_finding import PathFinding

start = Node(Vector2(1, 1))
end = Node(Vector2(1, 1))

end.getNeighbors()

nodes.append(start)
nodes.append(end)

open = [start]
closed = []

pathFinding = PathFinding()

class Scene:
    def __init__(self) -> None:
        self.state = State.READY
        pass

    def update(self):
        pathFinding.findPath(start, end)
        pass
    
    def draw(self):
        backgroundPosition = Vector2(0, 0)
        WINDOW.blit(background, backgroundPosition)

        for node in nodes:
            node.draw()

        pass