### File Handling ### 

# .txt file

import os


txt_file = open('Intermedio/my_file.txt', 'w+') #Leer y Escribir
print(txt_file.write('\nPablo\nPuch\n26\nPython\nMe gusta la manzana'))

# print(txt_file.read())
# print(txt_file.read(10))
# print(txt_file.readline())
# print(txt_file.readline())
# print(txt_file.readlines())

for line in txt_file.readlines():
    print(line)
    
print(txt_file.write('\nMe gusta la manzana'))
print(txt_file.readlines())

with open('Intermedio/my_file.txt' , 'a') as my_other_file:
    my_other_file.write('\nY la naranja')

txt_file.close()

# os.remove('Intermedio/my_file.txt')




# .json file

import json

json_file = open('Intermedio/my_file.json', 'w+')

json_text = {
            'Nombre': 'Pablo', 
            'Apellido': 'Puch', 
            'Edad': 25, 
            'lenguajes': ['python', 'php', 'javascript', 'java'],
        }

json.dump(json_text, json_file, indent=4)

json_file.close()

with open('Intermedio/my_file.json') as my_other_file:
    for line in my_other_file.readlines():
        print(line)
        
        

json_dict = json.load(open('Intermedio/my_file.json'))
print(json_dict)

print(type(json_dict))
print(json_dict["Nombre"])





# .csv file

import csv

csv_file = open('Intermedio/my_file.csv', 'w+')

csv_writer = csv.writer(csv_file)

csv_writer.writerow(["name", "surname", "age", "language", "website"])
csv_writer.writerow(["pablo", "puch", 26, "python", "https://pablo.com"])

csv_file.close()

with open('Intermedio/my_file.csv') as my_other_file:
    for line in my_other_file.readlines():
        print(line)







# .xlsx file
# import xlsx # Instalar el modulo





# .xml file

import xml

