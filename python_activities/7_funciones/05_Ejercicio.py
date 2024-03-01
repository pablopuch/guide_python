'''
    05_Ejercicio
    Crea una función “calcularMaxMin” que recibe una lista con valores numéricos y 
    devuelve el valor máximo y el mínimo. Crea un programa que pida números por teclado y
    muestre el máximo y el mínimo, utilizando la función anterior.
'''

def calcularMaxMin():
    list = []
    
    for _ in range(4):
        a=int(input("Ingrese numero:"))
        list.append(a)
    
    print('#####################################')
    print('Maximo',max(list),'\nMinimo',min(list))

calcularMaxMin()