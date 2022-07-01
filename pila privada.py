class Pila:
    def __init__(self):
        self.__listaPila = []

objetoPila = Pila()
print(len(objetoPila.__listaPila))
#uando cualquier componente de la clase tiene
#  un nombre que comienza con dos guiones bajos (__), 
# se vuelve privado - esto significa 
# que solo se puede acceder desde la clase.
#No puedes verlo desde el mundo exterior. Así es 
# como Python implementa el concepto de encapsulación.