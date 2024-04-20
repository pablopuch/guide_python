 ### Operadores ###
 
print(3 + 4)
print(3 - 4)
print(3 * 4)
print(3 / 4)

# resto de una divición
print(10 % 2)

# aproximación a un numero entero
print(10 // 3)

# la potencia cubica
print(3 ** 3)

print(4 + 5 - 2 ** 4 / 3 //33)

print('hola' + 'python') # holapython concatenar string

# print('hola' + 4) # no se puede hacer ;)

print('hola' + str(7)) # hola7

print('hola ' * 3) # hola hola hola

print('hola ' * (2 **2)) # hola hola hola hola

my_float = 2.5 * 2
print('hola ' * int(my_float))



############## Operadores Comparativos #################

print(3 > 4)
print(3 < 4)
print(3 <= 4)
print(3 >= 4)
print(3 == 4)
print(3 != 4)
print(3 > 4 == 2)

print('hola ' < 'python')
print('hola ' > 'python')
print('hola ' <= 'python')
print('hola ' >= 'python') # Ordenacion alfabética por ASCII
print(len('aaa') >= len('AAA')) # Cuenta los caracteres
print('hola ' == 'python')
print('hola ' != 'python')



############## Operadores lógicos ###############


print(3 > 4 and 'hola ' > 'python') # en este caso el "and" se tiene que cumplir los dos
print(3 > 4 or 'hola ' < 'python') # aquí la logica es que se cumpla uno "O" otro
print(not(3 > 4)) # el not espara negar toda la condición