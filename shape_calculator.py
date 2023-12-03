class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width (self, width):
        self.width = width

    def set_height (self, height):
        self.height = height

    def get_area (self):
        return self.width * self.height

    def get_perimeter (self):
        return (self.width * 2) + (self.height * 2)

    def get_diagonal (self):
        return ((self.width ** 2 + self.height ** 2) ** .5)

    def get_picture (self):
        if (self.width > 50):
            return "Too big for picture."

        if (self.height > 50):
            return "Too big for picture."

        line = '*' * self.width

        lines = [line for _ in range(self.height)]

        picture = '\n'.join(lines)

        return picture + "\n"
    
    def get_amount_inside (self, shape):
        x = self.width // shape.width
        y = self.height // shape.height

        return x * y

    def __str__(self):
        return "Rectangle(width=" + str(self.width) + ", height=" + str(self.height) + ")"



class Square(Rectangle):
    def __init__(self, side):
        self.width = side
        self.height = side

    def set_side(self, side):
        self.width = side
        self.height = side
        
    def __str__(self):
        return "Square(side=" + str(self.width) + ")"