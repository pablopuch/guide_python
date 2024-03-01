'''
    08_Ejercicio
    Queremos guardar los nombres y la edades de los alumnos de un curso. 
    Realiza un programa que introduzca el nombre y la edad de cada alumno. 
    El proceso de lectura de datos terminará cuando se introduzca como 
    nombre un asterisco (*) Al finalizar se mostrará los siguientes datos:
    
        Todos lo alumnos mayores de edad.
        Los alumnos mayores (los que tienen más edad)
'''

list_name = []
list_year = []

while True:
    name_student = input('Nombre del alumno: ')

    if name_student == '*':
        print('***************Programa finalizado***************')
        break

    year_student = int(input('Edad del alumno: '))
    
    list_name.append(name_student)
    list_year.append(year_student)

for name, year in zip(list_name, list_year):
    print(f'{name}: {year}')
    if year >= 18:
        print(f'Mayor de edad {name}: {year}')

max_year = max(list_year)
for name, age in zip(list_name, list_year):
    if age == max_year:
        print(f'Alumno mayor: {name} con {age}')