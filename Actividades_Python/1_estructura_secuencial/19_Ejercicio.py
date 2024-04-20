'''
    19_Ejercicio
    Escribir un algoritmo para calcular la nota final de un estudiante, 
    considerando que por cada respuesta correcta se suman 5 puntos, 
    por una incorrecta se resta 1 y por respuestas en blanco no se suma ni se resta. 
    Imprime el resultado obtenido por el estudiante
'''

correct = int(input('Numero de preguntas correctas: '))
incorrect = int(input('Numero de preguntas incorrectas: '))


def cal_note(correct, incorrect):
    points = correct * 5 - incorrect * 1
    return print(f'La puntuación del estudiante es {points} puntos')

cal_note(correct, incorrect)


'''
    En esta ejercicio yo no tengo encuenta el numero de preguntas en blanco, ya que no tienen ningun valor.
    Tambien no tengo encuenta el numero de preguntas, ya que concidero que no es relevante para el resultado,
    en cualquier caso se puede sacar sumando el numero de preguntas Correctas, Incorrectas y en blanco.
'''