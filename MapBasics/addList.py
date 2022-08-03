#----Add two lists using map and lambda----#

numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
add_list=[]

for i in range(0, len(numbers1)):
    x=(numbers1[i]+numbers2[i])
    add_list.append(x)
print(add_list)

#---Using map---#
# print('')
# print('Using map')

# num1 = [1, 2, 3]
# num2 = [4, 5, 6]
# newList=[]

# def addLists(l1,l2):
#     for i in range(0, 3):
#         elements=[l1[i]+l2[i]]
#         newList.append(elements)
#     return newList
# y=list(map(addLists,(num1) , (num2)))
# print(y)