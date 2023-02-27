class rect:
    def __init__(self,l,b):
        self.__l=l
        self.__b=b
        self.ar=0
    def area(self):
        ar=self.__l*self.__b
        
    def __gt__(self,other):
        if self.ar > other.ar:
            print("First one is greater")
        else:
            print("Second one is greater")
        

r1=rect(2,4)
r2=rect(3,5)
r1>r2
 