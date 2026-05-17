# print("Hello world!")
# print("I am a AI Agent!")
# name=input("Enter your name:")
# print("Hello!",name)



# correct_password="python1122"
# user_password=int(input("Enter your password:"))
# if(user_password==correct_password):
#     print("Login successful!")
# else:
#     print("Login failed!")


# num1=int(input("Enter first number:"))
# num2=int(input("Enter second number:"))
# num3=int(input("Enter third number:"))
# if(num1>num2 and num1>num3):
#     print(num1,"is greater")
# if(num2>num1 and num2>num3):
#     print(num2,"is greater")
# else:
#     print(num3,"is greater")



# i=1
# while i<=10:
#     print(i)
#     i+=1





# i=1
# while i<=20:
#     if(i%2==0):
#         print(i)
#     i+=1


# num=int(input("Enter a number:"))
# i=1
# while i<=10:
#     print(num,"*",i,"=",num*i)
#     i+=1


# 1 se N tak numbers ka sum calculate karo (N user input hoga)
# n=int(input("Enter a number:"))
# i=1
# sum=0
# while(i<=n):
#     sum+=i
#     i+=1
# print("sum of",n,"number is",sum)


# Countdown program banao (10 se 1 tak reverse print).
# i=10
# while(i>=1):
#     print(i)
#     i-=1


# User bar bar number enter kare jab tak wo 0 enter na kare.
# n=int(input("Enter a number:"))
# while(n!=0):
#     print("You enterd a number",n)
#     num=int(input("Enter a number:"))   


# Password system banao — user ko 3 attempts milen.
# correct_password=1122
# attempt=1
# user_password=int(input("Enter a password:"))
# while(user_password!=correct_password):
#     attempt+=1
#     user_password=int(input("Enter a password:"))
#     if(attempt==3):
#         print("your account is blocked!")
#         break
# else:
#     print("Login successful!")



# i=1
# while(i<=50):
#     if(i%3==0):
#         print(i)
#     i+=1    


# nums=[3,4,7,8,9,1,2,4,6,9,10,12,54,67,8]
# index=0
# while(index <=len(nums)-1):
#     print(nums[index])
#     index  +=1


# nums=[3,4,7,8,9,1,2,4,6,9,10,12,54,67,8]
# print(nums[0])
# print(nums[1])
# print(nums[2])
# print(nums[3])               #by indexing list ky element ko print krwany ky lia 




# nums=[3,4,7,8,9,1,2,4,6,9,10,12,54,67,8]
# index=0
# while(index <len(nums)):
#     print(nums[index])
#     index  +=1


# i=0
# while(i<=10):
#     if(i%2==0):
#         print("Founded",i)
#     i+=1




# nums=[3,4,7,8,9,1,2,4,6,9,2,10,12,2,54,67,8]
# x=2
# index=0
# while(index <=len(nums)-1):
#     if(nums[index]==x):
#         print("Found at index",nums[index])
#     else:
#         print("Founding at index",nums[index])    
#     index +=1





# nums=[3,4,7,8,9,1,2,4,6,9,10,12,54,67,8]
# x=2
# index=0
# while(index <=len(nums)-1):
#     if(nums[index]==x):
#         print("Found at index",nums[index])
#         break
#     else:
#         print("Founding at index",nums[index])    
#     index +=1



# nums=[2,4,6,8,10,12,14,16,18,20,3,5,7,9,33,55,67,79,55]
# index=0
# while(index <=len(nums)-1):
#     if(nums[index]%2==0):
#         index+=1
#         continue
#     print(nums[index])
#     index +=1 




# nums=[2,4,6,8,10,12,14,16,18,20,3,5,7,9,33,55,67,79,55]
# index=0
# while(index <=len(nums)-1):
#     print(nums[index])
#     index+=1



# nums=[2,4,6,8,10,12,14,4,18,12,3,5,7,2,33,55,6,79,55]
# new_nums=[]
# index=0
# while(index <=len(nums)-1):
#     new_nums.append(nums[index])
#     index+=1
# nums=set(new_nums)  
# nums=list(set(nums))  
# print(nums)
    


# User se number lo aur count karo us number mein kitne digits hain.
# nums=input("Enter a numbers:")
# print("Length of list is",len(nums))


# User se number lo aur us number ko reverse print karo
# nums=input("Enter a numbers:")
# reverse_nums=nums[: :-1]
# print(reverse_nums)




# User numbers enter karta rahe jab tak negative number na aaye. Phir total sum print karo.
# nums=int(input("Enter a number:"))
# sum=0
# while(nums>=0):
#     sum=sum+nums
#     nums=int(input("Enter a number:"))
# print("Sum of all nuumbers is",sum)




# from numpy.core.defchararray import index
# username=["Ali","Ahmad","Akram","Naveed","Bilal","Umer","Jaffer"]
# index=0
# new_usernames=[]
# while(index<=len(username)-1):
#     new_usernames.append(username[index])
#     print(username[index])
#     index+=1
# new_usernames=set(list(new_usernames))
# print(new_usernames)


 
# F0R LOOP
# for item in username:
#     print(item)


# def sum(num1,num2):
#     result=num1+num2
#     print(result)
# sum(5,5)


# def check(num):
#     if(num%2==0):
#         print("Even")
#         return True
#     else:
#         print("Odd")
#         return False
# output=check(10)
# if(output==True):
#     print("My favourit number")
# else:
#     print("My not favourit number")

# print("after function")



# def numbers(num1,num2):
#     return num1+num2
# result=numbers(10,20)
# output=result-5*10/3
# print(output)
   

# fruites=["Apple","Banana","Cherry","Date","Fig","Orange","Papaya","Quince","Raspberry","Strawberry"]
# index=0
# new_fruites=[]
# while(index<len(fruites)):
#     new_fruites.append(fruites[index])
#     index+=1    
# print(new_fruites)


# def squ(num):
#     return num*num
# output=squ(5)
# print(output)    


# def check(num):
#     if(num%2==0):
#         return "Even"
#     else:
#         return "odd"
# output=check(int(input("Enter a number:"))) 
# print(output)           



# def big(num1,num2):
#     if(num1>num2):
#         return num1
#     else:
#         return num2
# output=big(int(input("Enter a number:")),int(input("Enter a number:")))
# print(output)           


# def sum():
#     total=0
#     nums=[1,2,3,4,5,6,7,8,9,10]
#     for item in nums:
#         total+=item
#     return total
# output=sum()
# print(output)        
    
    
# def reverse(text):
#     return text[::-1]
# output=reverse("My name is Sharjeel")
# print(output)  


# def vowal_check(text):
#     vowals="aeiouAEIOU"
#     count=0
#     for char in text:
#         if char in vowals:
#             count+=1
#     return count
# output=vowal_check(input("Enter a text:"))
# print(output)
    

# def check_letter(text):
#     count=0
#     for char in text:
#         if char.isupper():
#             count+=1
#     return count
# output=check_letter(input("Enter a text:"))
# print(output)


# def check_length(text):
#     count=0
#     for char in text:
#         if char.isalpha():     #yaa function only letters ko count krta hai  spaces ko ingnore kry ga
#             count+=1
#     return count
# text=input("Enter a text:")  
# output=check_length()
# print("lenght",output)   #length ko print krwany ky lia 
# print("text",text)         #text ko print krwany ky lia 
         
 
# def check_length(text):
#     output=len(text) 
#     return output
# output=check_length("Enter a text:")
# print(output)         #yaa bhi string ki length count krta hai but iss mein spaces bhi count hou gi
    

 





print("Hello sharjeel ","Welcome to our code")   
print("Print is a built in function")
    


























































































    






