'''
    12_Ejercicio
    Pide al usuario dos pares de números x1, y1 y x2, y2, 
    que representen dos puntos en el plano. Calcula y muestra la distancia entre ellos
'''

# Solicitar al usuario los primeros coordenadas
x1 = int(input("Ingrese la coordenada x del primer punto: "))
y1 = int(input("Ingrese la coordenada y del primer punto: "))

# Solicitar al usuario los segundos coordenadas
x2 = int(input("Ingrese la coordenada x del segundo punto: "))
y2 = int(input("Ingrese la coordenada y del segundo punto: "))

distX = (x2 - x1)
distY  = (y2 - y1)

dist = (distX**2 + distY**2)**0.5

print(f'La distarcia entre los puentos {x1,y1} y {x2,y2} es de {dist}')