import mysql.connector

dbku = mysql.connector.connect(
    host='localhost',
    port=3306,
    user='root',
    password='denny2310',
    auth_plugin = 'mysql_native_password'
)
kursor=dbku.cursor()
kursor.execute('use doraemon')
kursor.execute('describe karakter')
b=kursor.fetchall()

data={}
newdata=[]

key=[]
val=[]
for item in b:
    key.append(item[0])
kursor.execute('use doraemon')
kursor.execute('select * from karakter')
a=kursor.fetchall()
for item in a:
    val.append(item)
isi=[]
for item in range(len(val)):
    new={}
    for item1 in range (len(val[item])):
        new[key[item1]]=val[item][item1]
    isi.append(new)
import json
import csv


# Convert to JSON=========================================================================
with open('convert.json','w') as x:
    x.write(str(isi).replace("'",'"'))
# Convert to CSV==========================================================================
with open('convert.csv','w',newline='') as x:
    field=isi[0].keys()
    writer=csv.DictWriter(x, fieldnames=field)
    writer.writeheader()
    writer.writerows(isi)







