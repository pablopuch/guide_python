### Comprensión de listas ###

my_original_list = [35, 24, 62, 30, 30, 17]
print(my_original_list)

my_list = [i for i in range(7)]
print(my_list)

my_range = range(8)
print(my_list)

my_list = [i + 1 for i in range(8)]
print(my_list)

my_list = [i * 2 for i in range(8)]
print(my_list)

my_list = [i + i for i in range(8)]
print(my_list)

def sum_five(number):
    return number + 5

my_list = [sum_five(i) for i in range(8)]
print(my_list)
