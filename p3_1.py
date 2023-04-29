s=input("Enter your String : ")
s= s.lower()
position=0
ss=""
for letter in s :
    if letter =='a' or letter=='e' or letter=='i' or letter=='o' or letter=='u' :
        position=position+1
    else :
        ss= ss+ '.' +letter
        position=position+1

print(ss)