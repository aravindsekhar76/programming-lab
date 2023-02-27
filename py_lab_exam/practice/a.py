class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    def perimeter(self):
        print(2*(self.length + self.breadth))

rect1 = Rectangle(4, 5)
rect2 = Rectangle(8, 10)

rect2.perimeter()
rect1.perimeter()