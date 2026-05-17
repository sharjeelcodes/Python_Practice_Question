##Practice of List:
list01=["Ali",1080,"Akram",1050,"Sharjeel",878]
print(type(list01)) 
print(len(list01))
print(list01[2])
slicing=list01[0:3]
print(slicing)
print(list01[-4:-1])
list01.append("Naveed")   #append method add a anything at the End.
print(list01)
fruit=["orange","mango","banana","apple","strawbrry"]
fruit.sort()                                           ##Sort the the list in accending order
print(fruit)
fruit.sort(reverse=True)     #sort the list in decending order
print(fruit)
fruit.insert(2,"grapes")    ##insert method:add the anything at the particular Index.
print(fruit)
num=[4,5,7,8,9,1,2,3,]
num.reverse()            #Reverse the any list
print(num)
intro=[9,3,4,6,1,3,9,4,6,2]
intro.sort(reverse=True)
intro.pop(3)
print(intro)   ##remove the any number by his index
names=["Naveed","Ali","Akram","Hassan","Haroon","jaffer","Naeem"]
names.insert(4,"Sharjeel")
names.sort()
print(names)




print("TOPIC:TUPLE")
tup=(3,4,8,2,1,7,4,9,5,7,)
print(tup.index(2))     ##yaha pr hum element lekhy gy joo tuple  mein hai woo hummy bataya ga ky yaa element is tuple mein is index pr hai.
print(tup[0:4])
print(len(tup))
name1=("Ali",)     ##common will be doneted that will be tuple,If not comma there,the type of the variable is string.
print(name1)
print(type(name1))
nums=()             ##Empty tuple
print(nums)
print(type(nums))   