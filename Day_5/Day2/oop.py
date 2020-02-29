class User:
    active_user = 0
    def __init__(self,first,last,age):
        self.first = first
        self.last = last
        self.age = age
        User.active_user+=1

    #class methods 
    @classmethod
    def display_active_users(cls):
        return f'There are currently {cls.active_user} active users'

    @classmethod
    def from_string(cls,data_string):
        first,last,age = data_string.split(',')
        return cls(first,last,int(age))

    def full_name(self):
        return f"{self.first} {self.last}"

    def log_out(self):
        User.active_user -=1
        return f'{self.first} log out'

    def initials(self):
        return f"{self.first[0]}.{self.last[0]}."

    def is_senior(self):
        return self.age>=65

    def birthday(self):
        self.age+=1
        return f"Happy {self.age}th Birthday,{self.first}"

user1 = User("Colt","Steele",35)
user2 = User("Deepak","Prajapati",20)

# print(user1.full_name())
# print(user1.is_senior())
# print(user1.birthday())
# print(User.active_user)
# print(user2.full_name())

# print(user1.log_out())
# print(User.active_user)
print(User.display_active_users())

tom = User.from_string('Tom,Smith,65')
print(tom.first)
print(tom.full_name())
print(tom.birthday())