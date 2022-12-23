class rectangle:
    def __init__(self,a,b):
        self.l=a
        self.b=b

    def area(self):
        return (self.l * self.b)

    def perimeter(self):
        return 2*(self.l+self.b)


n1 =int(input("enter the length of first rectangle :"))
n2 =int(input("enter the breadth of first rectangle :"))

b1 = rectangle(n1,n2)

n1 =int(input("enter the length of second rectangle :"))
n2 =int(input("enter the breadth of second rectangle :"))
b2 = rectangle(n1,n2)

a1 = b1.area()
a2 = b2.area()

if a1 > a2:
        print("area of first reactangle is greater=",a1)
else:
        print("area of the second rectangle is greater=",a2)

