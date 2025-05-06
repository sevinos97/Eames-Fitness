import pygame as pg
import sys
pg.init()
#objs
import data
import random
from data import settings as stg
from button import Button
from text_box import TextBox
from text import Text
from image import Image
from panel import Panel

WIDTH = stg['resolution'][0]
HEIGHT = stg['resolution'][1]
FRAMES_PER_SECOND = stg['frames_per_second']
scroll = 0
SCROLL_MIN, SCROLL_MAX = -1000, 0

# local user stats
TOTAL_CALORIES = sum([val.calories for val in data.days.values()])
TOTAL_MINUTES = sum([val.minutes for val in data.days.values()])
AVG_MINUTES = TOTAL_MINUTES/7
CURRENT_DAY_VIEW = None
CURRENT_WORKOUT_PANEL = None

# OBJs
images = {
    'title': Image('title', 'Images\Title.png', (WIDTH // 2, 100), 0.5)
}
data_buttons = {
    'edit1': Button('edit1', (WIDTH / 2 - 200, 820), width=50, height=25, text='Edit', text_col=pg.Color(0,123,50), hover_col=(0,123,123), font_size=24, col=pg.Color(210,210,210), active=False, visible=False),
    'edit2': Button('edit2', (WIDTH / 2 - 230, 870), width=50, height=25, text='Edit', text_col=pg.Color(0,123,50), hover_col=(0,123,123), font_size=24, col=pg.Color(210,210,210), active=False, visible=False),
    'edit3': Button('edit3', (WIDTH / 2 - 220, 915), width=50, height=25, text='Edit', text_col=pg.Color(0,123,50), hover_col=(0,123,123), font_size=24, col=pg.Color(210,210,210), active=False, visible=False)
}  
buttons = {'random_workout': Button('random_workout_button', (WIDTH/2, 700), width=400, height=50, text='Give me a random workout!', col=pg.Color(255,255,255), text_col=pg.Color(0, 0, 0), hover_col=pg.Color(210,210,210))}
buttons.update(data_buttons)
data_text_boxes = {
    'tbox1': TextBox('tbox1', (WIDTH/2, 820), WIDTH-10, 50, pg.Color(255,255,255), pg.Color(0,0,0), on=False,visible=False,clicksable=True),
    'tbox2': TextBox('tbox2', (WIDTH/2, 870), WIDTH-10, 50, pg.Color(255,255,255), pg.Color(0,0,0), on=False,visible=False,clicksable=True),
    'tbox3': TextBox('tbox3', (WIDTH/2, 915), WIDTH-10, 50, pg.Color(255,255,255), pg.Color(0,0,0), on=False,visible=False,clicksable=True),    
}
text_boxes = {}
text_boxes.update(data_text_boxes)
texts = {
    'Text1': Text('Text1', (150, 275.55), stg['text_font'], 23, stg['subtitle_text_color'], 'Welcome back, Leon.', AA=True),  
    'WeeklyStats': Text('WeeklyStats', (WIDTH / 2, 325), stg['text_font'], 32, pg.Color(144,155,123), 'Your Week', AA=True),
    'Text2': Text('Text2', (100, 559), stg['text_font'], 18, pg.Color(255,255,0), 'Click to view', AA=True),
    'prompt': Text('prompt', (WIDTH/2, 1200), stg['text_font'], 18, pg.Color(255,255 ,255), 'What is your name and address?', AA=True)
}
panels = {
    'calorie_panel_1': Panel('calorie_panel_1', (100, 450), border_radius=20, img_name='Images\Calorie.webp', text=f'Calories: {TOTAL_CALORIES}', text_col=pg.Color(14,144,14), font_size=27),
    'minute_panel_1': Panel('minute_panel_1', (292.2, 450), border_radius=20, img_name='Images\clock.png', text=f'Minutes: {TOTAL_MINUTES}', text_col=pg.Color(14,144,14), font_size=27),
    'avg_minute_panel_1': Panel('avg_minute_panel_1', (484.4, 450), border_radius=20, img_name='Images\clock.png', text=f'Average Time: {AVG_MINUTES} min', text_col=pg.Color(14,144,14), font_size=15),
    'day_display': Panel('day_display', (WIDTH / 2, 845), width=WIDTH-60, height=400, border_radius=45, text=f'{CURRENT_DAY_VIEW}\nTotal Calories Burnt: {data.days[CURRENT_DAY_VIEW].calories}\nTotal Minutes Worked Out: {data.days[CURRENT_DAY_VIEW].minutes}\nExercises Done: {data.days[CURRENT_DAY_VIEW].exercises}', font_size=40, visible=False)
}
workout_panels = {
    'push_up_panel': Panel('push_up_panel', (WIDTH/2, 890), width=300, height=300, border_radius = 30, font_size=26, img_name='Images\push-up.jpg', text=f'PUSH UP:\n1. Place hands on ground\n2. Bend arms 1/2pi radians.\n3. Fully extend back up.', visible=False),
    'pull_up_panel': Panel('pull_up_panel', (WIDTH/2, 890), width=300, height=300, border_radius = 30, font_size=26, img_name='Images\pull-up.webp', text=f'PULL UP:\n1. Get bar.\n2. Grab bar. \n3. Pull up and down.', visible=False),
    'sit_up_panel': Panel('sit_up_panel', (WIDTH/2, 890), width=300, height=300, border_radius = 30, font_size=26, img_name='Images\sit-upjpeg.jpeg', text=f'SIT UP:\n1. Lay down with legs bent. \n2. Sit up.\n3. Repeat.', visible=False)
}
panels.update(workout_panels)
calendar_panels = {}
panel_width = 83
panel_height = 50
sx = 45
y_pos = 600
days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
days_full_name = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

for i, day in enumerate(days):
    x_pos = sx + i * (panel_width)
    calendar_panels[day] = Button(
        name=days_full_name[i],
        pos=(x_pos,y_pos),
        width=panel_width,
        height=panel_height,
        text=f"{day}",
        text_col=pg.Color(40, 20, 50),
        col=pg.Color(230, 230, 230),
        hover_col=pg.Color(88,99,99)
    )

panels.update(calendar_panels)

ui_elements = {}
ui_elements.update(panels)
ui_elements.update(images)
ui_elements.update(buttons)
ui_elements.update(text_boxes)
ui_elements.update(texts)

def drawAllElements(surf):
    for element in ui_elements.values():
        element.draw(surf)
def scrollElements(scroll):
    for element in ui_elements.values():
        element.scroll(scroll)
def handleAllElements(event):
    for element in ui_elements.values():
        if (ret := element.handleEvent(event)) is not None:
            return ret
    return None
def updateElementPos():
    for element in ui_elements.values():
        element.updatePos()
def updateAllElements():
    for element in ui_elements.values():
        element.update()
def shiftElements(dir, shiftAbove, value, amount, exclude=None):
    for element in ui_elements.values():
        if element not in exclude:
            if shiftAbove == True:
                if element.pos[1] > value and element:
                    if dir.lower() == 'down':
                        element.pos = element.pos[0], element.pos[1] + amount
                    elif dir.lower() == 'up':
                        element.pos = element.pos[0], element.pos[1] - amount
            else:
                if element.pos[1] < value and element:
                    if dir.lower() == 'down':
                        element.pos = element.pos[0], element.pos[1] + amount
                    elif dir.lower() == 'up':
                        element.pos = element.pos[0], element.pos[1] - amount
        
        element.updatePos()

if __name__ == '__main__':
    running = True
    clock = pg.time.Clock()
    
    DISPLAYSURF = pg.display.set_mode((WIDTH, HEIGHT))
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.MOUSEWHEEL:
                dy = event.y * stg['scroll_sensitivity']
                new_scroll = scroll + dy
                clamped = max(SCROLL_MIN, min(SCROLL_MAX, new_scroll))
                dy = clamped - scroll
                scroll = clamped
                scrollElements(dy)
                updateElementPos()

            ret = handleAllElements(event)
            if isinstance(ret, Button):
                print(f"{ret.name} pressed")
                if ret.name in days_full_name:
                    if ret.name != CURRENT_DAY_VIEW:
                        CURRENT_DAY_VIEW = ret.name
                        panels['day_display'].visible = True
                        for button in data_buttons.values():
                            button.visible, button.active = True, True
                        shiftElements('down', True, panels['day_display'].pos[1] - 200, 400, exclude=[panels['day_display'], buttons['edit1'], buttons['edit2'], buttons['edit3'], text_boxes['tbox1'], text_boxes['tbox2'], text_boxes['tbox3']])
                    else:
                        CURRENT_DAY_VIEW = None
                        panels['day_display'].visible = False
                        for button in data_buttons.values():
                            button.visible, button.active = False, False
                        shiftElements('up', True, panels['day_display'].pos[1] - 200, 400, exclude=[panels['day_display'], buttons['edit1'], buttons['edit2'], buttons['edit3'], text_boxes['tbox1'], text_boxes['tbox2'], text_boxes['tbox3']])
                    panels['day_display'].text = f'{CURRENT_DAY_VIEW}\nTotal Calories Burnt: {data.days[CURRENT_DAY_VIEW].calories}\nTotal Minutes Worked Out: {data.days[CURRENT_DAY_VIEW].minutes}\nExercises Done: {data.days[CURRENT_DAY_VIEW].exercises}'
                    panels['day_display'].updateText()

                elif ret.name == 'edit1':
                    text_boxes['tbox1'].enable()
                    text_boxes['tbox1'].active=True
                elif ret.name == 'edit2':
                    text_boxes['tbox2'].enable()
                    text_boxes['tbox2'].active=True
                elif ret.name == 'edit3':
                    text_boxes['tbox3'].enable()
                    text_boxes['tbox3'].active=True

                elif ret.name == 'random_workout_button':
                    if CURRENT_WORKOUT_PANEL is not None:
                        CURRENT_WORKOUT_PANEL.visible = False
                    while True:
                        res = random.choice(list(workout_panels.values()))
                        if res != CURRENT_WORKOUT_PANEL:
                            break
                    CURRENT_WORKOUT_PANEL = res
                    CURRENT_WORKOUT_PANEL.visible = True

            elif isinstance(ret, tuple):
                if CURRENT_DAY_VIEW is not None:             
                    if ret[0] == 'tbox1':
                        if ret[1].isdigit():
                            data.days[CURRENT_DAY_VIEW].calories = int(ret[1])
                            TOTAL_CALORIES = sum([val.calories for val in data.days.values()])
                            panels['calorie_panel_1'].text = f'Calories: {TOTAL_CALORIES}'
                            panels['calorie_panel_1'].updateText()
                    elif ret[0] == 'tbox2':
                        if ret[1].isdigit():
                            data.days[CURRENT_DAY_VIEW].minutes = int(ret[1])
                            TOTAL_MINUTES = sum([val.minutes for val in data.days.values()])
                            AVG_MINUTES = TOTAL_MINUTES/7
                            panels['minute_panel_1'].text = f'Minutes: {TOTAL_MINUTES}'
                            panels['avg_minute_panel_1'].text = f'Average Time: {AVG_MINUTES} min'
                            panels['minute_panel_1'].updateText()
                            panels['avg_minute_panel_1'].updateText()
                    elif ret[0] == 'tbox3':
                        if ret[1] in data.days[CURRENT_DAY_VIEW].exercises:
                            data.days[CURRENT_DAY_VIEW].exercises.remove(ret[1])
                        else:
                            data.days[CURRENT_DAY_VIEW].exercises.append(ret[1])
                panels['day_display'].text = f'{CURRENT_DAY_VIEW}\nTotal Calories Burnt: {data.days[CURRENT_DAY_VIEW].calories}\nTotal Minutes Worked Out: {data.days[CURRENT_DAY_VIEW].minutes}\nExercises Done: {data.days[CURRENT_DAY_VIEW].exercises}'
                panels['day_display'].updateText()

        DISPLAYSURF.fill(stg['app_background_color'])
        drawAllElements(DISPLAYSURF)
        updateAllElements()

        pg.display.update()
        clock.tick(FRAMES_PER_SECOND)
        
    pg.quit()
    sys.exit()