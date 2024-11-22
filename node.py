from setting import Vector2, WINDOW, nodes
from pygame import draw


class Node:
    def __init__(self, _position) -> None:
        self.position = _position
        self.gCost = 0
        self.hCost = 0
        pass

    def draw(self):
        draw.rect(WINDOW, (255, 0, 0), (self.position.x * 110, self.position.y * 110, 110 , 110))

    def getDistance(self, target):
        distX = abs(target.position.x - self.position.x)
        distY = abs(target.position.y - self.position.y)

        if distX < distY:
            return distX * 1.4 + (distY - distX)
        return distY * 1.4 + (distX - distY)
    
    def getCost(self):
        return self.gCost + self.hCost
    
    def getNeighbors(self):
        neighbors = []

        for x in range(-1, 2, 1):
            for y in range(-1, 2, 1):
                if x == 0 and y == 0:
                    continue

                node = Node(self.position + Vector2(x, y))
                neighbors.append(node)
                nodes.append(node)