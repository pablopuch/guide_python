'''
    13_Ejercicio
    Escribe un programa que pida una fecha (día, mes y año) y diga si es correcta..
'''
day = int(input('Día:'))
month = int(input('Mes:'))
year = int(input('Año:'))

dia_del_mes = 0 


if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    dia_del_mes = 31
elif month == 4 or month == 6 or month == 9 or month == 11:
    dia_del_mes = 30
elif month == 2:
    if (year % 4 == 0 and not (year % 100 == 0)) or year % 400 == 0:
        dia_del_mes = 29
    else:
        dia_del_mes = 28
elif day < 0 or day > dia_del_mes:
    print('Fecha no correcta')
else:
    print('Fecha correcta')