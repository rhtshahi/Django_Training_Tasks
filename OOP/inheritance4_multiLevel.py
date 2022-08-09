class First:
    def __init__(self) -> None:
        print('This is first init.')

    def testing_method(self):
        print('This is first method.')
    
class Second(First):
    def __init__(self) -> None:
        print('this is second init.')

    def testing_method(self):
        print('This is second method.')
    
class Third(Second):
    def __init__(self) -> None:
        print('This is third init.')
    
    def testing_method(self):
        print('This is third method.')

third = Third()

print(Third.mro())
print(third.testing_method())