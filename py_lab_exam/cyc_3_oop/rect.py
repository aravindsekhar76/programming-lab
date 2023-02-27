class rectangle:
    def __init__(self,lenghth,breadth) :
        self.l= lenghth
        self.b= breadth
    def area(self):
        return self.l*self.b
    def perimeter(self):
        return 2*(self.l+self.b)
    
p=int(input("enter the length of rectangle1 : "))
q= int(input("enter the beadth of rectangle 1: "))
rect1=rectangle(p,q)

r=int(input("enter the length of rectangle 2 : "))
s= int(input("enter the beadth of rectangle 1: "))
rect2=rectangle(r,s)

m=rect1.area()
n=rect2.area()

e= rect1.perimeter()
f= rect2.perimeter()
if m > n:
    
    print("the first rectangle has the biggest area",m)
else:
    print("the second rectangle has the biggest area",n)
if e > f:
    print("the first rectangle has the biggest perimeter",e)
else:
    print("the second rectangle has the biggest perimeter",f)

