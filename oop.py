# class dog:          #simple class
#     name="buddy"
#     color="black"
#     tale="Small"
#     eyes="brown"
# dog1=dog()           #simple object
# print(dog1)
# print(dog1.name,dog1.color,dog1.tale,dog1.eyes)   #print values of object
# dog2=dog()        #object2
# print(dog2.color)     #print value of object2


# class dog:
#     def __init__(self,name,color,tale,age):
#         self.name=name
#         self.color=color
#         self.tale=tale
#         self.age=age
#         print("Your dog is Created")
# dog1=dog("buddy","black","brown","20")
# print("Dog name is",dog1.name,"Dog color is",dog1.color,"Dog tale is",dog1.tale,"Dog age is",dog1.age)


# class student:
#     def __init__(self,name,rollno,marks):
#         self.name=name
#         self.rollno=rollno
#         self.marks=marks
#         print("Your Student info is created")

# s=student("Ali",1122,90)
# print("Wellcome",s.name,"your rollno is",s.rollno,"your marks is",s.marks)




class ATM:
    def __init__(self,user_cash):
    
        self.user_cash=user_cash

    def check_balance(self):
        print("Your current balance is",self.user_cash)

            
    def deposit(self):
        amount=int(input("Enter the deposite amount:"))
        self.user_cash=self.user_cash+amount
        print("Deposite Successfully")
    def withdrawl(self):
        amount=int(input("Enter your ammount:"))
        if(amount<=self.user_cash):
            self.user_cash=self.user_cash-amount
            print("Withdrawl Successfully")
        else:
            print("Insufficient Balance")
bank=ATM(50000)
bank.check_balance()
bank.deposit()
bank.withdrawl()










