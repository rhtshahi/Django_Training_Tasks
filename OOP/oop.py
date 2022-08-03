# from curses import ACS_GEQUAL

class Person:
     age=1
     name='abc'

     def get_name(self):
        print(f'my name is {self.name}')
p=Person()
p.get_name()

class Person:
    
    def __init__(self, name, age):
        self.age = age
        self.name = name

    def get(self):
        print('Calling here: ', self.name, self.age)

    def __str__(self):
        return f"My name is {self.name}"

p1=Person('abc', 19)
p2=Person('xyz', 20)
print('Name: ', p2.name)
print('Age: ',p2.age)

print(p1.get())

print(Person.get(p2))

print('This is str for p', p1)

from datetime import date

class Person:

    def __init__(self, name, age):
        self.name=name
        self.age=age
    
    @classmethod
    def obj_createwithage_by_yr(cls, name, year):

        age = date.today().year-year 
        print(age)
        return cls(name, age)

print('')
print('Age is: ')

person = Person('Rohit', 22)
person2 = Person.obj_createwithage_by_yr('Rht', 2010)