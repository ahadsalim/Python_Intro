n_w= int(input('how many words : '))
dictionary = dict()
for w in range(n_w) :
    words= input('enter phrase with translated : ')
    words =words.strip().split()
    dictionary[words[0]] = words[1]

sentences = input('Enter you sentences: ')
s=""
sentences = sentences.strip().split()
for w in sentences :
    s += dictionary.get(w,w)+' '


print(dictionary)
print(s)