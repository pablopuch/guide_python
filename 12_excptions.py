### Excepciones ###
 
numberOne = 5
numberTwo = 1

numberTwo = "1"

#try except
try: 
    print(numberOne + numberTwo)
    print('No se ha produciodo un error')
except:
    print('Se ha producido un error')
    
    
    
#try except else finally
try: 
    print(numberOne + numberTwo)
    print('No se ha produciodo un error')
except:
    print('Se ha producido un error')
else: # opcional
    # esto se ejecuta si no se produce una excpción
    print('La ejecucion continua')
finally: # opcional
    # se ejecuta siempre
    print('La ejecución continúa')
    

########### Captura por tipo ############

print(numberOne + numberTwo)

try: 
    print(numberOne + numberTwo)
    print('No se ha produciodo un error')
except ValueError:
    # se ejecuta si se produce una exepción
    print('Se ha producido un ValueError')
except TypeError:
    # se ejecuta si se produce una exepción
    print('Se ha producido un TypeError')
    
    
    
# Captura de la información de la excepción
try: 
    print(numberOne + numberTwo)
    print('No se ha produciodo un error')
except ValueError as e:
    print(e)
except Exception as e:
    print(e)
