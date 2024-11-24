from pygame import sprite
from sprite import pipeButtonSprite
from setting import WINDOW

buttons = sprite.Group()


class Button(sprite.Sprite):
    def __init__(self, _position, _sprite) -> None:
        super().__init__()
        self.isActive = False

        self.sprite = _sprite
        self.rect = self.sprite.get_rect()
        self.rect.center = _position

        buttons.add(self)
        pass

    def input(self, _isPressed, _mousePosition):
        # if _isPressed:
        if self.rect.collidepoint(_mousePosition):
            for button in buttons:
                button.isActive = False
            self.isActive = True
            pass

    def draw(self):
        WINDOW.blit(self.sprite, self.rect)