import math
num= int(input('How many nubers :'))
n=[]
m=[]
for i in range(num) :
    n.append(int(input('number : ')))
    m.append(math.sqrt(n[i]))

print (n)
for i in range(num) :
    print("{:.4f}".format(m[i]))
