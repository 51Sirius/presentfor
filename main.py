import pygame as pg

blue_color = (161, 234, 251)
white_color = (253, 253, 253)
pink_color = (255, 206, 243)
purple_color = (202, 187, 233)
display_size = (1000, 600)
display = pg.display.set_mode(display_size)
pg.init()
pg.display.set_caption('Present')


def mouse_effects(number: int):
    mouse_x = pg.mouse.get_pos()[0]
    mouse_x = pg.mouse.get_pos()[1]
    number += 1
    if number >= 1000:
        number = 1
    return number


def start():
    number = 1
    show_menu = True
    while show_menu:
        event = pg.event.poll()
        if event.type == pg.QUIT:
            exit()
        display.fill(blue_color)
        number = mouse_effects(number)
        pg.display.update()


start()