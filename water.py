from sprite import import_sprite
from setting import WINDOW


class Water:
    def __init__(self, _direction, _position) -> None:
        self.direction = _direction
        self.position = _position

        self.sprite = import_sprite(self.direction + "WATER.png")
        self.spriteIndex = 0
        self.animateSpeed = 0.2
        pass

    def update(self):
        pass

    def draw(self):
        self.animate()
        pass

    def animate(self):
        WINDOW.blit(self.sprite[self.spriteIndex])

        self.spriteIndex += self.animateSpeed

        limitIndex = self.sprite.size() - 1
        if self.spriteIndex > limitIndex:
            self.spriteIndex = 0

        pass