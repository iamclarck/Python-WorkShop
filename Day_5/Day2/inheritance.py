class X:
    pass
a1 = X()

class Y:
    pass
b1 = Y()

class Z:
    pass
c1 = Z()

class A(X,Y):
    pass

class B(Y,Z):
    pass

class M(A,B,Z):
    pass
obj = M()

print(obj)
# mro(method resolution order) print all the inherit classes
print(M.mro()) 

