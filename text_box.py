from pygame import *
from ui_element import UI_Element

class TextBox(UI_Element):
    def __init__(self, name, pos, box_width, box_height, box_col, text_col, on=True, visible=True, clicksable=False):
        self.pos = pos
        self.name = name
        self.box_width = box_width
        self.box_height = box_height
        random_ass_constant = 6.91931415921 # lmaoooo
        self.font_size = min(int(box_width/random_ass_constant), box_height)
        self.box_col = box_col
        self.text_col = text_col
        self.rect = Rect(0, 0, box_width, box_height)
        self.rect.center = self.pos
        self.text = str()
        self.font = font.SysFont('Comic Sans MS', self.font_size)
        self.on = on
        self.visible = visible
        self.clicksable = clicksable
        
        self.active=False
        self.text_cursor = False
        self.text_cursor_rect = Rect(0, 0, 2, self.font_size)
        self.cursor_color = Color(0, 0, 0 )
        self.t1, self.t0 = 0, 0
        self.cursor_cooldown = 500 # ms

    def draw(self, surf):
        # draw box
        if self.visible:
            draw.rect(surf, self.box_col, self.rect, width=0)
            #draw text
            text_surf = self.font.render(self.text, True, self.text_col)
            text_rect = text_surf.get_rect(center=self.rect.center)
            surf.blit(text_surf, text_rect)
            if self.text_cursor:
                self.text_cursor_rect.midleft = text_rect.midright
                draw.rect(surf, self.cursor_color, self.text_cursor_rect)
            print(f'Drawing {self.name}')

    def disable(self):
        self.on, self.visible = False, False

    def enable(self):
        self.on, self.visible = True, True

    def handleEvent(self, event):
        if self.on:
            if event.type == MOUSEBUTTONUP:
                if not self.active and self.rect.collidepoint(event.pos):
                    self.active = True
                    self.text_cursor = True
                elif self.active and not self.rect.collidepoint(event.pos):
                    self.active = False
                    self.text_cursor = False
                    if self.clicksable:
                        self.disable()
            
            elif event.type == KEYDOWN:
                if self.active:
                    if event.key == K_RETURN:
                        ret = self.text
                        self.text = ''
                        self.active = False
                        self.cursor = False
                        if self.clicksable:
                            self.disable()
                        return self.name, ret
                    elif event.key == K_BACKSPACE:
                        self.text = self.text[:-1]
                    else:
                        self.text += event.unicode
        
        return None
    
    def updatePos(self):
        self.rect.center = self.pos

    def update(self):
        if self.active:
            self.t1 = time.get_ticks()
            if self.t1 - self.t0 >= 500:
                self.text_cursor = not self.text_cursor
                self.t0 = self.t1

        else:
            self.t1 = time.get_ticks()
            self.t0 = time.get_ticks()