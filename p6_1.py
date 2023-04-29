import hashlib
import csv
sha=dict()
csv_file = open('d:\sha256_lib.csv', 'w')
writer = csv.writer(csv_file)
for i in range(10000) :
    s=str(i)
    h_s=hashlib.sha256(s.encode('utf-8')).hexdigest()
    sha[h_s]= i
    writer.writerow([h_s,s])
csv_file.close()
