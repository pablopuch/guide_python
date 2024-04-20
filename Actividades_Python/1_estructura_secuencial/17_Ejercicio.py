'''
    17_Ejercicio
    Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS segundos. 
    El tiempo de viaje hasta llegar a otra ciudad B es de T segundos. 
    Escribir un algoritmo que determine la hora de llegada a la ciudad B.
'''

HH_start = int(input('Hora de salida: '))
MM_start = int(input('Minutos de salida: '))
SS_start = int(input('Segundos de salida: '))
SS_travel = int(input('Tiempo del viaje en Segundos: '))

seg_start = HH_start*3600 + MM_start*60 + SS_start
time_total = seg_start + SS_travel;

hora_final = time_total // 3600;
mini_final = (time_total % 3600) // 60;
seg_final = (time_total % 3600) % 60;

print('Hora de llegada: ',hora_final,':',mini_final,':',seg_final)
