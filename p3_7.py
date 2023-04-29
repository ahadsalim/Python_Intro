s= input('Enter your String : ')

s=s.upper()
l_ab= s.find("AB")
l_ba= s.find("BA")
print("AB : ",l_ab)
print("BA : ",l_ba)
l_l= abs(l_ba-l_ab)
if l_ab>=0 and l_ba>=0 and l_l>1 :
    print("YES")
else :
    print("NO")