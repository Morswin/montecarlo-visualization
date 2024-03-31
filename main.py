import pygame as pg
import random
import math
from color import Color
from point import Point
from state_manager import StateManager


def main():
    pg.init()
    running: bool = True
    clock = pg.time.Clock()
    window_size = (800, 800)
    window = pg.display.set_mode(window_size)
    window.fill((255, 255, 255))
    # 
    state_manager = StateManager()
    points: [Point] = []
    functions = []
    functions.append(lambda point: math.sqrt((point.get_x() - 400)**2 + (point.get_y() - 400)**2) <= 400)  # 400 == half of the screen
    functions.append(lambda point: math.sqrt((point.get_x() - 400)**2 + (point.get_y() - 400)**2) <= 200)
    functions.append(lambda point: -point.get_x() + 600 < point.get_y())
    functions.append(lambda point: -point.get_x() + 1000 > point.get_y())
    while running:
        clock.tick(60)
        window.fill((0, 0, 0))
        for event in pg.event.get():  # Event loop
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    running = False
                if event.key == pg.K_RETURN:
                    state_manager.switch_adding()
            if event.type == pg.QUIT:
                running = False
        # End of event loop
        if state_manager.is_adding_new_points:
            points.append(Point(random.randint(0, window_size[0]), random.randint(0, window_size[1]), Color(63, 63, 63)))
        for point in points:
            if functions[0](point):
                point.color += Color(255, 255, 255)
            if functions[1](point):
                point.color += Color(127, 127, 127)
            if functions[2](point):
                point.color -= Color(0, 255, 0)
            if functions[3](point):
                point.color -= Color(0, 0, 255)
            pg.draw.circle(window, point.get_color(), point.get(), 5)
        pg.display.flip()
    pg.quit()


if __name__ == "__main__":
    main()
