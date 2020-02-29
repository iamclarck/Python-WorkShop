# def my_for(iterable):
#     iterator = iter(iterable)
#     while True:
#         try:
#             print(next(iterator))
#         except StopIteration:
#             break

# my_for('Hello World!')
# my_for([1,2,3,4])
        
# def fib_list(max):
#     num = []
#     a,b = 0,1
#     while len(num) < max:
#         num.append(b)
#         a,b = b , a+b
#     return num

# print(fib_list(20))


# generators

def fibo_gen(max):
    x = 0
    y = 1
    count = 0
    while count < max:
        x ,y = y,x+y
        yield x
        count+=1 
for n in fibo_gen(10):
    print(n)