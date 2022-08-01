#---Write a Python program to combine two dictionary adding values for common keys.---# 
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
#Sample output: {'a': 400, 'b': 400, 'd': 400, 'c': 300}
d3={}

for x in d1:
    for y in d2:
        if x==y:
            sum=d1[x]+d2[y]
            #print(sum)  
            d3[x]=sum
        else:
            pass
print(d3)                 