class rectangle:
    def __init__(self,len,bre):
        self.l=len
        self.b=bre

    def peri (self):
        perimeter= 2*(self.l+self.b) 
        return(perimeter)
    def area(self):
        area=(self.l*self.b)
        return(area)
p = int(input("enter the length of rect 1:"))
q= int(input("enter the breadth of rect1:"))
rect1= rectangle(p,q)
r = int(input("enter the length of rect 2:"))
s= int(input("enter the breadth of rect 2:"))
rect2= rectangle(r,s)

x=rect1.peri()
y=rect2.peri()
if(x>y):

    print(" perimeter of rectangle 1 is larger",x)

else:

    print("perimeter of rectangle 2 is larger",y)

a= rect1.area()
b= rect2.area()

if(a>b):
    print("area of rect1 is larger",a)

else:
    print("area of rect 2 is larger",b)   


