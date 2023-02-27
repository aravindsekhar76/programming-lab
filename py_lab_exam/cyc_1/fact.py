
def fact(a):
        f=1
        for i in range(1,a+1):
                f*=i
        return f
a=int(input("enter a number:"))

x=fact(a)
print("factorial is",x)