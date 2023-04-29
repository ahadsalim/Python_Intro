num= int(input('How many players : '))
l=[]
for i in range(num) :
    g= int(input('How many games did he play: '))
    if g<4 : 
        l.append(g)
len= len(l)
team = len//3
print('You can create %s team(s)' % team)