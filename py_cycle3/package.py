from graphics import rectangle,circle
from graphics.graphics3d import cuboid
from graphics.graphics3d.sphere import area as sphere_area

radius= int(input("enter the radius of the circle:"))
print("area of circle:",circle.area(radius))

length=int(input("enter the length of the reactangle:"))
breadth=int(input("enter the breadth of the rectangle:"))
print("area of the rectangle:",rectangle.area(length,breadth))

radius= int(input("enter the radius of the sphere:"))
print("area of the sphere:",sphere_area(radius))

l=int(input("enter the lenghth of the cuboid:"))
w=int(input("enter the width of the cuboid:"))
h=int(input("enter the height of the cuboid:"))
print("area of the cuboid", cuboid.area(l,w,h))

