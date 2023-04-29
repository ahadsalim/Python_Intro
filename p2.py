sum = 0
count=0
num = int(input())
while (num != -1) :
    count = count +1
    sum = sum + num
    num= int(input())

print ('count=' , count , '. sum=' , sum , ' average=' , sum/count)