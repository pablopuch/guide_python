'''
    20_Ejercicio
    Diseñar un algoritmo que nos diga el dinero que tenemos (en euros y céntimos) 
    después de pedirnos cuántas monedas tenemos (de 2€, 1€, 50 céntimos, 20 céntimos o 10 céntimos)
'''
euro_two = int(input('Monedas de 2€: '))
euro_one = int(input('Monedas de 1€: '))
cents_fifty = int(input('Monedas de 50 céntimos: '))
cents_twenty = int(input('Monedas de 20 céntimos: '))
cents_ten = int(input('Monedas de 10 céntimos: '))

total = (euro_one * 1 + euro_two * 2 + cents_fifty * 0.50 + cents_twenty * 0.20 + cents_ten * 0.10)

euros = int(total)

cents = int((total - euros) * 100)


print(f"Tienes {euros} euros y {cents} céntimos.")
