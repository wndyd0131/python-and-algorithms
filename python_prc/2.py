# file I/O
name = input("What's your name?")
file = open("names.txt", "a")
file.write(f"{name}\n")
file.close()

# with
with open("names.txt", "a") as file:
    file.write(f"{name}\n")

# readlines
with open("names.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    print(line, end="")

#
names = []
with open("names.txt", "r") as file:
    for line in file:
        names.append(line.rstrip())

# csv file
students = []
with open("students.csv", "r") as file:
    for line in file:
        first, last = line.rstrip().split(",")
        student = {}
        student["first"] = first
        student["last"] = last
        students.append(student)
print(students)

def get_name(student):
    return student["first"]

for student in sorted(students, key=get_name):
    print(student)

    '''
    or
    '''
for student in sorted(students, key=lambda student: student["first"]):
    print(student)

#CSV Reader
import csv
students_list = []
with open("students.csv", "r") as file:
    reader = csv.reader(file)
    for first, last in reader:
        students_list.append({"first": first, "last": last})

print("CSV Reader")
print(students_list)

#CSV DictReader
import csv
students_list = []
with open("students_dict.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)
        students_list.append({"first": row["first"], "last": row["last"]})

print("DICT Reader")
print(students_list)

#CSV Writer
import csv
first = input("What's your first name?")
last = input("What's your last name?")

with open("students_write.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow([first, last])

#CSV DictWriter
import csv
first = input("What's your first name?")
last = input("What's your last name?")

with open("students_dict_write.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["first", "last"])
    writer.writerow({"first": first, "last": last})