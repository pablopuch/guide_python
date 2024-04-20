### Clases ### 

class MyEmptyPerson:
    pass

print(MyEmptyPerson)
print(MyEmptyPerson())

class Person:
    def __init__(self, name, surname, alias = 'Sin alias'): # self permite adjuntar parametros a una clase
        self.full_name = f'{name} {surname} ({alias})' # porpiedad publica
        self.__name = name # porpiedad privada
    
    
    def get_name (self):
        return  self.__name
    

    def walk(self):
        print(f'{self.full_name} está caminado')
    
my_person = Person('Pablo', 'Puch')
print(my_person.full_name)
print(my_person.get_name())
my_person.walk()

my_other_person = Person('pablo', 'puch', 'poker21')
print(my_other_person.full_name)
my_other_person.walk()
my_other_person.full_name = 'Pablo Puch (El crack)'

