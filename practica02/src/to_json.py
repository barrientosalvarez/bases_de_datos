"""
Para este script se usaran las bibliotecas "csv" para acceder a la informacion 
contenida en el archivo csv y "json" para crear el nuevo archivo con la informacion
en formato json.
"""
import csv
import json

data={}

with open('files/inventario/inventario.csv', encoding='utf-8') as csvf:
    csvReader=csv.DictReader(csvf)

    for rows in csvReader:
        key=rows['ID']
        data[key]=rows

with open('files/inventario/inventario.json', 'w', encoding='utf-8') as jsonf:
    jsonf.write(json.dumps(data, indent=4))
