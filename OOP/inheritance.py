'''
1. Single Inheritance
2. Multiple
3. Multilevel
4. Hierarchial
5. Hybrid

syntax: class child_class(parent_class1, parent_class2)
'''

class Person:
    def __init__(self, name):
        self.name = name
        self.is_emp = False

    def get_description(self):
        print('This is a person class description.', self.name, self.is_emp)
    
    #single inheritance

class Employee(Person):
    def employee_status(self):
        self.is_emp=True

person=Person('ABC')
print("Person", person.name, person.is_emp)
print('person parent class calling method', person.get_description())

employee = Employee('Rohit')
employee.employee_status()
print('employee', employee.name, employee.is_emp)
print('employee class calling parent method')
employee.get_description()
#print(Employee.mro())

#--When a parent class is inherited by more than one child or subclasses -> Hierarchial Inheritance--#
class Staff(Person):

    # Overriding init example
    def __init__(self, name):
        super(Staff, self).__init__(name)
        self.is_emp=True

    def get_staff_status(self):
        return self.is_emp

staff_obj=Staff('Staff1')
print('Staff', staff_obj.name, staff_obj.is_emp)
print('get staff status', staff_obj.get_staff_status())
staff_obj.get_description()

print('')
print('DOGS')
class Dog:
    def __init__(self, name, color):
        self.name=name
        self.color=color

    def get_color(self):
        print('Parent class ', self.color)
        return self.color

class Labrador(Dog):

    def __init__(self, name, color, fur='double-coated'):
        super(Labrador,self).__init__(name, color)
        self.fur=fur

dog = Dog('Tom', 'black')
lab_obj = Labrador('Mickey', 'Golden')
print(dog.name, dog.color)
print(lab_obj.name, lab_obj.color, lab_obj.fur)
print(lab_obj.get_color())
print(dog.get_color())
# print(dog.fur)           # >> Error coz parent class has no breed_name

#--issubclass(sub,sup) method--#

print(issubclass(Labrador, Dog))#Prints True if Labrador in subclass of class Dog. If Labrador inherits Dog
print(issubclass(Dog, Labrador))

#--isinstance (obj, class) method--#

print(isinstance(lab_obj, Dog))#Prints True if lab_obj is object of class Dog
print(isinstance(lab_obj, Labrador))

#-----------------Method Overriding------------------#

class Students:
    def speak(self):
        print('Student')

class BBA(Students):
    def speak(self):
        print('BBA Students')

class BSC(Students):
    def speak(self):
        print('BSC Students')

class BA(Students):
    def speak(self):
        print('BA Students')

s1=Students().speak()
s2=BBA().speak()
s3=BSC().speak()