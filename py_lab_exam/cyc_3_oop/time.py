class time:
    def __init__(self,h,m,s):
        self.__h=h
        self.__m=m
        self.__s=s
    
    def __add__(self,other):
        self.__h=self.__h+other.__h
        self.__m=self.__m+other.__m
        self.__s=self.__s+other.__s
        if(self.__m>=60):
            self.__h=self.__h+1
            self.__m=self.__m-60
        if(self.__s>=60):
            self.__m=self.__m+1
            self.__s=self.__s-60
        print("\n",self.__h," hours\n",self.__m," minutes\n",self.__s," seconds\n")
        
    
    
t1=time(1,31,6)
t2=time(1,30,1)
t3=t1+t2