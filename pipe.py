from sprite import import_sprite
from water import Water
from setting import WINDOW, transform
from enums import Direction

class Pipe:
    def __init__(self, _direction, _position) -> None:
        self.position = _position
        self.direction = _direction

        self.sprite = self.setSprite()
        self.spriteIndex = 0
        self.animateSpeed = 0.2
        pass

    def update(self):
        pass

    def draw(self):
        self.animate()
        pass

    def animate(self):
        WINDOW.blit(self.sprite[int(self.spriteIndex)], self.position)

        self.spriteIndex += self.animateSpeed

        limitIndex = len(self.sprite) - 1
        if self.spriteIndex > limitIndex:
            self.spriteIndex = 0

    def setSprite(self):
        return import_sprite(self.direction.value + ".png")

class StartPipe(Pipe):
    def __init__(self, _direction, _position) -> None:
        super().__init__(_direction, _position)

    
    def setSprite(self):
        if self.direction.value == Direction.HORIZONTAL.value:
            return import_sprite("START" + ".png")
        elif self.direction.value == Direction.VERTICAL.value:
            sprites = import_sprite("START" + ".png")
            return [transform.rotate(sprites[i], -90) for i in range(len(sprites) - 1)]