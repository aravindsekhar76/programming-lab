class bank:
    def __init__(self,acc_no,acc_name,acc_type,acc_bal):
        self.number=acc_no
        self.name=acc_name
        self.type=acc_type
        self.bal=acc_bal
    def withdraw(self,x):
        if(x>self.bal):
            print("insufficent")
        else:
            self.bal=self.bal-x
            print(self.bal)
    def deposit(self,y):
        self.bal= self.bal+y
        print(self.bal)

    def balance(self):
        print(self.bal)


no=int(input("account no:"))
name=input("NAme:")
type=input("type of account:")
bal=int(input("Enter balance:"))
ob=bank(no,name,type,bal)
while(1):
    print("1.deposit\n2.withdraw\n3.balance\n")
    c=int(input("Enter choice"))
    if c==1:
        y=int(input("enter the amount to deposit: "))
        ob.deposit(y)
    elif c==2:
        x=int(input("Enter amt to withdraw: "))
        ob.withdraw(x)
    elif c==3:
        ob.balance()
    else:break


    




