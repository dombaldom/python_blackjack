import cuenta
import pinta_cartas
'''
lleva el control del juego de este jugador, guarda sus cartas, realiza los tiros y contiene una cuenta de dinero
'''
class Jugador:
    
    def __init__(self, saldo_juego, nombre):
        """ crea un jugador, le asigna un nombre y crea una cuenta con $"""
        self.nombre = nombre
        self.cuenta = cuenta.Cuenta(self.nombre, saldo_juego)
        self.pintor = pinta_cartas.PintaCartas()
        self.cartas_jugador = []

    def paga_apuesta(self, pago_apuesta):
        """ el jugador paga la apuesta de la partida, si ya no desea jugar regresa apuesta $0 y con esto termina el juego. """
        # si no cuenta con fondos se rechaza la apuesta
        if self.cuenta.saldo == 0:
            print('Sin saldo, agregue mas dinero a su monedero para poder jugar!')
            return 0
        # si el jugador apuesta mas que su saldo, se pide que baje la apuesta o que se retire del juego
        if self.cuenta.retiro(pago_apuesta):
            print(f'Jugador {self.cuenta.cliente} apuesta {pago_apuesta}')
            return pago_apuesta
        else:
            # sobregiro, pide al jugador rebajar su apuesta o retirarse apostando $0
            while self.cuenta.saldo <= pago_apuesta and pago_apuesta != 0:
                try :
                    pago_apuesta = int(input('Esta sobregirado, rebaje su apuesta o apueste 0 para salir: '))
                except :
                    print('Elija solo numeros')

            return pago_apuesta


    def set_cards(self, cartas_nuevas):
        """ Agrega las cartas al mazo del jugador, las cartas se agregan una a una"""
        for i in cartas_nuevas:
            self.cartas_jugador.append(i)
        self.pintor.pinta_todo(self.cartas_jugador, self.nombre)
    