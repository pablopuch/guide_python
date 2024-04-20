'''
    03_Ejercicio
    Algoritmo que pida números hasta que se introduzca un cero. 
    Debe imprimir la suma y la media de todos los números introducidos.
'''

suma = 0
cont = 0

num = int(input('Numero (0 para salir):'))
while num != 0:
    suma+=num
    cont+=1
    num=int(input("Numero (0 para salir):"))

# si cont = 0 no puedo realizar la división

if cont > 0:
    media = suma / cont
else:
    media = 0

print('Suma:', suma)
print('Media:', media)



'''--------------------------------------------------------------------'''



def suma_y_media():
    suma = 0
    cont = 0
    
    while True:
        num = int(input('Introducir un numero (0 para salir):'))
        
        if num == 0:
            break
        
        suma += num
        cont += 1
    
    if cont == 0:
        print('No se introdujeron números')
    else:
        media = suma / cont
        print('Suma:', suma)
        print('Media:', media)
            
suma_y_media()

    