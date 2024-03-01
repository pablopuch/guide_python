'''
    03_Ejercicio
    Se quiere realizar un programa que lea por teclado las 5 notas obtenidas por un alumno 
    (comprendidas entre 0 y 10). A continuación debe mostrar todas las notas, la nota media, 
    la nota más alta que ha sacado y la menor.
'''

list_note = []

for _ in range(5):
    note = int(input('Pon una nota del 0 a 10: '))
    if note < 0 or note > 10:
        print("La nota no es válida")
    else:
        list_note.append(note)
        
print(list_note)
print('Media: ', sum(list_note)/len(list_note))
print('Nota más alta: ', max(list_note))
print('Nota más baja: ', min(list_note))