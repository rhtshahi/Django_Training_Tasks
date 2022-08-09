class First(object):
    def __init__(self):
        print('First')

    def test():
        print('This is test from First.')

class Second(object):
    def __init__(self):
        print('Second')

    def test():
        print('This is test from Second.')

class Third(First, Second):
    def __init__(self):
        super(Third, self).__init__()
        print('Third')

    # def test():
    #     print('This is test from Third.')

print('---------------------------------------------')
Third()
print(Third.mro())
print(Third.test())