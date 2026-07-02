# with open("data_csv.csv","w") as f:
#     f.write("name,age,class\n")
#     f.write("kalpesh,21,MCA\n")
#     f.write("jayesh,25,web_developer\n")
#     f.write("dharmraj,50,contractor")
import csv
with open("student.csv","w") as f:
    f.write("name,age,marks\n"),
    f.write("kalpesh,21,72\n"),
    f.write("jayesh,25,78\n"),
    f.write("ram,23,96\n"),
    f.write("rahul,42,22\n"),
    f.write("taddy,32,74")
           
with open("student.csv","r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)
