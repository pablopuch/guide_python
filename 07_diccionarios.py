### Diccionarios ###

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))


my_other_dict = {'Nombre': 'Pablo', 'Apellido': 'Puch', 'Edad': 25, 1: 'python'}
my_dict = {
            'Nombre': 'Pablo', 
            'Apellido': 'Puch', 
            'Edad': 25, 
            'lenguajes': {'python', 'php', 'javascript', 'java'},
            1: 1.87,
        }


print(my_other_dict)
print(my_dict)

print(len(my_dict))
print(len(my_other_dict))

print(my_dict['Nombre'])

my_dict['Nombre'] = 'pedro'

print(my_dict['Nombre'])

print(my_dict[1])

my_dict['Calle'] = 'C/ pablo'

print(my_dict)

del my_dict['Calle']

print(my_dict)

print('Pablo' in my_dict) # False
print('pedro' in my_dict) # False

print('Nombre' in my_dict) # True

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())

my_list = ['Nombre',1 , 'Piso']

my_new_dict = my_other_dict.fromkeys(('Nombre', 1, 'Piso'))
print(my_new_dict)

my_new_dict = dict.fromkeys(('Nombre', 1, 'Piso'))
print((my_new_dict))

my_new_dict = dict.fromkeys(my_dict, 'pablo')
print((my_new_dict))


print(list(my_new_dict))
print(tuple(my_new_dict))
print(set(my_new_dict))

