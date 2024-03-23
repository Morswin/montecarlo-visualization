import pygame as pg


def main():
    pg.init()
    running = True
    clock = pg.time.Clock()
    window = pg.display.set_mode((800, 800))
    window.fill((255, 255, 255))
    while running:
        clock.tick(60)
        window.fill((0, 0, 0))
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    running = False
            if event.type == pg.QUIT:
                running = False
        pg.display.flip()
    pg.quit()


if __name__ == "__main__":
    main()
