class Color:
    red: int
    green: int
    blue: int

    def __init__(self, r=0, g=0, b=0):
        self.red = r
        self.green = g
        self.blue = b

    def __add__(self, other):
        if isinstance(other, Color):
            self.red += other.red
            self.green += other.green
            self.blue += other.blue
            return self
        else:
            raise TypeError("You cannot add to color, comething that isn't another color")

    def __sub__(self, other):
        if isinstance(other, Color):
            self.red -= other.red
            self.green -= other.green
            self.blue -= other.blue
            return self
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

