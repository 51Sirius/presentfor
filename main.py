import pygame as pg

blue_color = (161, 234, 251)
white_color = (253, 253, 253)
pink_color = (255, 206, 243)
purple_color = (202, 187, 233)
display_size = (1000, 600)
display = pg.display.set_mode(display_size)
pg.init()
pg.display.set_caption('Present')


class Effect_mouse:
    def __init__(self):
        self.width = 1
        self.color = white_color

    def circle_draw(self, x, y):
        pg.draw.circle(display, self.color, (x, y), self.width)

    def mouse(self):
        mouse_x = pg.mouse.get_pos()[0]
        mouse_y = pg.mouse.get_pos()[1]
        self.circle_draw(mouse_x, mouse_y)


def start():
    effects_m = Effect_mouse()
    number = 1
    show_menu = True
    while show_menu:
        event = pg.event.poll()
        if event.type == pg.QUIT:
            exit()
        display.fill(blue_color)
        effects_m.mouse()
        pg.display.update()


start()
