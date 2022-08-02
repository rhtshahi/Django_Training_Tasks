#-----Function to return square of number------#
print('Function to return square of number')
def sq_no(num):
    #return num**2
    print(num**2)

# x=sq_no(12)
# print(x)
sq_no(13)

#------Passing list as parameter-----#
print('')
print('Passing list as parameter')
def list_para(li):
    for i in li:
        print(i, end=' ')
list_para([1, 2, 3, 4, 5])


#-----Function to return length of string------#
print('')
print('Function to return length of string')
def str_len(word):
    #print(len(word))
    return len(word)
print(str_len('javatpoint'))
#str_len('Javatpoint')


#---Function to return square of each element in list---#
print('')
print('Function to return square of each element in list')
def sq_li(li):
    sq=[]
    for i in li:
        sq.append(i**2)
    #print(sq)
    return sq

l1=[1, 3, 5, 7]
print(sq_li(l1))

#---Python code to demonstrate the use of default arguments---#
print('')
print('Python code to demonstrate the use of default arguments')

def default_values(x, y=0):
    print(f'x: {x} and y: {y}')
print('Passing one parameter:')
default_values(3)
print('Passing both parameters:')
default_values(3,7)

#---Python code to demonstrate the use of keyword argument---#
print('')
print('Python code to demonstrate the use of keyword argument')

def key_words(a, b):
    print(f'the value of a is {a} and value of b is {b}.')
print('Without keywords:')
key_words(6, 8)
print('With keywords:')
key_words(b=-1, a=12)

#---All arguments must be passer
# Defining a function  
print('')
def function( num1, num2 ):  
    print("num1 is: ", num1)  
    print("num2 is: ", num2)  
  
# Calling function and passing two arguments out of order, we need num1 to be 20 and num2 to be 30  
print( "Passing out of order arguments" )  
function( 30, 20 )     
  
# Calling function and passing only one argument  
print( "Passing only one argument" )  
try:  
    function( 30 )  
except:  
    print( "Function needs two positional arguments" )

#*args and **kwargs
print('')
print('*args and **kwargs')
print('')

def multiple_args(*multiple_ar):
    print(multiple_ar)
    print(f'First element: {multiple_ar[0]} and Last element: {multiple_ar[-1]}')
multiple_args(3, 5, 7, 9, 'last')

print('List as *args: ')

def myList(*my_list):
    l1=[]

    for i in my_list:
        l1.append(i)
    print(l1)
myList(1, 3, 9, 'a', 'b', 'c')

print('')
print('Using **kwargs: ')

def new_kwarg(**firt_kwarg):
    print(firt_kwarg)
new_kwarg(**({'s_no': 1, 'name':'rohit', 'address':'patan', 'level':4}))

def s_details(**details):
    print(details)
    print(type(details))
s_details(name='Rohit', level=5)

# def my_function(child3, child2, child1):
#   print("The youngest child is " + child3)

# my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

#---Python code to demonstrate the use of return statements---# 
print('')
print('Python code to demonstrate the use of return statements')
  
# Defining a function with return statement  
def square( num ):  
    return num**2  
   
# Calling function and passing arguments.  
print( "With return statement" )  
print( square( 39 ) )  
  
# Defining a function without return statement   
def square( num ):  
    num**2   
  
# Calling function and passing arguments.  
print( "Without return statement" )  
print( square( 39 ) )

#---------------------Lambda-----------------#
print('')
print('Working with lambda:')
print('')

first_lambda= lambda a,b:print(a**b)
first_lambda(b=3, a=2)

second_lambda=lambda num1,num2:print(int(num1/num2))
second_lambda(35,2)

print('')
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))