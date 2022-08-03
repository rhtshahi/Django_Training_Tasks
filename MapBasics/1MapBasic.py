#-----------------------------------MAP----------------------------------------#
print('ADD: ')
def add(i):
    i+=10
    return i

a = map(add, [1, 2, 3])
print(a)
print(list(a))


print('')
print('MULTIPLY: ')
li=[1, 2, 3, 4]
def prd(n):
    i=7
    n=i*n
    return n
product=map(prd, li)
print(product)
print(list(product))

print('')
print('DIVIDE: ')

def division(x):
    i=3
    x=int(x/3)
    return x
y=list(map(division, (4, 7, 10, 13)))
print(y)

#-----map with lambda----#
print('')
print('map with lambda: ')
map_lambda1=list(map(lambda a:a+1,(2, 4, 5, -8, -2, -1)))
print(map_lambda1)

#----Calculating length of string using map----#
print('')
print('Calculating length of string using map:')
words=('abc', 'python', 'oop', 'map', 'string', 'calculator', 'django')

def ret_len(x):
    return len(x)

y=list(map(ret_len, words))
print(y)