import code
from random import randint

class Employee:
    def __init__(self, name, designation, code):
        self.name=name
        self.code=code
        self.designation=designation
    @staticmethod
    def empCode():
        code=randint(1000,9999)
        #print(code)
        return code

    def empObj(self):
        print(f'Name: {self.name}, Designation: {self.designation}, Code: {self.code}')

    @classmethod
    def classMethod(cls, name, designation):
        emp_id=cls.empCode()
        return cls(name, designation, emp_id)

# code1=Employee.empCode()
#print(code1)

# emp1=Employee('ABC', 'Manager', code1)
# emp1.empObj()
emp2=Employee.classMethod('xyz', 'Manager')
#print(f'Name: {emp2.name}, Designation: {emp2.designation}, Code: {emp2.code}')
print(emp2.name, emp2.designation, emp2.code)