#--Write a Python program to get the maximum and minimum value in a dictionary.--#

my_dict = {'x':500, 'y':5874, 'z': 560}#random dictionary
listDict=list(my_dict.values())#extracting values from dictionary
#print(listDict)

max_value=max(listDict)
#print(max_value)

min_value=min(listDict)
#print(min_value)

print(f'The maximum value is {max_value} and minimum value is {min_value}')