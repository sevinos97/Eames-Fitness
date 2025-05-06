from pygame import (
    Rect,
    draw,
    MOUSEBUTTONUP,
    MOUSEMOTION,
    font,
    Color
)
from ui_element import UI_Element
# chat how we doin
class Button(UI_Element):
    def __init__(self, name, pos, width=150, height=150, **kwargs):
        self.name = name
        self.width = width
        self.height = height
        self.pos = pos
        self.draw_pos = pos
        self.hover_col = kwargs.get('hover_col', None)
        self.col = kwargs.get('col', Color(210, 210, 210))
        self.draw_col = self.col
        self.text = kwargs.get('text', '')
        self.font_size = kwargs.get('font_size', int(self.height / 2))
        self.font = font.Font('freesansbold.ttf', self.font_size)
        self.text_col = kwargs.get('text_col', Color(0, 0, 0))
        self.visible = kwargs.get('visible', True)
        self.active = kwargs.get('active', True)
        self.text_surf = self.font.render(self.text, True, self.text_col)
        self.text_rect = self.text_surf.get_rect(center=pos)
        self.rect = Rect(0, 0, width, height)
        self.rect.center = self.draw_pos
        self.border_rad = kwargs.get('border_radius', 0)

    def draw(self, surf):
        if self.visible:
            draw.rect(surf, self.draw_col, self.rect, border_radius=self.border_rad)
            surf.blit(self.text_surf, self.text_rect)

    def setText(self, text):
        self.text = text
        if self.text_col is not None:
            self.text_surf = self.font.render(self.text, True, self.text_col)
            self.text_rect = self.text_surf.get_rect(center=self.pos)

    def handleEvent(self, event):
        if self.active:
            if event.type == MOUSEBUTTONUP and self.rect.collidepoint(event.pos) and event.button == 1:
                return self
            elif event.type == MOUSEMOTION and self.rect.collidepoint(event.pos):
                self.draw_col = self.hover_col
            elif event.type == MOUSEMOTION and not self.rect.collidepoint(event.pos):
                self.draw_col = self.col

    def updatePos(self):
        self.rect.center = self.pos
        self.text_rect.center = self.pos