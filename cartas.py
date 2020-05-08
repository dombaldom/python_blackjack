import figuras
import valores
import random
'''
Clase que se encarga de manejar todo lo relacionado con las cartas del juego black-jack
'''
class Cartas:

    mazo = []

    def __init__(self):
        """ siempre se crea un mazo de cartas cuando se inicia la clase 
            el mazo es una lista de pares de valores dict """
        for f in figuras.Figuras.__members__.items():
            for v in valores.Valores.__members__.items():
                carta = {}
                # si el valor es mayor a 10 el valor sera siempre 10
                if v[1].value >= 10:
                    carta[ v[1].name + '-' + f[1].name ] =  10 
                else:
                    carta[ v[1].name + '-' + f[1].name ] =  v[1].value
                self.mazo.append(carta)            


    def get_cards(self, number_of_cards):
        """ Regresa el numero de cartas indicado en forma aleatoria, todo en tuplas """
        salida = []
        for i in range(number_of_cards):
            inx = random.randint(0, len(self.mazo)-1)
            salida.append(self.mazo.pop(inx))
        return salida


# 
