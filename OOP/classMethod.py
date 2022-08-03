#-------------------------------classmethod------------------------#
class Student:
    def __init__(self, name, subject, level):
        self.name=name
        self.subject=subject
        self.level=level

    def getDetails(self):
        print(f'Name: {self.name}, Subject: {self.subject}Level: {self.level}')

    @classmethod
    def getDetails_using_classmethod(cls, name, subject, level):
        print(f'Student Name: {name},Student Level: {level}, Student Subject: {subject}')

    @staticmethod
    def test(a,b):
        print('This is test from static method:',a,b)
        return "This is test"

#--Without using class method--#
#s1 object is able to access the method defined inside class Student
print('Without using class method:')
s1=Student('Rohit', 'BSc', 5)
s1.getDetails()

print('')
print('Using class method:')
s2=Student.getDetails_using_classmethod('abc', 'BBA', 4)
#s2.getDetails_using_classmethod()==> Object cannot access classmethod

#----Using static method-----#
print('')
print('Using static method')
static_test=Student.test('a','b')
print(static_test)
