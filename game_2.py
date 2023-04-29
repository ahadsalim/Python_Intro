print('keep a number between 0,99 in your mind !')
import random
a=0
b=99
x = random.randint(a,b)
count=0
print('Is it ',x)
javab=input('s=my number is Smaller  ,  b=my number is Bigger  ,  e=Exactly: ')
while javab != 'e' :
    if javab == 's':
        b=x
        x=random.randint(a,b)
        print('Is it ',x)
    elif javab== 'b' :
        a=x
        x=random.randint(a,b)
        print('Is it ',x)
    count= count+1
    javab=input('s=my number is Smaller  ,  b=my number is Bigger  ,  e=Exactly: ')

print('WWWWWWWoooooWWWW : ',x , 'you guess ', count , 'times')
