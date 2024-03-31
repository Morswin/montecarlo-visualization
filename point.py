from color import Color


class Point:
    x: int
    y: int
    color: Color

    def __init__(self, x, y, color=Color()):
        self.x = x
        self.y = y
        self.color = color

    def get(self) -> (int, int):
        return (self.x, self.y)

    def get_x(self) -> int:
        return self.x

    def get_y(self) -> int:
        return self.y
    
    def get_color(self) -> (int, int, int):
        return self.color.get()

