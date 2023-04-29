import random
x= random.randint(1,99)
y= int (input ('Your guess = ? '))
while x != y :
    if y>x :
        print('That is bigger !')
    else :
        print('That is Smaller !')
    
    y= int (input ('You guess = ? '))

print('That is Right:',x)
    