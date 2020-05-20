import figuras
import valores
import random
import pinta_cartas
'''
Clase que se encarga de manejar todo lo relacionado con las cartas del juego black-jack
'''
class Cartas:


    def __init__(self):
        self.mazo = []
        self.pintor = pinta_cartas.PintaCartas()
        """ siempre se crea un mazo de cartas cuando se inicia la clase 
            el mazo es una lista de pares de valores dict """
        for f in figuras.Figuras.__members__.items():
            for v in valores.Valores.__members__.items():
                carta = {}
                # si el valor es mayor a 10 el valor sera siempre 10
                if v[1].value >= 10:
                    carta[ 'name' ] =  v[1].name + '-' + f[1].name
                    carta[ 'value' ] =  10 
                else:
                    carta[ 'name' ] =  v[1].name + '-' + f[1].name
                    carta[ 'value' ] =  v[1].value
                self.mazo.append(carta)            


    def get_cards(self, number_of_cards, is_dealer):
        """ Regresa el numero de cartas indicado en forma aleatoria, todo en tuplas """
        salida = []
        for i in range(number_of_cards):
            inx = random.randint(0, len(self.mazo)-1)
            carta_n = self.mazo.pop(inx)
            # si la carta es un as el jugador debe elejir si desea 1 o 10 como valor
            if carta_n.get('name')[0:3] == 'as1' and not is_dealer:
                valor_as = self._choose_card_player(carta_n.get('name'), carta_n.get('value'))
            elif carta_n.get('name')[0:3] == 'as1' and is_dealer:
                # regresa 1 o 10
                valor_as = random.randrange(1,19,9)
           
            salida.append(carta_n)
        return salida


    def _choose_card_player(self, name_carta, value_carta):
        tempo = [{'name': name_carta, 'value':value_carta}]
        # muestra la carta as al jugador
        self.pintor.pinta_carta_as(tempo)
        valor_as = -1
        # pide el valor
        while valor_as != 1 and valor_as != 10:
            try:
                valor_as = int(input('que valor elije para su as, elija solo 1 o 10: '))
            except:
                pass
        return valor_as