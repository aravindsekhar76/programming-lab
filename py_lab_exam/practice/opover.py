class Rectangle:
    def __init__(self, l, b):
        self.length = l
        self.breadth = b

    def area(self):
        return self.length*self.breadth

    def __gt__(self, other):
        if (self.area() > other.area()):
            return True
        else:
            return False

rect1 = Rectangle(1, 2)
rect2 = Rectangle(2, 3)

rect1 > rect2