'''
    10_Ejercicio
    Un alumno desea saber cual será su calificación final en la materia de Algoritmos.
    Dicha calificación se compone de los siguientes porcentajes:

        55% del promedio de sus tres calificaciones parciales.
        30% de la calificación del examen final.
        15% de la calificación de un trabajo final.
'''

parcial_1 = float(input('Nota del 1º parcial: '))
parcial_2 = float(input('Nota del 2º parcial: '))
parcial_3 = float(input('Nota del 3º parcial: '))
exam_final = float(input('Nota del examen final: '))
trabajo_final = float(input('Nota del trabajo final: '))

promedio = (parcial_1 + parcial_2 + parcial_3) / 3
nota_final = (55*promedio + 30*exam_final + 15*trabajo_final)/100

# %.2f lo que va hacer es devolver el valor pero con dos decicmales 
print('Nota final de la materia %.2f' % nota_final)