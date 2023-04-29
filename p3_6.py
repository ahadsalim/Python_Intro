s= input('Enter your string : ')
s=s.lower().replace(' ','')
if s== s[::-1] :
    print('palindrome')
else :
    print ('not palindrome')
    