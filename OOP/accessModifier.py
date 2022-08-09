class Person:

    def __init__(self, name, age, password):
        self.name=name
        self.age=age
        self.password=password

    def getName(self):
        print(f'Name: {self.name}')
        return self.name

    def _getAge(self):
        print(f'Age: {self.age}')
        return self.age

    def __getPassword(self):
        print(f'Age: {self.password}')
        return self.password

    def publicClass(self):
        my_name=self.getName()
        my_age=self.__getPassword()
        my_pass=self.__getPassword()
        print('')
        print('Public Method')
        print(f'Name: {my_name}, Age: {my_age}, Password: {my_pass}')

person1=Person('ABC', 20, 'Password123')
person1.getName()
person1._getAge()
person1._Person__getPassword()
person1.publicClass()

class Employee(Person):
    pass

emp1=Employee('Xyz', 21, 'newPass')
emp1.getName()
emp1._getAge()
# emp1._Employee__getPassword()