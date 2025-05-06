from ui_element import UI_Element
from pygame import (
    Rect, 
    image,
    draw,
    font,
    transform,
    Color
)

class Panel(UI_Element):
    def __init__(self, name, pos, width=150, height=150, **kwargs):
        self.name = name
        self.width = width
        self.height = height
        self.pos = pos
        self.pos_orig = pos

        self.rect_col = kwargs.get('rect_col', Color(210, 210, 210))
        self.border_radius = kwargs.get('border_radius', 0)
        self.img_name = kwargs.get('img_name', None)
        self.img_scale = kwargs.get('img_scale', 0)
        self.font_size = kwargs.get('font_size', int(self.height * 0.2) if self.img_name else self.height)
        self.font = kwargs.get('font', font.SysFont('Arial', self.font_size)) 
        self.text = kwargs.get('text', None)
        self.text_col = kwargs.get('text_col', Color(0, 0, 0))
        self.visible = kwargs.get('visible', True)
        self.rect = Rect(0, 0, width, height)
        self.rect.center = pos

        self.img = None
        self.text_surf = None
        self.padding_y = int(height * 0.05)

        if self.img_name:
            self.img = image.load(self.img_name)
            if self.img_scale <= 0:
                img_w, img_h = self.img.get_size()
                w_ratio = self.width * 0.6 / img_w
                h_ratio = self.height * 0.6 / img_h
                self.img_scale = min(w_ratio, h_ratio)
            self.scaled = transform.scale_by(self.img, self.img_scale)
            if self.text:
                self.img_rect = self.scaled.get_rect(midtop=self.rect.midtop)
                self.img_rect.y += self.padding_y
            else:
                self.img_rect = self.scaled.get_rect(center=self.pos)

        self.total_height, self.line_spacing = 0, 0
        if self.text:
            self.line_spacing = 0
            self.lines = self.text.split('\n')
            self.text_surfs = []
            self.text_rects = []
            self.total_height = 0
            
            for line in self.lines:
                surf = self.font.render(line, True, self.text_col)
                rect = surf.get_rect()
                self.text_surfs.append(surf)
                self.text_rects.append(rect)
                self.total_height += rect.height + self.line_spacing
            self.total_height -= self.line_spacing

            if self.img is not None:
                self.text_center = (self.rect.centerx, self.rect.bottom - self.padding_y - self.total_height // 2)
            else:
                self.text_center = self.rect.centerx, self.rect.centery
            self.start_y = self.text_center[1] - self.total_height // 2

            for rect in self.text_rects:
                rect.centerx = self.text_center[0]
                rect.y = self.start_y
                self.start_y += rect.height + self.line_spacing


    def draw(self, surf):
        if self.visible:
            draw.rect(surf, self.rect_col, self.rect, border_radius=self.border_radius)
            if self.img is not None:
                surf.blit(self.scaled, self.img_rect)
            if self.text_surfs:
                for text_surf, rect in zip(self.text_surfs, self.text_rects):
                    surf.blit(text_surf, rect)

    def updatePos(self):
        self.rect.center = self.pos
        if self.img:
            self.img_rect.midtop = self.rect.midtop
            self.img_rect.y += self.padding_y
        if self.text:
            if self.img is not None:
                self.text_center = (self.rect.centerx, self.rect.bottom - self.padding_y - self.total_height // 2)
            else:
                self.text_center = self.rect.center
                
            self.start_y = self.text_center[1] - self.total_height // 2
            for rect in self.text_rects:
                rect.centerx = self.text_center[0]
                rect.y = self.start_y
                self.start_y += rect.height + self.line_spacing

    def updateText(self):   

        self.total_height, self.line_spacing = 0, 0
        if self.text:
            self.line_spacing = 0
            self.lines = self.text.split('\n')
            self.text_surfs = []
            self.text_rects = []
            self.total_height = 0
            
            for line in self.lines:
                surf = self.font.render(line, True, self.text_col)
                rect = surf.get_rect()
                self.text_surfs.append(surf)
                self.text_rects.append(rect)
                self.total_height += rect.height + self.line_spacing
            self.total_height -= self.line_spacing

            if self.img is not None:
                self.text_center = (self.rect.centerx, self.rect.bottom - self.padding_y - self.total_height // 2)
            else:
                self.text_center = self.rect.centerx, self.rect.centery
            self.start_y = self.text_center[1] - self.total_height // 2

            for rect in self.text_rects:
                rect.centerx = self.text_center[0]
                rect.y = self.start_y
                self.start_y += rect.height + self.line_spacing