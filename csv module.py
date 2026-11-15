import csv

with open("data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Age"])
    writer.writerow(["A", 9])

with open("data.csv", "r") as a:
    reader = csv.reader(a)
    for row in reader:
        print(row)

print("..End")
with open("data2.csv", "w", newline="") as d:
    w = csv.DictWriter(d, fieldnames=["name", "age"])
    w.writeheader()
    w.writerow({"name" : "A", "age" : 9})

with open("data2.csv", "r") as rd:
    r = csv.DictReader(rd)
    for read in r:
        print(read["name"], read["age"])

print("End")