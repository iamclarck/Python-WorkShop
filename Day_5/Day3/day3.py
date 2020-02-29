a=10
def print1():
    global a
    a=12 + 21
    print('Inside local:',a)
print1()
print('outside local',a+12)