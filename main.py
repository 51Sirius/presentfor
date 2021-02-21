import pygame as pg
import random as rand

blue_color = (161, 234, 251)
white_color = (253, 253, 253)
pink_color = (255, 206, 243)
purple_color = (202, 187, 233)
display_size = (1000, 600)
display = pg.display.set_mode(display_size)
pg.init()
clock = pg.time.Clock()
pg.display.set_caption('Present')


class Effect_mouse:
    def __init__(self):
        self.new = True
        self.width = 8
        self.color = purple_color
        self.amount = 0
        self.points_list = []
        self.timer = 0

    def circle_draw(self, x, y):
        pg.draw.circle(display, self.color, (x, y), self.width)

    def mouse(self):
        self.timer += 1
        if self.timer >= 30:
            self.new = True
        if self.timer < 10:
            self.width = 6
        elif self.timer >= 10 and (self.timer < 20):
            self.width = 4
        else:
            self.width = 2
        mouse_x = pg.mouse.get_pos()[0]
        mouse_y = pg.mouse.get_pos()[1]
        if self.new:
            self.amount = rand.randint(4, 10)
            self.new = False
            self.timer = 0
            self.points_list = []
            for j in range(self.amount):
                r = rand.randint(1, 4)
                self.points_list.append([0, 0, r])
        for i in range(len(self.points_list)):
            self.points_list[i][0] += rand.randint(1, 3)
            self.points_list[i][1] += rand.randint(1, 3)
            if self.points_list[i][2] == 1:
                self.circle_draw(mouse_x + self.points_list[i][0], mouse_y + self.points_list[i][1])
            elif self.points_list[i][2] == 2:
                self.circle_draw(mouse_x - self.points_list[i][0], mouse_y + self.points_list[i][1])
            elif self.points_list[i][2] == 3:
                self.circle_draw(mouse_x - self.points_list[i][0], mouse_y - self.points_list[i][1])
            elif self.points_list[i][2] == 4:
                self.circle_draw(mouse_x + self.points_list[i][0], mouse_y - self.points_list[i][1])


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
        clock.tick(80)


start()
