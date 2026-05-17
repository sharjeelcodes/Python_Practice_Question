#                      #SETS
# names={"ali","ahmad","bilal","umer","bilal"} 
# names.add("bilal")
# names.remove("ali")
# print(names) 


# nums=[2,4,6,8,6,8,2,4,12,2,6,8,12,7,9,3,11,23]
# new_nums=set(nums)
# print(new_nums)      


# nums=[2,4,6,8,6,8,2,4,12,2,6,8,12,7,9,3,11,23]
# nums=list(set(nums))
# print(nums)      



# largest=0
# i=1
# while(i<=5):
#     num=int(input("Enter the number:"))
#     if(num>largest):
#         largest=num
#     i+=1
# print("The largest number is:",largest)



# i=0 
# even=0
# while(i<=10):
#     num=int(input("Enter the number:"))
#     if(num%2==0):
#         even+=1
#     i+=1
# print(even,"Even numbers")    




 
# even=0
# for i in range(10):
#     num=int(input("Enter the number:"))
#     if num% 2==0:
#         even+=1
# print(even,"Even numbers")





# sum=0
# for i in range(5):
#     num=int(input("Enter the number:"))
#     if(num<0):
#           continue
#     sum+=num
# print(sum)





# sum=0
# i=1
# while i<=5:
#     num=int(input("Enter a number:")) 
#     if(num<0):
#         continue
#     sum+=num
#     i+=1
# print("sum of total numbers is",sum)

  
# num1=int(input("Enter the first number : "))
# num2=int(input("Enter the second number : "))
# num3=int(input("Enter the third number : "))
# if num1>num2 and num1>num3:
#     print("first number is greater",num1)
# elif num2>num1 and num2>num3:
#     print("Second number is greater",num2)
# else:
#     print("Third number is greater",num3)

# while True:
#     number=int(input("Enter your marks: "))
#     if (number>90 and number<=100):
#         print("A grade")
#     elif(number >80 and number<=90):
#         print("B grade")
#     elif(number>70 and number<=80):
#         print("C grade")
#     elif(number >60 and number>=70):
#         print("D grade")
#     else:
#         print("F grade")



count=0
userpin=1234
useramount=20000
while count<=3:
    pin=int(input("Enter your pin:"))
    count+=1
    if pin==userpin:
        amount=int(input("Enter your amount : "))
        if amount<=useramount:
            useramount-=amount
            print("Withdrawl Successfully,")
            print("Please take your cash")
            print("Thank you for using our ATM")
            break
        else:
            print("Insuffiecient Balance\nTry again")
    elif pin!=userpin:
        print("Invalid pin\nTry again")
print("Your aacount is blocked")

        





































