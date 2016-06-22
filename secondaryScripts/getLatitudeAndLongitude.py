import sqlite3
import requests

connection = sqlite3.connect('incomeDatabase.db')
cursor = connection.cursor()
cursor.execute('SELECT name, state FROM mainSite_city')

temp = cursor.fetchall()
list = []

for x in temp:
    list.append(str(x[0]) + ", " + str(x[1])[:2])

print(type(list))
print(str(list[:2]))

r = requests.post("http://www.datasciencetoolkit.org/street2coordinates/", str(list).replace("'",'"'))
json = r.json() is dict
print(json)
print(type(json))

for key, element in r.json().items():
    if element is not None:
        tuple = (element['latitude'], element['longitude'], key.split(',', 1)[0], key.split(', ', 1)[1])
        print(tuple)
        cursor.execute(
            'UPDATE mainSite_city SET lat = ?, lng = ? WHERE mainSite_city.name = ? AND mainSite_city.state LIKE "%"||?||"%"',
            tuple)

connection.commit()
connection.close()