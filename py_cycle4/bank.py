class bankAccount:
    def __init__(self,accno,name,acctype,accbal):
        self.no = accno
        self.name = name
        self.type = acctype
        self.bal = accbal

    def deposit(self,amount):
        self.bal += amount 
    def withdraw(self,amount):
        if self.bal < amount:
            print("insufficient balance")
        else: 
            self.bal -= amount
    def balance(self):
            print("account balance=", self.bal)
accno= int(input("enter your account number"))
name= input("enter your name")
acctype= input("enter your account type")
accbal= int(input("enter your account balance"))
obj1 = bankAccount(accno,name,acctype,accbal)
op = 0
while(op!=4):
        print("\n 1.deposit \n 2. withdraw \n 3.balance \n 4. exit")
        op= int(input("Enter your choice :"))
        if op ==1:
            n= int(input("enter the emount to be deposited"))
            obj1.deposit(n)
            print("amount deposited sucessfully")
        elif op==2:
            n= int(input("enter the amount to withdraw"))
            obj1.withdraw(n)
        elif op==3:
            obj1.balance()
        elif op==4:
            print("Exiting...")
            break
        else:
            print("Enter valid choice ")
