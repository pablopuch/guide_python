'''
    16_Ejercicio
    Dos vehículos viajan a diferentes velocidades (v1 y v2) y están distanciados 
    por una distancia d. El que está detrás viaja a una velocidad mayor. Se pide 
    hacer un algoritmo para ingresar la distancia entre los dos vehículos (km) y 
    sus respectivas velocidades (km/h) y con esto determinar y mostrar en qué 
    tiempo (minutos) alcanzará el vehículo más rápido al otro
'''

v1 = int(input('Velocidad del primer coche: '))
v2 = int(input('Velocidad del segundo coche: '))
d = int(input('distancia a la que se encuntra: '))



def time_cars(v1,v2,d):
    
    if (v2 >= v1):

        dif_velocidad = abs(v1-v2)
        time_hour = dif_velocidad / d
        tiempo = time_hour * 60
        return int(f'El tiempo que tardara es de {tiempo}')
        
    else: 
        return('La velocidad del segundo coche tiene que ser más alta.')
    
    
print(time_cars(v1, v2, d))
