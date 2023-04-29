s= input('Enter your question : ')
ss=''
for num in s :
    if num == '1' :
        ss= ss + num + '+'
for num in s :
    if num == '2' :
        ss= ss + num + '+'
for num in s :
    if num == '3' :
        ss= ss + num + '+'
print(ss[:-1])