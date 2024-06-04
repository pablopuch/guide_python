### Error Types ###

# SyntaxError

# print 'hola mundo' # Descomentar para ver el error
print ('hola mundo')







# NameError

name = 'pablo' # Comentar para ver el error
print(name)





# IndexError

my_list = ['Ana', 'Raul', 'Jose']
# print(my_list[5]) # Descomentar para ver el error






# ModuleNotFoundError

# import maths # Descomentar para ver el error
import math





# AttributeError

# print(math.PI) # Descomentar para ver el error
print(math.pi)







# KeyError

my_other_dict = {'Nombre': 'Pablo', 'Apellido': 'Puch', 'Edad': 25, 1: 'python'}
# print(my_other_dict['Edad'])
# print(my_other_dict['Eddad']) # Descomentar para ver el error






# TypeError

# print(my_list['nombre']) # Descomentar para ver el error






# ImportError

# from math import PI # Descomentar para ver el error
from math import pi
print(pi)







# ValueError

# my_int = int('10')
# my_int = int('10 años') # Descomentar para ver el error
# print(type(my_int))









# ZeroDivisionError

print(4/2)
# print(4/0) # Descomentar para ver el error