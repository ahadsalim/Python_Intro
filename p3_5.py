s= input('Your search :')
count_l=0
count_b=0
for l in s :
    if l> l.upper() :
        count_l +=1
    else :
        count_b +=1
if count_b>count_l :
    print (s.upper())
else :
    print(s.lower())