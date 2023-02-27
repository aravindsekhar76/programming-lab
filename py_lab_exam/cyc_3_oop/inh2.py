class publisher:
    def __init__(self):
        self.publisher=input("enter the name of publisher:")
    def display(self):
        print("\n name of publisher is",self.publisher)

class book(publisher):
    def __init__(self):
        super().__init__()
        self.title=input("enter the title:")
        self.author=input("enter the name of author:")
    def display(self):
        super().display()
        print("\n the title is:",self.title)
        print("\n the name of author is",self.author)


class python(book):
    def __init__(self):
        super().__init__()
        self.price=int(input("enter the price:"))
        self.pgno=int(input("enter the no of pages:"))
    def display(self):
        super().display()
        print("the page no of book is",self.pgno)
        print("the price of book is",self.price)

b1=python()
b1.display()