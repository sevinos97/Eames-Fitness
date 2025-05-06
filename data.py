import pygame as pg
pg.init()
# settings for app
settings = {
    'resolution': (585, 1266), # IPhone 12 resolution halved
    'frames_per_second': 60,
    'app_background_color': pg.Color(33, 33, 33),
    'button_fill_color': pg.Color(255, 255, 255),
    'button_hover_color': pg.Color(195, 195, 195),
    'scroll_sensitivity': 45,   
    'input_text_color': pg.Color(0, 0, 0),
    'text_font': 'freesansbold.ttf',
    'title_text_color': pg.Color(18, 255, 177),
    'subtitle_text_color': pg.Color(113, 215, 76)

}

class Day:
    def __init__(self):
        self.exercises = []
        self.minutes = 0
        self.calories = 0

days = {
    None: Day(),
    'Monday': Day(),
    'Tuesday': Day(),
    'Wednesday': Day(),
    'Thursday': Day(),
    'Friday': Day(),
    'Saturday': Day(),
    'Sunday': Day(),
}