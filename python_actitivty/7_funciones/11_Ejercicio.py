'''
    11_Ejercicio
    El día juliano correspondiente a una fecha es un número entero que 
    indica los días que han transcurrido desde el 1 de enero del año indicado. 
    Queremos crear un programa principal que al introducir una fecha nos diga el 
    día juliano que corresponde. Para ello podemos hacer las siguientes subrutinas:

        LeerFecha: Nos permite leer por teclado una fecha (día, mes y año).
        DiasDelMes: Recibe un mes y un año y nos dice los días de ese mes en ese año.
        EsBisiesto: Recibe un año y nos dice si es bisiesto.
        Calcular_Dia_Juliano: recibe una fecha y nos devuelve el día juliano.
'''

def leerFecha():
    dias = int(input('Introducier un día: '))
    mes = int(input('Introducier un mes: '))
    año = int(input('Introducier un año: '))
    return dias,'/',mes,'/',año
    diasDelMes(mes,año)

def diasDelMes(mes,año):
    mes_31_dias = [1,3,5,7,8,10,12]
    mes_30_dias = [4,6,9,11]
    
    if mes in mes_31_dias:
        return 31
    elif mes in mes_30_dias:
        return 30
    elif mes == 2:
        if esbisiesto(año):
            return 29
        else:
            return 28

def esbisiesto(año):
    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
        return True
    else:
        return False

def calcularDiaJuliano(dias,mes,año):
    dias_totales = 0
    for m in range(1, mes):
        dias_totales += diasDelMes(m, año)
    dias_totales += dia
    return dias_totales

# Programa principal
dia, mes, año = leerFecha()
dia_juliano = calcularDiaJuliano(dia, mes, año)
print("El día juliano correspondiente a la fecha es:", dia_juliano)

