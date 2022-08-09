class Bird:
    def __init__(self):
        self.status=True

    def does_fly(self):
        if self.status==True:
            print('It can fly.')
            return True
        else:
            print('It cannot fly.')
            return False

class Pegion(Bird):
    def __init__(self, status=True):
        self.status=status

class Ostrich(Bird):
    def __init__(self, status=False):
        self.status=False

#---Testion for pegion object---#
print('Testion for pegion object')
bird1=Pegion()
bird1.does_fly()

#---Testion for ostrich object---#
print('')
print('Testion for ostrich object')
bird2=Ostrich()
bird2.does_fly()