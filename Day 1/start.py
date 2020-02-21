# # # a=int(input("Enter the number:"))
# # # b=int(input("Enter the number:"))
# # # print(a+b)

# # # Dictionay
# # student ={
# #     "name":"colt steele",
# #     "rollno":"17CO22",
# #     "age":28,
# #     "Phone":[983989984,4799957495]
# # }

# # student["age"]=29
# # # Adding new value to dictionary
# # student["Subject"]="Python"
# # print(student)

# # # Loops

# # for i in range(0,10,2):
# #     print(i,"M&M")

# # # for var in set(range(5)):
# # #     print(var)

# # for i in "Python":
# #     print("Letters are:",i)


# # fruits=["mango","Banana","Orange"]
# # for i in fruits:
# #     print(i)

# # # While loop
# # # i=1
# # # while(i<20):
# # #     i+=1
# # #     print(i)
# # i = 0
# # while i < 6:
# #   print(i)
# #   if i == 3:
# #     continue
# #   i += 1
# # print("i is no longer in loop")
# iteration = int(input("Enter the number:"))
# a = 0
# b = 1
# counter = 0
# print(a)

# while(counter < iteration):
#     a = b
#     b = counter
#     counter = a+b
#     print(counter)
  
# Functions
def add(num1,num2):
    return num1+num2
print("Addition is:",add(12,13))

def sub(num1,num2):
    return num1-num2
print("Substraction is:",sub(16,13))

def mul(num1,num2):
    return num1*num2
print("Multiplication is:",mul(12,13))


def fibo(number):
    a,b=0,1
    print(a)
    print(b)
    i=1
    while(i<number):
        c=a+b
        a,b=b,c
        i+=1
        print(c)
fibo(10)

# F string
guess=10
print(f"your guess {guess} was wrong!")

print("How many kilometers did you cycle today??");
kms=input()
miles=float(kms)/1.6093
miles=round(miles,2)
print(f"Your {kms} km ride was {miles} miles!")

# if else
name=input("Enter the name!\n")
if name =="Arya Stark":
    print("Valar Morghulis")
elif name =="John Snow":
    print("You know nothing!")
else:
    print("carry on!")