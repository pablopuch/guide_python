### condicionales ###

my_condition = False

if my_condition: # es lo mismo que if my_condition == True:
    print('Se ejecuta la condicion del if')
    
print('La ejecución continua')

my_condition = 5 * 2

if my_condition == 10:
    print('Se ejecuta la condicion del segundo if')
    
if my_condition >= 10 and my_condition < 20:
    print('Es mayor que 10 y menos que 20')
elif my_condition == 25:
     print('Es igual a 25') 
else:
    print('Es menos o igual que 10 o mayor o igual que 20') 

print('La ejecución continua')

my_string = ''

if not my_string:
    print('mi cadena de texto es vacía')
    
if my_string == 'mi cadenaaaaaaaaaaaaaaa':
    print('estas cadena de texto coinciden')