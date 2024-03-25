import pygame as pg
import random
import math


class ProgramState:
    is_adding_new_points: bool

    def __init__(self):
        self.is_adding_new_points = False

    def switch_adding(self) -> None:
        self.is_adding_new_points = not self.is_adding_new_points


class Color:
    red: int
    green: int
    blue: int

    def __init__(self, r, g, b):
        self.red = r
        self.green = g
        self.blue = b

    def __add__(self, other) -> None:
        if isinstance(other, Color):
            self.red += other.red
            self.green += other.green
            self.blue += other.blue
        else:
            raise TypeError("You cannot add to color, comething that isn't another color")

    def __sub__(self, other) -> None:
        if isistance(other, Color):
            self.red -= other.red
            self.green -= other.green
            self.blue -= other.blue
        else:
            raise TypeError("You cannot substract from color, comething that isn't another color")

    def get(self) -> (int, int, int):
        red = self.red
        if red > 255:
            red = 255
        elif red < 0:
            red = 0
        green = self.green
        if green > 255:
            green = 255
        elif green < 0:
            green = 0
        blue = self.blue
        if blue > 255:
            blue = 255
        elif blue < 0:
            blue = 0
        return (red, green, blue)


class Point:
    x: int
    y: int
    color: Color

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = Color(0, 0, 0)

    def get(self) -> (int, int):
        return (self.x, self.y)

    def get_x(self) -> int:
        return self.x

    def get_y(self) -> int:
        return self.y
    
    def get_color(self) -> (int, int, int):
        return self.color.get()


def main():
    pg.init()
    running: bool = True
    clock = pg.time.Clock()
    window_size = (800, 800)
    window = pg.display.set_mode(window_size)
    window.fill((255, 255, 255))
    # 
    program_state = ProgramState()
    points: [Point] = []
    functions = [
        lambda point: math.sqrt((point.get_x() - 400)**2 + (point.get_y() - 400)**2) <= 400  # 400 == half of the screen
    ]
    while running:
        clock.tick(60)
        window.fill((0, 0, 0))
        for event in pg.event.get():  # Event loop
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    running = False
                if event.key == pg.K_RETURN:
                    program_state.switch_adding()
            if event.type == pg.QUIT:
                running = False
        # End of event loop
        if program_state.is_adding_new_points:
            points.append(Point(random.randint(0, window_size[0]), random.randint(0, window_size[1])))
        for point in points:
            if functions[0](point):
                pg.draw.circle(window, (255, 255, 255), point.get(), 5)
            else:
                pg.draw.circle(window, (127, 127, 127), point.get(), 5)
        pg.display.flip()
    pg.quit()


if __name__ == "__main__":
    main()
