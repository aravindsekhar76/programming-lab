class publisher:
    def __init__(self,):
        self.publish=input("enter publisher name\n")
    def display(self):
        print("publisher name is ", self.publish)

class Book(publisher):
    def __init__(self):
        super().__init__()
        self.title= input("enter the title\n")
        self.authname=input("enter the name of author\n")
    def display(self):
        super().display()
        print("the title is",self.title)
        print("the name of author is",self.authname)
    
class Python(Book):
    def __init__(self):
        super().__init__()
        self.pages=input("enter the Number of pages\n")
        self.price= input("enter the price of the book\n ")
    def display(self):
        super().display()
        print("the number of pages in this book is", self.pages)
        print("the price of the book is", self.price)

obj1= Python()
obj1.display()