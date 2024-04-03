### Sets ###

my_set = set()
my_other_set = {} # en python se pueden declarar sets y diccionarios igual

print(type(my_set))
print(type(my_other_set))


my_other_set = {27, 1.87, 'Pablo', 'Poker21'}
print(type(my_other_set))

print(len(my_other_set))

my_other_set.add('Rojo')
print(my_other_set) # Un set no es una estructura ordenada

my_other_set.add('Rojo')
print(my_other_set) # un set no admite repetidos

'''
Dentro de los Sets tenemos la pocivilidad de comprar 
si un elemento se encunatra dentro del set
'''
print('Pablo' in my_other_set)
print('Paula' in my_other_set)

my_other_set.remove('Pablo') # Elimina un elemento
print(my_other_set) 


my_other_set.clear() # Con 'clear' borramos todo el contenido del set
print(len(my_other_set))  

'''
Llegados a este punto, tenemos que tener en ucnta que un set nos puede servir para
tener elementos no duplicados y que no esten ordenados
'''

del my_other_set
# print(my_other_set) esto no esta definido

my_set = {'Pablo', 'Puch', 25}
my_list = list(my_set)

print(my_list)
print(my_list[1])

my_other_set = {'php', 'python', 'javascript'}

my_new_set = my_set.union(my_other_set) # uniendo dos sets
print(my_new_set)
print(my_new_set.union({'html','css'}))

print(my_new_set.difference(my_set)) # diferencia entre sets
