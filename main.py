import pygame as pg


class Point:
    x: int
    y: int

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def get(self) -> (int, int):
        return (self.x, self.y)

    def get_x(self) -> int:
        return self.x

    def get_y(self) -> int:
        return self.y


def main():
    pg.init()
    running: bool = True
    clock = pg.time.Clock()
    window_size = (800, 800)
    window = pg.display.set_mode(window_size)
    window.fill((255, 255, 255))
    # 
    points: [Point] = [
        Point(100, 100),
        Point(200, 200),
        Point(300, 300)
    ]
    while running:
        clock.tick(60)
        window.fill((0, 0, 0))
        for event in pg.event.get():  # Event loop
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    running = False
            if event.type == pg.QUIT:
                running = False
        # End of event loop
        for point in points:
            pg.draw.circle(window, (127, 127, 127), point.get(), 5)
        pg.display.flip()
    pg.quit()


if __name__ == "__main__":
    main()
