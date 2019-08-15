import json
import csv

with open('data.json') as x:
    data=json.load(x)

print(data)

with open('data.csv','w',newline='') as x:
    writer=csv.DictWriter(x, fieldnames=data[0].keys())
    writer.writeheader()
    writer.writerows(data)


file = open ('data.csv','r')
print(file.readlines())
json1=[]
with open('data.csv','r') as x:
    reader=csv.DictReader(x)
    for i in reader:
        json1.append(dict(i))

print(json1)


with open('data.json','w') as x:
    x.write(str(json1).replace("'",'"'))
