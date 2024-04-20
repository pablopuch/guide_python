### Loops ### 

# While

my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 1
else: # Es opcional
    print('mi condición es mayor o igual que 10')

print('la ejecución continúa')
    
while my_condition < 20:
    my_condition +=1
    if my_condition == 15:
        print('se detiene la condición')
        break # con el break lo utilizamos para parar el bucle
    
    print(my_condition)
    
print('la ejecución continúa')


# For

my_list = [35, 24, 52, 30, 30, 17]

for element in my_list:
    print(element)
    
    
my_tuple = (35, 24, 52, 30, 30, 17)

for element in my_tuple:
    print(element)
    
    
my_set = {27, 1.87, 'Pablo', 'Poker21'}

for element in my_set:
    print(element)
    
    
my_dict = {'Nombre': 'Pablo', 'Apellido': 'Puch', 'Edad': 25, 1: 'python'}

for element in my_dict:
    print(element)
    if element == 'Edad':
        break
    print('Se ejecuta')
else:
    print('El bucle for para mi diccionario a finalizado')

print('Se ejecuta')

for element in my_dict:
    print(element)
    if element == 'Edad':
        continue # indica que que continue el bucle for, OJO cuidado al usarlo
else:
    print('El bucle for para mi diccionario a finalizado')

print('Se ejecuta')