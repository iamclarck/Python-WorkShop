class Humans:

    def __init__(self,first,last,age):
        self.first = first
        self.last = last

        if age>=0:
             self._age = age
        else:
            self._age = 0

    # property
    @property
    def age(self):
        return self._age

    @age.setter # this method set new value to age
    def age(self,new_value):
        if new_value>=0:
            self._age = new_value
        else:
            raise ValueError("age can't be negative")

    @property
    def fullname(self):
        return f'{self.first} {self.last}'

    @fullname.setter
    def  fullname(self,name):
        self.first,self.last = name.split(" ")



colt = Humans('colt','steele',34)
print(colt.age)
colt.age = 43
print(colt.age)
print(colt.fullname)
colt.fullname = "John Doe"
print(colt.fullname)