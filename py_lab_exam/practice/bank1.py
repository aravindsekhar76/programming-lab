class Bank:
    def __init__(self,accno,accname,acctype,accbal):
        self.accno=accno
        self.accname=accname
        self.acctype=acctype
        self.accbal=accbal

    def deposit(self,x):
        self.bal=self.bal+x
        print(self.bal)
    
    def withdraw(self,k):
        if(k>self.bal):
            print("insufficient balance")
        else: 
            self.bal=self.bal-k
        print(self.bal)

    def balance(self):
        print(self.bal)

ob=Bank(accno,name,type,bal)
accno=int(input("enter your acc no: "))
name=input("enter your name: ")
type=input("enter your account type: " )
bal=int(input("eneter your account balance: "))



while(1):
    c=int(input("enter your choice: "))
    if c==1:
        x=int(input("enter the amount to deposit: "))
        ob.deposit(x)
    elif c==2:
        k= int(input("enter the amount to withdrw: "))
        ob.withdraw(k)
    elif c==3:
        ob.balance()

