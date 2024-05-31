### Higher Order Funtions ###

from functools import reduce


def sum_one (value):
    return value + 1

def sum_five (value):
    return value + 5



def sum_two_values_and_one(first_value, second_value):
    
    return sum_one(first_value + second_value)

print(sum_two_values_and_one(5, 2)) # 8



def sum_two_values_and_one(first_value, second_value, f_sum):
    
    return f_sum(first_value + second_value)

print(sum_two_values_and_one(5, 2, sum_one)) # 8
print(sum_two_values_and_one(5, 2, sum_five)) # 12



### Closures ### 

"""
    En Python, el cierre se crea anidando una función dentro de otra
    función encapsuladora y luego devolviendo la función interna.
"""


def add_ten(ten):
    def add(num):
        return num + ten
    return add

closure_result = add_ten(1)
print(closure_result(5))  # 6
print((add_ten(5))(1)) # 6


### Built-in Higher Order Functions ###

numbers = [2, 5, 10 ,21, 30]



# Map

"""
    Función incorporada que toma una función y un iterable como parámetros. 

"""

def multiply_two(number):
    return number *2

print(map(multiply_two, numbers))
print(list(map(multiply_two, numbers)))
print(list(map(lambda number: number * 2, numbers)))


# Filter

"""
    La función filter() llama a la función especificada que devuelve un valor 
    booleano para cada elemento del iterable (lista) especificado. Filtra los 
    elementos que satisfacen los criterios de filtrado.

"""


def filter_greater_ten(number):
    if number > 10:
        return True
    return False

print(list(filter(filter_greater_ten, numbers)))
print(list(filter(lambda number: number > 10, numbers)))



# Reduce

""" 
    Opera entre los valores que va recorriendo. Este no devuelve un iterable sino un valor unico

    [2, 5, 10 ,21, 30]
"""

def sum_two_values(first_value, second_value):
    print(first_value)
    print(second_value)
    return first_value + second_value


print(reduce(sum_two_values, numbers)) 