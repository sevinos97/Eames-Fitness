from pygame import (
    font,
    draw
)
from ui_element import UI_Element

class Text(UI_Element):
    def __init__(self, name, pos, text_font, font_size, col, text, AA=False, border=False, border_col=None):
        self.name = name
        self.pos = pos
        print(text_font)
        self.font = font.Font(text_font, font_size)
        self.font_size = font_size
        self.col = col
        self.text = str(text)
        self.border = border
        self.border_col = border_col
        self.AA = AA

        self.text_surface = self.font.render(self.text, self.AA, self.col)
        self.text_rect = self.text_surface.get_rect(center=self.pos)

    def draw(self, surf):
        if self.border:
            draw.rect(surf, self.border_col, self.text_rect, width=0)
        surf.blit(self.text_surface, self.text_rect)

    def updatePos(self):
        self.text_rect.center = self.pos

    def setText(self, text):
        self.text = text
        self.text_surface = self.font.render(self.text, self.AA, self.col)
        self.text_rect = self.text_surface.get_rect(center=self.pos)