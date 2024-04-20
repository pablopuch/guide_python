'''
    20_Ejercicio
    Diseñar un algoritmo que nos diga el dinero que tenemos (en euros y céntimos) 
    después de pedirnos cuántas monedas tenemos (de 2€, 1€, 50 céntimos, 20 céntimos o 10 céntimos)
'''
euro_row = int(input('Monedas de 2€: '))
euro_one = int(input('Monedas de 1€: '))
cents_fifty = int(input('Monedas de 50 céntimos: '))
cents_twenty = int(input('Monedas de 20 céntimos: '))
cents_ten = int(input('Monedas de 10 céntimos: '))

def cal_euro(euro_row, euro_one, cents_fifty, cents_twenty, cents_ten):
    euros = euro_row*2 + euro_one*1
    
    # cents = (cents_fifty*50 + cents_twenty*20 + cents_ten*10)/100
      cents =     
    
    return print(f'Tienes {euros}€ y {cents} céntimos')
    
cal_euro(euro_row, euro_one, cents_fifty, cents_twenty, cents_ten)