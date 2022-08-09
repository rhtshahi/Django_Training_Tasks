class First(object):
    def __init__(self):
        super(First, self).__init__()
        print('First')

    #def test():
    #   print('First method')

class Second(object):
    def __init__(self):
        super(Second, self).__init__()
        print('Second')

    def test():
        print('second method')

class Third(First, Second):
    def __init__(self):
        #super(Third, self).__init__()
        print('Third')

third=Third()
print(third.mro())