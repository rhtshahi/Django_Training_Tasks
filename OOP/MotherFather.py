class Parent:
    def __init__(self):
        print('Parent')

class Mother:
    def __init__(self):
        print('Mother')

class Father:
    def __init__(self):
        print('Father')

class Child1(Mother, Father):
    def __init__(self):
        pass