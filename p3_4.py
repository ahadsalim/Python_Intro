s= input('Enter you statment :')
order0= (s.find('h'))
if order0 >=0 :
    order1= s.find('e')
    if order1>order0 :
        order2= s.find('l')
        if order2 > order1 :
            order2 +=1
            ss= s[order2:]
            order3= ss.find('l')
            if order3>=0 :
                order4= ss.find('o')
                if order4> order3 :
                    print('YES')
                else :
                    print ('NO')
            else :
                print ('NO')
        else :
            print ('NO')
    else :
        print ('NO')
else :
    print ('NO')