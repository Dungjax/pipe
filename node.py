from setting import Vector2, WINDOW, TILE_SIZE, drawText, GRID_SIZE
from pygame import draw, Surface
from grid import toWorldPoint
from enums import NodeType, Direction

walls = {}

class Node:
    def __init__(self, _position) -> None:
        self.position = _position
        self.gCost = 0
        self.hCost = 0
        self.parent = self
        self.startDirection = Direction.DOWN
        self.endDirection = Direction.TOP
        
        self.type = NodeType.BLOCKED if walls.get(tuple(self.position)) != None  else NodeType.ALLOWED
        pass

    def getDistance(self, target):
        distX = abs(target.position.x - self.position.x)
        distY = abs(target.position.y - self.position.y)

        return distX + distY

        diagonalCoeff = 14
        if distX < distY:
            return distX * diagonalCoeff + (distY - distX) * 10
        return distY * diagonalCoeff + (distX - distY) * 10
    
    def getCost(self):
        return self.gCost + self.hCost
    
    def getNeighbors(self, type):
        neighbors = []

        cords = [Vector2(0, -1), Vector2(-1, 0), Vector2(1, 0), Vector2(0, 1)]

        for cord in cords:
            nodePosition = Vector2(self.position + Vector2(cord.x, cord.y))

            node = type(nodePosition)

            if nodePosition.x < 0 or nodePosition.x >= GRID_SIZE or nodePosition.y < 0 or nodePosition.y >= GRID_SIZE or node.type == NodeType.BLOCKED:
                continue
                
            neighbors.append(node)

        # for x in range(-1, 2, 1):
        #     for y in range(-1, 2, 1):
        #         nodePosition = Vector2(self.position + Vector2(x, y))
        #         node = self.__class__(nodePosition)

        #         if Vector2(x, y) == Vector2(0, 0) or nodePosition.x < 0 or nodePosition.y < 0 or node.type == NodeType.BLOCKED:
        #             continue
                
        #         neighbors.append(node)

        return neighbors
    
    def changeDirection(self):
        direction = self.position - self.parent.position

        if direction.x > 0:
            self.startDirection = Direction.LEFT
        elif direction.x < 0:
            self.startDirection = Direction.RIGHT

        if direction.y > 0:
            self.startDirection = Direction.TOP
        elif direction.y < 0:
            self.startDirection = Direction.DOWN

        if self.startDirection == Direction.LEFT:
            self.parent.endDirection = Direction.RIGHT
        elif self.startDirection == Direction.RIGHT:
            self.parent.endDirection = Direction.LEFT

        if self.startDirection == Direction.TOP:
            self.parent.endDirection = Direction.DOWN
        elif self.startDirection == Direction.DOWN:
            self.parent.endDirection = Direction.TOP

class BlockedNode(Node):
    def __init__(self, _position) -> None:
        super().__init__(_position)

        walls[tuple(self.position)] = self

    def draw(self):
        draw.rect(WINDOW, (0, 0, 0), (toWorldPoint(self.position.x), toWorldPoint(self.position.y), TILE_SIZE , TILE_SIZE))
        #drawText(self.getCost(), self.position)