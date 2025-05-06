from pygame import (
    image,
    transform
)
from ui_element import UI_Element

class Image(UI_Element):
    def __init__(self, name, img_name, pos, scale):
        self.name = name
        self.img = image.load(img_name)
        self.scale = scale
        self.scaled = transform.scale_by(self.img, scale)
        self.pos = pos
        self.rect = self.scaled.get_rect(center=pos)

    def draw(self, surf):
        surf.blit(self.scaled, self.rect)

    def updatePos(self):
        self.rect = self.scaled.get_rect(center=self.pos)