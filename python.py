import csv
with open("data.csv") as pfile:
    csv_reader=csv.reader(pfile,delimiter=',')
    line_count=0
    for i in csv_reader:
        if line_count==0:
            print("Columns Manes", ",".join(i))
            line_count+=1
        else:
            print("Columns are", i[1], i[2])
            line_count+=1
print("line count",line_count)