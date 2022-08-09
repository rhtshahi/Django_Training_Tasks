class Bird():
    def __init__(self, status):
        self.status=status

    def does_fly(self):
        if self.status==True:
            print('It can fly.')
            return True
        else:
            print('It cannot fly.')
            return False

class Ostrich(Bird):
    def __init__(self, status):
        super(Ostrich, self).__init__(status)
        self.status=False

class Pegion(Bird):
    def __init__(self, status):
        self.status=True

ost1=Ostrich(False)
ost1.does_fly()

pegion1=Pegion(True)
pegion1.does_fly()