
def maghsoom(num,is_print) :
    count=0
    for i in range(2,num) :
        if num % i == 0 :
            count = count+1
            if is_print :
                print (i)
    return count


a=0
b=0
for i in range(10) :
    num= int(input('Enter your number : '))
    tedad_maghsoom= maghsoom(num,False)
    if tedad_maghsoom > b : 
        a= num
        b= tedad_maghsoom
    elif tedad_maghsoom == b and num>a :
        a= num
        b= tedad_maghsoom

print('The Number is : ',a , ' Maghsooms are : ')
c=maghsoom(a,True)
print('Tedad maghsoom ha : ',c)
    