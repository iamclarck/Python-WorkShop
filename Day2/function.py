# # def  add():
# #     name = input("Enter your name:")
# #     product = input("Enter your product:")
# #     print(f"Hii {name} thanks for purchasing {product}")
# # add()
    
# def vote():
#     age=int(input("Enter your age:"))
#     if(age<=18):
#         print('you are not eligible for vote')
#     else:
#         print("you are eligible for vote")
# vote()

# def div(a,b):
#     diff = a // b
#     return diff
# print(div(10,2))

# def mark():
#     marks = int(input("Enter marks:"))
#     if(marks<29):
#         print('fail')
#     else:
#         if(marks>90):
#             print('A+')
#         else:
#             print('B+')
# # mark()
# def add(*args,a):
#     ans = sum(args)
#     print(ans)
#     print(type(args))
# addition = add(2,3,a=5)
# # # print(addition)
# def person(b,c,**kwargs):
#     print(type(kwargs['name'])
#     print(type(b+c))

# person(10,20,name={'donde','lagggggging','codebind','colt'})

# def print_kwargs(**kwargs):
#         print(kwargs)

# person = ['donde','lagggggging','codebind','colt']
# if 'donde1' in person:
#     print("exist")
# else:
#     print('sorry')

# def person(name,**kwargs):
#     for i in name:
#         if i[0] in 'aeiou':
#          print(i)
#         else:
#             print("not exist")
# person(['donde','lagggggging','eodebind','aolt'])

# map Function
# def square(num):
#     return  num**2
# valuse = [2,4,5,3,2,1]
# print(list(map(square,valuse)))


# def isEven(num):
#     # if num%2==0:
#     #     return True
#     # else:
#     #     False
#     return True if num%2==0 else False
# print(list(filter(isEven,valuse)))

# num = [1,2,3,4,5,6,7,8]
# print(list(map(lambda num:num**2,num)))

# Reduce function
# import functools
# a=[1,2,3,4,5,6,7]
# sum_list = functools.reduce(lambda x,y: x+y,a)
# print(sum_list)

# Opps
class Employee:
    counter = 0
    def __init__(self,fname,lname,email,salary):
        self.fname=fname
        self.lname=lname
        self.email=email
        self.salary = salary
        Employee.counter +=1
    def fullName(self):
        return f'{self.fname} {self.lname}'
    raise_amount = 1.04
    def apply_raise(self):
        self.salary = int(self.salary * self.raise_amount)


    @classmethod
    def from_string(cls,emp_str):
        fname,lname,email,salary = emp_str.split('-')
        return cls(fname,lname,email,salary)


    @staticmethod
    def work_day(day):
        if(day.weekday()==5 or day.weekday()==6):
            return 'Holiday!'
        else:
            return 'Working day!'

    @property
    def email1(self):
        return f'{self.fname}{self.lname}@gmail.com'


    # @property
import datetime
current_day = datetime.date(2000,4,13)
print(Employee.work_day(current_day))


# Inheritance
class Developer(Employee):
    raise_amount = 1.08
    def __init__(self,fname,lname,email,salary,prog_lang):
        Employee.__init__(self,fname,lname,email,salary)
        self.prog_lang = prog_lang    
    
emp3=Developer('Ashraf','sonde','ashraf@gmail.com',232452454,'Python')

emp = Employee("Deepak","Prajapati","codebind12@gmail.com",100000000)
emp1 = Employee("Hamdan","Ansari","hamdan12@gmail.com",1500000)
print(emp3.__dict__)  
# print("Salary:",emp.salary)
# print("Salary:",emp1.salary)
# print(emp1.fullName())
# print(emp.fullName())
# emp.apply_raise()
# print("Increased salary:",emp.salary)
tempEmp = Employee.from_string('TestName-LastName-test@test.com-2000')
print(tempEmp.fname,tempEmp.lname,tempEmp.salary,tempEmp.email)
print(tempEmp.__dict__)

# Employee.raise_amount = 3
# print(Employee.raise_amount)
# print(emp.raise_amount)
# print(emp1.raise_amount)
# print(Employee.__dict__)
# print("\n")
# print(emp.__dict__)
# print(emp1.__dict__)
# print('Total number of employees:',Employee.counter)

print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp3.raise_amount)
print(emp3.prog_lang)
print(Employee.email1(emp3))

