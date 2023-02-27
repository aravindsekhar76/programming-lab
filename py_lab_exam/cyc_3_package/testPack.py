from graphics import circle
from graphics import rectangle

from graphics.threeD_graphics import sphere
from graphics.threeD_graphics import cuboid

#import cuboid
#import sphere


r=int(input("Enter Radius of Circle : "))
circle.cArea(r)
circle.cPerim(r)

l=int(input("Enter Length of Rectangle : ")) 
b=int(input("Enter Breadth of Rectangle : "))
rectangle.rArea(l,b)
rectangle.rPerim(l,b)

p=int(input("Enter Length of Cuboid : "))
q=int(input("Enter Breadth of Cuboid : "))
r=int(input("Enter Height of Cuboid : "))
cuboid.cubArea(p,q,r)
cuboid.cubPerim(p,q,r)

x=int(input("Enter Radius of Sphere : "))
sphere.sArea(x)
sphere.sPerim(x)








