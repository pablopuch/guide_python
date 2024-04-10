### Funcuines ### 

def my_funcition ():
    print('Esto es una función')
    
my_funcition () # de esta forma podemos llamar a la función


def sum_two_values (first_number, second_number): 
    print(first_number + second_number)
    
    
sum_two_values (5,7)
# sum_two_values (5,7,2) esto peta
# sum_two_values ('5','7') este resultado es 57 son cadenas de string

def sum_two_values_with_return (first_number, second_number):
    return first_number + second_number

my_result = sum_two_values_with_return (10, 5)
print(my_result)

def print_name (name, surname):
    print(f'{name} {surname}')
    
print_name(surname = 'Puch', name = 'Pablo')
# print_name(surname = 'Puch') TypeError

def print_name_with_default (name, surname, alias = 'Sin alias'): # en este caso alias tienes un valor por defecto
    print(f'{name} {surname} {alias}')
    
print_name_with_default('Pablo', 'Puch', 'Poker21')
print_name_with_default('Pablo', 'Puch')



def print_text (*texts): # * el este caso le podemos pasar el numero de parametros que quieras
    for text in texts:
        print(text)
    
print_text('Hola','Pablo','Python')

def print_upper_text (*texts): # * el este caso le podemos pasar el numero de parametros que quieras
    for text in texts:
        print(text.upper())
    
print_upper_text('Hola','Pablo','Python')