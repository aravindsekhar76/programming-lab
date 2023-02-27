class Bank:
    def __init__(self,accno,name,acctype,accbal):
        self.num=accno
        self.n=name
        self.type=acctype
        self.bal=accbal
    def deposit(self,amt):
        self.bal=self.bal+amt
    def withdraw(self,amt):
        if self.bal<amt:
            print("insufficient balance")

        else:
            self.bal= self.bal-amt 
        print("Amount is withdrawed is :",amt)
    def balance(self):
        print("balance=",self.bal)
print("***\t WELCOME TO  ARAVIND BANK \t***")
accno =int(input("Enter your account number: "))
name = input("Enter your name: ")
acctype =input("Enter the type of your account (savings or current) : ")
accbal =float(input("enter your account balance: "))
obj1=Bank(accno,name,acctype,accbal)
print("ypur account balance is: ",obj1.bal)
while(1):
    x=int(input("\n 1.deposit \n 2.withdraw \n 3.show balance\n 4.exit"))
    if x==1:
        amt=int(input("enter the amount to deposit"))
        obj1.deposit(amt)
        print("amount deposited sucessfully")
    elif x==2:
        amt=int(input("enter the amount to withdraw"))
        obj1.withdraw(amt)
    elif x==3:
        obj1.balance()
    elif x==4:
        break
    else:
        print("invalid option")

