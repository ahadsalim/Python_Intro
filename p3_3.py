s=''
list=''
for i in range(5) :
    ss= input('Name : ')
    ss=ss.lower()
    ss= ss[0].upper() + ss[1:]
    list = list + '\n'+ ss

print (list)
