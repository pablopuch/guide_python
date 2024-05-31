### Lambdas ###

""" ¿Que és?

    Es una fucnión anonima escrita en una sola linea, que puede resivir 
    cualquier número de parámetros y conlleva un return implícito.
"""

sum_two_values = lambda first_value, second_value: first_value + second_value

print(sum_two_values(3, 5))


multi_values = lambda first_value, second_value: first_value * second_value

print(multi_values(3, 5))



def sum_three_values(value):
    return lambda first_value, second_value: first_value + second_value + value

print(sum_three_values(5)(2, 4))    