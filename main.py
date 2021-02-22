import pygame as pg
import random as rand

blue_color = (146, 204, 242)
white_color = (254, 206, 253)
pink_color = (255, 206, 243)
purple_color = (164, 124, 233)
display_size = (1000, 600)
display = pg.display.set_mode(display_size)
pg.init()
clock = pg.time.Clock()
pg.display.set_caption('Present')


def draw_right_flower(middle_color=(255, 255, 0), flower_color=(255, 0, 0)):
    print(middle_color, flower_color)
    color_stem = (0, 255, 0)
    width_flower = 30
    length_flower = 80
    stem = pg.draw.line(display, color_stem, [900, 600], [900, 260], 10)
    first_flower = pg.draw.ellipse(display, flower_color, (885, 180, width_flower, length_flower))
    second_flower = pg.draw.ellipse(display, flower_color, (780, 285, length_flower, width_flower))
    third_flower = pg.draw.ellipse(display, flower_color, (940, 285, length_flower, width_flower))
    middle_circle = pg.draw.circle(display, middle_color, (900, 300), 50)


def change_color(max_color, color: tuple):
    color = list(color)
    if color[0] <= 255 and color[1] == max_color and color[0] != max_color:
        if color[2] < 255:
            color[2] += 1
        elif color[0] != max_color:
            color[0] -= 1
        else:
            color[0] = max_color
    elif color[2] <= 255 and color[0] == max_color and color[2] != max_color:
        if color[1] < 255:
            color[1] += 1
        elif color[2] != max_color:
            color[2] -= 1
        else:
            color[2] = max_color
    elif color[1] <= 255 and color[2] == max_color and color[1] != max_color:
        if color[0] < 255:
            color[0] += 1
        elif color[1] != max_color:
            color[1] -= 1
        else:
            color[1] = 0
    return tuple(color)


class Font:
    def __init__(self, x, y, font_color=tuple(pink_color), font_size=30, font_type='20216.ttf',
                 message=None):
        self.x = x
        self.y = y
        self.font_color = font_color
        self.font_type = font_type
        self.font_size = font_size
        self.message = message

    def draw_text(self, ms=None):
        font_type = pg.font.Font(self.font_type, self.font_size)
        text = font_type.render(self.message, True, self.font_color)
        display.blit(text, (self.x, self.y))


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
    color_first = (255, 110, 102)
    second_color = (255, 246, 102)
    font = Font(100, 200, font_size=60, message='Entry your present')
    effects_m = Effect_mouse()
    number = 1
    show_menu = True
    while show_menu:
        event = pg.event.poll()
        if event.type == pg.QUIT:
            exit()
        display.fill(blue_color)
        effects_m.mouse()
        font.draw_text()
        color_first = change_color(102, color_first)
        second_color = change_color(102, second_color)
        draw_right_flower(second_color, color_first)
        font.font_color = change_color(206, font.font_color)
        pg.display.update()
        clock.tick(80)


start()
