### Listas ###

# Declaraciones de listas, es la mis forma
my_list = list()
my_other_list = []

print(len(my_list)) # longitud de mi lista

my_list = [35, 24, 52, 30, 30, 17]

print(my_list)
print(len(my_list))

my_other_list = [35, 1.85, 'Pablo', 'Puch']

print(type(my_other_list))

# Vamos a acceder a lois elementos por separado
print(my_other_list[0]) # 35
print(my_other_list[1]) # 1.85
print(my_other_list[2]) # pablo
print(my_other_list[3]) # puch
print(my_other_list[-1]) # puch

# IndexError, aquí nos hemos pasado de vuelta ;)
# print(my_other_list[-4]) 
# print(my_other_list[-5])


print(my_list.count(30)) # con el count() contar elementos DENTRO de la porpia lista

# Asignación de elementos a variables
age, height, name, surname = my_other_list
print(name)


# Concatenamos dos listas
print( my_list + my_other_list)

# IndexError
# print( my_list - my_other_list)
# print( my_list * my_other_list)
# print( my_list / my_other_list)


my_other_list.append('DevPuch')# append añade un elemento a la lista al final
print(my_other_list)

my_other_list.insert(1, 'Rojo')# añadimos en una pocicion concreta 
print(my_other_list)

my_other_list[1] = 'Negro'
print(my_other_list)

my_other_list.remove('Negro')# elimina elementos (si hay uno repetido elimine el primero que encuentre) !! OJO CON ESTO
print(my_other_list)

my_other_list.pop()#elimina el ultimo, se le puede pasar el idice de lo que se puede desapilar
print(my_other_list.pop())
print(my_other_list)

del my_other_list[2]# del para borrar el elemeto por indice
print(my_other_list)

'''
La diferencia principal de 'del' y 'remove' es que con 'remove' elimina el elemento que coincide
y 'del' elimina el elemento que conincide con el INDICE.
'''

my_new_list = my_list.copy() # antes de borrar vamos hacer un backup

my_other_list.clear()
print(my_other_list) # borrar de la lista

print(my_new_list)

my_new_list.reverse() # le damos la vuelta
print(my_new_list)

my_new_list.sort() # y lo ordenamos
print(my_new_list)

# Mmmmm tengo hambre vamos hacer revanadas jajajaj
# Conociendo los indices podemos hacer sub-listas.
print(my_new_list[1:3])


# convirtiendo de una lista a una str
my_list = 'Hola Python'
print(my_list)
print(type(my_list))



