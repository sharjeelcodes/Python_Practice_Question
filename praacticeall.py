# print("Hello world")
# name="myself Sharjeel i am  a python developer."
# print(len(name))
# print(name[4])
# print(type(name[8:12]))
# num1=34
# num2=45
# print("num1+num2=",num1+num2)
# name=input("Enter a name")
# if(name=="Sharjeel"):
#     print("This is a valid person ")
# else:
#     print("Invalid person")   


# pin=int(input("Enter a pin:")) 
# amount=int(input("Enter a amount:")) 
# if(pin==7271):
#     if(amount<=5000):
#         print("Withdrawl successful")      
# elif(amount>5000):
#     print("Insufisiant balance")  
# else:
#     print("Invalid withdraw ammount")  



# age=int(input("Enter your age:"))
# if(age<13 and age>0):
#     print("You are child")
# elif(age>=13 and age<19):
#     print("you are a teenger")
# elif(age>=19):
#     print("you are an adult")
# else: 
#     print("invalid age")         
    
    
# name="Sharjeel" 
# password=1234
# username=input("Enter your name:")
# password1=int(input("Enter a password:"))
# if(username==name and password1==password):
#     print("Login Successful!")
# elif(username==name and password1!=password):
#     print("Incorrect password!")
# else:
#     print("User not found!")

                   
          
# balance=5000
# print("1.Check Balance") 
# print("2.Deposite Money") 
# print("3.Withdraw Money")
# choice=int(input("Enter your choice (1-3):"))
# if(choice==1):
#     print("Your balance is",balance)
# elif(choice==2):
#     deposit=int(input("Enter deposite amount:")) 
#     new_balance=balance+deposit 
#     print("Wellcome!your new balance is",new_balance)
# elif(choice==3):
#     withdraw=int(input("Enter a withdraw amount"))
#     if(withdraw<=balance):
#         new_balance=balance-withdraw
#         print("Withdraw Successful!your new balance is",new_balance)
#     else:
#         print("Insufficent balance")
# else:
#     print("Invalid choice")              
          
          
# Balance=100
# print("1.Jazz pakage") 
# print("2.Zong pakage") 
# print("3.Ufone pakage") 
# choose=int(input("Enter the pakage (1-3):"))
# if(choose==1):
#     print("Jazz pakage activated") 
# elif(choose==2):
#     print("Zong pakage activated")
# elif(choose==3):
#     print("Ufone pakage activated") 
# else:
#     print("Invalid choose")                         
# balance=5000
# print("1.check balance")
# print("2.deposite money")
# print("3.withdraw money")
# choice=int(input("Enter your choice:(1-3)"))
# if(choice==1):
#     print("your curentt balance",balance)
# elif(choice==2):
#     deposite=int(input("Enter your money:")) 
#     total=deposite+balance  
#     print("Wellcome!Dear coustermer your current balance is",total) 
# elif(choice==3):
#     withdraw=int(input("Enter your withdraw amount:")) 
#     if(withdraw>balance):
#        print("Sorry!your balaance insificient:Please! try again")  
#     elif(withdraw<=0):        
#        print("Invalid amout!Please try again") 
#     else:
#         amount=balance-withdraw
#     print("your current balance is",amount) 
# else:
#     print("Invalid choice")       
          
# list=["Apple","Mango","Orange","Banana","grapes","Cherry"]
# print(list[0])
# print(list[-1])
# list.append("Strawbbry")
# print(list.remove("Apple"))
# print(list)
# tup=(5,5,8,2,14,9,3,6,15)
# print(tup[1]) 
# print(tup.index (15))
   
# ##MOBILE PAKAGE SYSTEM:   
   
# Balance=1000
# print("1.Jazz pakage") 
# print("2.Zong pakage") 
# print("3.Ufone pakage") 
# choose=int(input("Enter the pakage (1-3):"))
# if(choose==1):
#     number=int(input("Enter your number:"))
#     print("pakage!1.mounth(900),2.1 day(100),3.1 week(500),5 week(5000) ") 
#     select_pakage=int(input("Enter a pakage:"))
#     amount=int(input("Enter a amount:"))
#     if(amount<Balance):
#         print("Congratulations!your pakage will activated")
#     else:
#         print("Insufficient balance!Your pakage will be not activated ")
# elif(choose==2):
#     number=int(input("Enter your number:"))
#     print("pakage!1.mounth(900),2.1 day(100),3.1 week(500),5 week(5000) ") 
#     select_pakage=int(input("Enter a pakage:"))
#     amount=int(input("Enter a amount:"))
#     if(amount<Balance):
#         print("Congratulations!your pakage will activated")
#     else:
#         print("Insufficient balance!Your pakage will be not activated ")
# elif(choose==3):
#     number=int(input("Enter your number:"))
#     print("pakage!1.mounth(900),2.1 day(100),3.1 week(500),5 week(5000) ") 
#     select_pakage=int(input("Enter a pakage:"))
#     amount=int(input("Enter a amount:"))
#     if(amount<Balance):
#         print("Congratulations!your pakage will activated")
#     else:
#         print("Insufficient balance!Your pakage will be not activated ")
# else:
#     print("Invalid choose")



# unit=int(input("Enter your units:"))
# if(unit<=100):
#     print(unit*10)
# elif(unit>=101 and unit<=200):
#     print(unit*15) 
# elif(unit>200):
#     print(unit*20) 
# else:
#     ("Invalid unit")            
    
    
# print("Empoley Bounus System:")
     
# salary=int(input("Enter your salary:"))
# service=int(input("Enter your service year:"))
# if(service<=5):
#     print("SOORY!NO BONOUS")
# elif(service>5 and service<=10):
#     bonous=salary*10/100
#     print(salary+bonous)
# elif(service>10):
#     bonous=salary*20/100
#     print(salary+bonous)    
# else:
#     ("Invalid number")    


# num1=int(input("Enter a number:"))
# operator=input("Enter a operation(+,-,*,/,%):")
# num2=int(input("Enter a number:"))
# if(operator=="+"):
#     print("num1+num2=",num1+num2)
# elif(operator=="-"):
#     print("num1-num2=",num1-num2)
# elif(operator=="*"):
#     print("num1+num2=",num1*num2)
# elif(operator=="/"):
#      print("num1/num2=",num1/num2)
# elif(operator=="%"):
#     print("num1%num2=",num1%num2)   
# else:
#     print("Error")    
    
    
# name=str(input("Enter your name:")) 
# length=len(name)    
# if(length<5):
#     print("Short name")
# elif(length>=5 and length<=8):
#     print("Normal name") 
# elif(length>8):
#     print("Long name") 
# else:
#     print("Invalid item") 
    
    
    
# side1=input("Enter a side one:")    
# side2=input("Enter a side two") 
# side3=input("Enter a side three:")  
# if(side1==side2==side3):
#     print("Equilateral Triangle")
# elif(side1==side2 or side2==side3 or side3==side1):
#     print("Isoscles Triangle")
# else:
#     print("Scalene Triangle")             
    
    
# password=input("Enter a password:")
# if(len(password)==0):
#     print("Invaid input!Please enter something")
# elif(len(password)<8):
#     print("Weak password")

# elif(password.isalpha()):        ##yaa batata hai ky string mein sirf letters hou capital aur small only 
#     print("Moderte password") 
# elif(password.isalnum()):          ##yaa batta hai ky string mein sirf numbers hou 
#     print("Strong password") 
# else:
#     print("Password very strong") 



# username=input("Enter your username:")
# if username[0].isupper() and username[1:].islower():
#     print("Valid username") 
# else:
#     print("Invalid username")
    
    
    
# number=input("Enter a number:")
# if(number.isdigit()):            ## yaa batata hai ky string mein sirf numbers hou 
#     print("Only Numbers!")
# else:
#     print("Invalid input!") 
    
    
    
# password=input("Enter a password:") 
# if(len(password)==8):
#     print("GOOD PASSWORD") 
# else:
#     print("TOO SHORT!")  


# name=input("Enter a name:")
# if(name.isalpha()):
#    print("Nice name!")
# else:
#     print("Name should not contain numbers or symbols!") 


# symbol=input("Enter any charcter:")
# if not symbol.isalnum():
#     print("Symbol detected!")
# else:
#     print("Not a symbol!")



# age=int(input("Enter your age:"))
# budget=int(input("Enter your budget:(Rs)"))
# food=input("Enter your food type:(veg,non-veg,fast-food,desi):")
# time=input("Enter your time:(morning,afternoon,night)") 
# weather=input("Enter your favorite weather:(hot,cold,rainy)")
# if(age<18 and budget<1000 and food=="fast-food" and time==time and weather==weather):
#     print("McDonals,KFC,Pizza Hut:youth favorite quick meals!")
# elif(age==18-25 and budget<800 and food=="Desi" and weather=="Hot" and time=="afternoon"):
#     print("Student Biryani,Biryani Express:Budget desi food!")
# elif(age==20-35 and budget==2000-4000 and food=="Desi" and weather=="cold" and time=="night"):
#     print("BBQ Tonight,Haveli, Monal:perfect for cold weather dinner! ")
# elif(age==25-40 and budget==1500-3000 and food=="Non-veg" and weather=="Raniy" and time=="morning"):
#     print("Butt karahi,Salt'n pepper,Qabail tribes:perfect raniy-day comfort food")
# else:
#     print("see other resturent")         
    
   
# dec={} 
# x=int(input("Enter phy:")) 
# dec.update({"phy":x})          
# x=int(input("Enter Math:"))  
# dec.update({"chm":x})         
# x=int(input("Enter chm:")) 
# dec.update({"math":x})
# print(dec)
   
#LOOPS
#qs1:             
# i=1
# while i<=10:
#     print(i)
#     i +=1         


#qs2:
# x=int(input("Enter your table number:")) 
# i=1
# while i<=10:
#     print(x ,"*",i,"=",i*x)
#     i +=1

     
#qs3:
# i=10
# while i>=1:
#     print(i)
#     i -=1 
         
          
#qs4:
# i=1
# while i<=20:
#     if(i % 2==0):
#         print("The number is even",i)
#     i +=1              


#qs5:
# i=1
# while i<=15:
#     if(i % 2!=0):
#         print("Number is odd",i)
#     i +=1
    
        
#qs6:
# i=1
# while i<=5:
#     print(i*i)
#     i +=1
    
    
#qs7:
# i=1
# while i<=10:
#     print(i+i)
#     i +=1
    
 
#qs8:                 
# nums=(2,4,8,6,5,9,)
# i=len(nums)
# while i==len(nums):
#     print(nums,"\nThe totle numbers of digits",len(nums))
#     i +=1 

     
# #qs9:
# sum=-1
# num=int(input("Enter a number:"))
# while num!=-1:
#     sum+=num
#     num=int(input("Enter a second number:"))
#     print("Sum =",sum) 
        
       
#qs10
marks=[44,56,78,90,23,67,99,55,68,54,22,100,77]
print(marks[0])
student=["Ali","Karan",44,"Sharjeel","Sohaib",56,88,99,"Kashif","Asim",100,"Qasim","Akaml"] 
print(student[5])     #indexing
print(len(student))
print(type(student))
print(marks[2:])     #slicing
print(student[0:8])
print(marks[-5:-2])    
student.append("Sharjeel")   
marks.sort()
print(marks)   
tup=(2,3,5,6,9,1,6,4,2,5,0,2,1)
print(tup[0])     
tup1=(1,)
print(type(tup1))


# movie1=input("Enter a first movie name:")
# movie2=input("Enter a second movie name:")
# movie3=input("Enter a third movie name:")
# list=[]
# list.append(movie1)
# list.append(movie2)
# list.append(movie3)
# print(list)

        
        
# name=input("Enter a name:"),
# print("WELL COME!SHARJEEL")            
        
        
# num1=int(input("Enter a first number:"))
# num2=int(input("Enter a second number:"))
# print(num1+num2)       
          
          
# age=int(input("Enter a age:"))
# age_5_years=age+5
# print(age_5_years)


# temp=float(input("Enter a temprature:"))
# fernhite=(temp*9/5)+32
# print(fernhite,"F")

          
# num=int(input("Enter a number:"))
# if(num%2==0):
#     print(num,"is even")
# else:
#     print(num,"Number is Odd")            
          
          
          
          
# marks=int(input("Enter a marks:"))
# if(marks>=90 and marks<=100):
#     print("Grade is A")
# elif(marks>=75 and marks<=90):
#     print("Grade is B")
# elif(marks>=55 and marks<=75):
#     print("Grade is C")
# else:
#     print("Fail")              
          
      
      
# password=input("Enter a password!")
# if(password=="python1122"):
#     print("Access Successful!")     
# else:
#     print("Access Denaied!")     
          
          
          
# num1=int(input("Enter a first number!"))
# num2=int(input("Enter a second number!"))
# num3=int(input("Enter a third number!"))
# if(num1>=num2 and num1>=num3):
#     print("First number is grater!",num1)
# elif(num2>=num1 and num2>=num3):
#     print("Second number is gerater!",num2)
# else:
#     print("Third number is greater!",num3) 

          
         
# i=1
# while(i<=10):
#     print(i) 
#     i+=1               
         
         
        
         
# i = 1
# while (i <= 20):
#     if( i % 2 ==0):
#         print(i)
#     i+=1         
         

         
# num=int(input("Enter a number:"))
# i=1
# while(i<=10):
#     print(num,"*",i,"=",i*num)
#     i+=1        
         
         
         
# 1 se N tak numbers ka sum calculate karo (N user input hoga).
# n=int(input("Enter a number:"))
# sum=0
# i=1
# while(i<=n):
#     sum=sum+i
#     i+=1
# print("1 sy",n,"tk ka sum =",sum) #agr indentetion dy ky lekhy gy tou har bar print alag print hou ga kion ky woo loop ky undar hou ga          
         
 
         
# i=10
# while(i>=1):
#     print(i)
#     i-=1              
         
         
# num=int(input("Enter a number:"))
# while(num!=0):
#     # print("Please Enter a Number!")
#     num=int(input("Enter a number:")) 
# print("Loop will be endded!")
        
         
          
#1 se 50 tak sirf wo numbers print karo jo 3 se divisible hain.   
# i=1
# while(i<=50):
#     if(i%3==0):
#         print(i," ","These numbers are divisible by 3!")
#     i+=1    
    

# Password system banao — user ko 3 attempts milen.         
# correct_password="python1122"
# attemts=1
# while(attemts<4):
#     password=input("Enter a password:")
#     if (password==correct_password):
#         print("Access granted!")
#         break
#     else:
#         attemts+=1
#         print("Access denied!","Please try again!")
#     if(attemts==4):
#         print("Access denied!","Your attemts have completed!")                  
         
         
         
# n=int(input("Enter a number:"))
# sum=0
# i=1
# while(i<=n):
#     sum=sum+i
#     i+=1
# print("1 sy n tk ka sum =",sum)



# n=int(input("Enter a number:"))
# while(n!=0):
#     print(n)
#     n=int(input("Enter a number:"))
# if(n==0):
#     print("Loop will be ended!")



# i=10
# while(i>=1):
#     print(i)
#     i-=1



# Password system banao — user ko 3 attempts milen.   
# correct_password=1122
# attemts=1
# while(attemts<4):
#     password=int(input("Enter a password:"))
#     if(password==correct_password):
#         print("Access granted!")


#         break
#     else:
#         attemts+=1
#         print("Access denaied!","Please try again!")
# if(attemts==3):
#     print("Access denaied!","your attemts have completed!")        



# 5 numbers user se le kar list mein store karo aur poori list print karo
# i=1
# list=[]
# while(i<=5):
#     num=int(input("Enter a number:"))
#     list.append(num)
#     i+=1
# print(list)

# i=1
# list=[]
# while(i<=5):
#     num=int(input("Enter a number:"))
#     list.append(num)
#     i+=1
# print(list)


# List ke sab numbers ka sum calculate karo
# lists=[2,4,6,8,9,5,4,1,8,9,4]
# sum=0
# i=0
# while(i<len(lists)):
#     sum=sum+lists[i]
#     i+=1
# print("lists ky saab element ka sum =",sum)
# print(lists)



# nums=[2,6,9,4,5,8,1,6,5,8,9,5]
# max_num=nums[0]
# i=0
# while(i<len(nums)):
#     if(nums[i]>max_num):
#         max_num=nums[i]
#     i+=1
# print("The largest number in the list is:",max_num)        



# lists=[4,4,2,7,8,4,2,1,0,6,6,9,6,5,]
# min_num=lists[0]
# i=0
# while(i<len(lists)):
#     if(lists[i]<min_num):
#         min_num=lists[i]
#     i+=1
# print("The smallest number in the list is:",min_num)
        

# List ke sirf even numbers print karo
lists=[2,4,8,5,2,6,8,5,2,9,1,4]
even=[]
i=0
while(i<len(lists)):
    if(lists[i]% 2==0):
        even.append(lists[i])
    i+=1
print("These are even numbers in th list:",even)



    





































































  
             
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          