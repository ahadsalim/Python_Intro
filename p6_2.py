import hashlib
import csv

def hash_password_hack(input_file_name, output_file_name):
    sha=dict()
    reader = csv.reader(input_file_name)
    writer = csv.writer(output_file_name)
    for i in range(10000) :
        s=str(i)
        h_s=hashlib.sha256(s.encode('utf-8')).hexdigest()
        sha[h_s]= i
        writer.writerow([h_s,s])
# از فایل ریدر بخوان و بعد در دیکشنری جستجو کن و بعد پاسخ را در رایتر بنویس


input_f = open('input.csv')
output_f = open('output.csv', 'w')
hash_password_hack(input_f,output_f)
input_f.close()
output_f.close()