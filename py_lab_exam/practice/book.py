class Publisher:
    def __init__(self, publisher_name):
        self.publisher_name = publisher_name

obj1 = Publisher('penguin')

class Book(Publisher):
    def __init__(self, publisher_name, title, author):
        super().__init__(publisher_name)
        self.title = title
        self.author = author
    def display(self):
        print("Ithoru book aanu")

class Python(Book):
    def __init__(self, publisher_name, title, author, no_pages, price):
        super().__init__(publisher_name, title, author)
        self.no_pages = no_pages
        self.price = price
    def display(self):
        print("Ithoru Python book aanu")

oru_book = Python("Oreally", "Learning_Python", "Mark Lutz", 2000, 800)
oru_book.display()

class Quadrilateral:
    def area(self, length, breadth):
        print(length*breadth)

    def area(self, length):
        print(length*length)

a = Quadrilateral()
a.area(5)