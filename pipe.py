from sprite import pipeSprites, startPipeSprites, wallSprite
from pygame import Surface, draw
from setting import WINDOW, transform, TILE_SIZE
from node import Node, BlockedNode
from grid import toWorldPoint
from enums import Direction

pipes = []
endPipes = []

class Pipe(Node):
    def __init__(self, _position) -> None:
        super().__init__(_position)

        self.sprite = Surface((50, 50))
        self.spriteIndex = 0
        self.animateSpeed = 0.5
        self.limitIndex = 0
        pass

    def update(self):
        pass

    def draw(self):
        #draw.rect(WINDOW, (0, 0, 0), (toWorldPoint(self.position.x), toWorldPoint(self.position.y), TILE_SIZE , TILE_SIZE))
        self.animate()
        pass

    def animate(self):
        WINDOW.blit(self.sprite[int(self.spriteIndex)], toWorldPoint(self.position))

        if self.parent.spriteIndex == self.parent.limitIndex or self.parent == self:
            self.spriteIndex += self.animateSpeed

            if self.spriteIndex > self.limitIndex:
                self.spriteIndex = self.limitIndex

    def setSprite(self):
        self.sprite = pipeSprites[self.startDirection.value + self.endDirection.value]
        self.limitIndex = len(self.sprite) - 1
        pass

class StartPipe(Pipe):
    def __init__(self, _position) -> None:
        super().__init__(_position)

    def setSprite(self):
        self.sprite = startPipeSprites[self.endDirection.value]
        self.limitIndex = len(self.sprite) - 1

class Wall(BlockedNode):
    def __init__(self, _position) -> None:
        super().__init__(_position)

        self.sprite = wallSprite

    def draw(self):
        WINDOW.blit(self.sprite, toWorldPoint(self.position))
    

