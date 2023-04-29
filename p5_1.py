import csv
# For the average
from statistics import mean 

def calculate_averages(input_file_name, output_file_name):
    reader = csv.reader(input_file_name)
    writer = csv.writer(output_file_name)
    for row in reader:
        grades=list()
        for grade in row[1:] :
            grades.append(float(grade))
        writer.writerow([row[0],mean(grades)])

def calculate_sorted_averages(input_file_name, output_file_name):
    reader = csv.reader(input_file_name)
    writer = csv.writer(output_file_name)
    gg=list()
    for row in reader:
        g=dict()
        grades=list()
        for grade in row[1:] :
            grades.append(float(grade))
        g['name']=row[0]
        g['average']=mean(grades)
        gg.append(g)
    def myFunc(a):
        return a['average']
    gg.sort(key=myFunc)
    for i in gg :
        name=i['name']
        av=i['average']
        writer.writerow([name,av])


def calculate_three_best(input_file_name, output_file_name):
    reader = csv.reader(input_file_name)
    writer = csv.writer(output_file_name)
    gg=list()
    for row in reader:
        g=dict()
        grades=list()
        for grade in row[1:] :
            grades.append(float(grade))
        g['name']=row[0]
        g['average']=mean(grades)
        gg.append(g)
    def myFunc(a):
        return a['average']
    gg.sort(reverse=True,key=myFunc)
    for i in gg[:3] :
        name=i['name']
        av=i['average']
        writer.writerow([name,av])    


def calculate_three_worst(input_file_name, output_file_name):
    reader = csv.reader(input_file_name)
    writer = csv.writer(output_file_name)
    gg=list()
    for row in reader:
        g=dict()
        grades=list()
        for grade in row[1:] :
            grades.append(float(grade))
        g['name']=row[0]
        g['average']=mean(grades)
        gg.append(g)
    def myFunc(a):
        return a['average']
    gg.sort(key=myFunc)
    for i in gg[:3] :
        name=i['name']
        av=i['average']
        writer.writerow([name,av])        


def calculate_average_of_averages(input_file_name, output_file_name):
    reader = csv.reader(input_file_name)
    writer = csv.writer(output_file_name)
    gg=list()
    for row in reader:
        grades=list()
        for grade in row[1:] :
            grades.append(float(grade))
        gg.append(mean(grades))
    writer.writerow([mean(gg)])


input_f  = open('D:\Projects\python\input.csv')
output_f = open('D:\Projects\python\output.csv','w')
#calculate_averages(input_f,output_f)
#calculate_sorted_averages(input_f,output_f)
#calculate_three_best(input_f,output_f)
#calculate_three_worst(input_f,output_f)
calculate_average_of_averages(input_f,output_f)
input_f.close()
output_f.close()
