# # # for i in range(1,11):
# # #     count=1
# # #     smile=''
# # #     while count<=i:
# # #         smile+="\U0001f600"
# # #         count+=1
# # #     print(smile)
# # name=['colt','steele']
# # name[0],name[1]=name[1],name[0]
# # print(name)

# # # list comprehension
# # number =[1,2,3,4,5,6]
# # double_number = [num*2 for num in number]
# # print(double_number)

# # # name1="deepak"
# # # [char.upper() for char in name1]
# # # print(char)

# # # Dictionary
# # # create dictionary with commaseprated value
# # abc = {}.fromkeys('a','b')
# # print(abc)
# # x = abc.get('a')
# # print(x)

# # playlist = {
# #     'title':'patagonia',
# #     'author':'deepak',
# #     'songs':[
# #         {'title':'RapGod','artist':['Eminem'],'duration':2.5,'genre':'sad'},
# #         {'title':'MockingBird','artist':['Eminem'],'duration':2.5,'genre':'sad'},
# #         {'title':'Godzilla','artist':['Eminem'],'duration':2.5,'genre':'sad'}
# #     ]
# # }

# # total =0
# # for song in playlist['songs']:
# #     total+=song['duration']
# #     print(total)


# # numbers =dict(first=1,second=2,third=3)
# # squares={key:value**2 for key,value in numbers.items()}
# # print(squares.values())

# # # Tuples
# # age = (12,34,23,45,51)
# # print(age)
# # print(age.count(12))
# # print(age.index(51))

# # # set

# # location = {'Delhi','Mumbai','Allahabad','China','India','Delhi'}
# # print('Sets----->')
# # print(location)
# # location.add('12')
# # print(location)
# # location.remove('Delhi')
# # location.discard('12')
# # # To avoid an error use discard method
# # print(location)


# # Functions 

# # from random import random

# # def flip_coin():
# #     if random()() >=0.5:
# #         return "Head"
# #     else:
# #         return "Tail"
# # print(flip_coin())


# # def sum_of_all(num1=12,*args):
# #     print(num1)
# #     total=0
# #     for num in args:
# #         total+=num
# #     return total
# # print(sum_of_all(1,2,3,4,5))

# # square = lambda num: num*num
# # nums=[1,2,3,4,5,6]
# # square1 = map(lambda x: x**2,nums)
# # print(list(square1))
# # print(square(8))
# # # print(add(12,34))

# # names = ['Rusty','colt','steele']
# # result=list(filter(lambda c: c[0]=="e",names))
# # print(result)


# # Builtin functions
# nums=[2,4,5,6]
# print(all([num%2==0 for num in nums])) #Returns true if all values are truthy
# print(any([num%2==0 for num in nums]))  #Returns true if any values is truthy

# # Genarator  vs list Comprehension
# # import sys

# # list_compr = sys.getsizeof([x*10 for x in range(1000)])
# # genr_exp = sys.getsizeof(x*10 for x in range(1000))

# # print(f"List Comprehension:{list_compr} Bytes")
# # print(f"Generator Expression:{genr_exp} Bytes")

# # # sorted vs sort (sorted just make copy of values with sorted original values will remain unchanged but in sort Function original values wil also change )

# # numbers = [1,7,3,5,6]
# # print(sorted(numbers,reverse=True))
# # print(numbers)


# # zip
# num1=[1,2,3,4]
# num2=[5,6,7,8]
# print(list(zip(num1,num2)))
# print(dict(zip(num1,num2)))

# # Common types of error
# """
# Syntax Error
# def first:
# nono=1
# """

# """
# Name Error
# test #test is not define
# """
# """
# Type Error(miss match of datatype)
# len(5)
# """

# """
# Index error
# a=["hello"]
# a[2]
# """

# """
# Value Error
# int("foo")
# """

# """
# Key Error
# d={}
# d["foo"]
# """

# # Error Handling
# while True:
        
#     try:
#         num = int(input("Enter the number!:"))
#     except ValueError:
#         print("Please enter the integer value")
#     else:
#         print("Good job!!!!!") 

# # pdb(python debugger)
# import pdb
# first = 'first'
# second = 'second'
# pdb.set_trace()
# result = first + second
# third = 'third'
# result+=third
# print(result)

def numbers(a,b,c,d):
    import pdb; pdb.set_trace()
    return a+b+c+d
numbers(1,2,3,4)
# common commands
'''
n-for next line
p-for print
c-for continue execution
l-list
'''