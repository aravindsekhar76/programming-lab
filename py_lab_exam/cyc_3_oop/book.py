class publisher:
    def __init__(self):
        self.publisher=input("Enter name of the Publisher\n")
    def display(self):
            print("publisher is ",self.publisher)

class book(publisher):
    def __init__(self):
        super().__init__()
        self.author=input("Enter name of the author\n")
        self.title=input("Enter title of the book\n")
    def display(self):
        super().display()
        print("author is ",self.author," and title is ",self.title)

class python(book):
    def __init__(self):
        super().__init__()
        self.price=int(input("ENter the price of the book\n"))
        self.pages=int(input("ENter the no of pages\n"))
    def display(self):
        super().display()
        print("Price of the book is ",self.price,"and no. of the pages is ",self.pages)


book1=python()
book1.display()