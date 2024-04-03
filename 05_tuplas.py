### Tuplas ###

my_tuple = tuple()
my_other_tuple = (35, 24, 52, 30, 30, 17)

my_tuple = (27, 1.87, 'Pablo', 'Poker21')
print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])
# print(my_tuple[-9]) IndexError

print(my_tuple.count('Pablo')) # nos cuenta cuantas veces esta Pablo

print(my_tuple.index('Pablo')) # nos devuleve el indice

'''
OJO EN LAS TUPLAS SON INMUTABLES
por lo cual solo podemos guardar datos
'''
# my_tuple[1] = 2.00
# print(my_tuple)

# en este caso tenomos la suma de dos tuplas
my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)
print(my_sum_tuple[3:6]) 


# puede haber casos en lo que realmente necesitemos hace inserciones eliminar y demás coas, pues podemos convertir una tupla a lista
my_tuple = list(my_tuple)
print(type(my_tuple))
my_tuple.insert(1, 'Rojo')
print(my_tuple)
my_tuple = tuple(my_tuple)
print(type(my_tuple))


del my_tuple
print(my_tuple) # esto es un error por que 'del' elimina la tupla 'my_tuple'