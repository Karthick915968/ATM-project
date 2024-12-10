class Bank:
    def __init__(self):
        self.closingbal=0
        
    def display(self):
        print("Enter your options: ")
        print ("1 for deposit: \n2 for withdraw: ")
        getoption= input()
        if getoption=="1":
            self.deposit()
        elif getoption=="2":
            self.withdraw()
        elif getOption!=1 or getoption!=2:
            print("thanks")
            return
        print("your closing balance:", self.closingbal)
        print("do you want to continue:")
        a=input()
        if a =="Y" or a=="y":
            self.display()
        else:
            print("thanks for visiting our bank")
            
    def deposit(self):
        depositAmount=int(input("enter your deposit amount:"))
        self.closingbal=self.closingbal+depositAmount
        return self.closingbal

    def withdraw(self):
        withdrawAmount=int(input("enter your withdraw amount;"))
        if self.closingbal>=withdrawAmount:
            self.closingbal=self.closingbal-withdrawAmount
            print("after withdraw your balance amount is:",self.closingbal)
        else:
            print("no sufficient  balance")
        return self.closingbal

bankObj=Bank()
bankObj.display()














    
        
