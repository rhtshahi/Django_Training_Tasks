#---Write a Python program to combine two dictionary adding values for common keys.---# 
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
#Sample output: {'a': 400, 'b': 400, 'd': 400, 'c': 300}

for x in d2:
    if x in d1:
        d2[x]=d2[x]+d1[x]

    else:
        pass
print(d2)