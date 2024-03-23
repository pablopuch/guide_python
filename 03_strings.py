### Strings ###

my_string = 'My string'

my_other_string = "My other string"

print(len(my_string))
print(len(my_other_string))

print(my_string + "" + my_other_string)

my_string_line = 'Este es una oración \nen dos lineas'

print(my_string_line)

my_string_line_tabulado = '\tEste es una oración \nen dos lineas'

print(my_string_line_tabulado)


### Formateo

name, surname, age = 'pablo', 'puch', 35

print('Mi nombre es %s %s y mi edad es %s'.format(name, surname, age))
print('Mi nombre es %s %s y mi edad es %s' %(name, surname, age))

print(f'Mi nombre es {name} {surname} y mi edad es {age}')



### Desempaquetado de caracteres

language = 'python'

a, b, c, d, e, f= language

print(a)
print(e)


### División

language_slice = language[1:3]
print(language_slice)

language_slice = language[1:]
print(language_slice)

language_slice = language[-2]
print(language_slice)

language_slice = language[1:4:6]
print(language_slice)

### Reverso

language_slice = language[::-1]
print(language_slice)


### Funciones

print(language.capitalize())
print(language.upper())
print(language.count('t'))
print(language.isnumeric())
print(language.lower())
print(language.upper().isupper())

