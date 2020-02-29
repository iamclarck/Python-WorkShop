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
    

class Manager(Employee):
    # def __init__(self,fname,lname,email,salary):
        # Employee.__init__(self,fname,lname,email,salary)
    pass
print(Manager.counter)


emp = Manager("Deepak","Prajapati","codebind12@gmail.com",100000000)
emp1 = Employee("Hamdan","Ansari","hamdan12@gmail.com",1500000)