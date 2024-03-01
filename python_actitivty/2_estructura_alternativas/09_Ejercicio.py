'''
    09_Ejercicio
    Algoritmo que pida tres números y los muestre ordenados (de mayor a menor).
'''

a = float(input('1º numero: '))
b = float(input('2º numero: '))
c = float(input('3º numero: '))
arr = [a,b,c]


n = len(arr) # tamaño del arr

# Iterar a través de cada elemento del arr
for i in range(n):
    for j in range(0, n - i -1): # El valor de n - i - 1 representa la posición límite en cada pasada del bucle.
        if arr[j] < arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print(arr)

'''-----------------------------------------------------------------------------'''

# if(a > b and a > c):
#     arr.insert(0,a)
#     if(b > c):
#         arr.insert(1,b)
#         arr.insert(2,c)     
#     else:
#         arr.insert(1,c)
#         arr.insert(2,b)
# elif(a < b and a < c):
#     arr.insert(2,a)
#     if(b > c):
#         arr.insert(0,b)
#         arr.insert(1,c)     
#     else:
#         arr.insert(0,c)
#         arr.insert(1,b)
# elif(a > b and a < c):
#     arr.insert(1,a)
#     if(b < c):
#         arr.insert(2,b)
#         arr.insert(0,c)
#     else:
#         arr.insert(2,c)
#         arr.insert(0,b)
# else:
#     arr.insert(1,a)
#     if(b < c):
#         arr.insert(2,b)
#         arr.insert(0,c)
#     else:
#         arr.insert(2,c)
#         arr.insert(0,b)
        
# print(arr)
   
    
'''-----------------------------------------------------------------------------'''

# num1 = float(input('1º numero: '))
# num2 = float(input('2º numero: '))
# num3 = float(input('3º numero: '))

# # el metodo sort() odena un array sin la necesidad de crear uno
# # el reverse=True ordenara en sentido desc.
# arr = [num1,num2,num3]
# arr.sort(reverse=True)
# print(arr)