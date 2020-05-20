import cuenta
import pinta_cartas
'''
lleva el control del juego del dealer, guarda sus cartas, realiza los tiros y contiene una cuenta de dinero
'''
class Dealer():


    def __init__(self, saldo_juego, nombre='Dealer'):
        """ crea un jugador, le asigna un nombre y crea una cuenta con $"""
        self.nombre = nombre
        self.cuenta = cuenta.Cuenta(self.nombre, saldo_juego)
        self.pintor = pinta_cartas.PintaCartas()

        self.apuestas_jugadores = {}
        self.cartas_dealer = []
        self.sum_dealer = 0


    def _paga_apuesta(self, ganador):
        """ el dealer paga la apuesta de la partida a cada jugador ganador. """
        # si no hay dinero para pagar la apuesta, se pide a la casa agregar mas dinero
        if self.cuenta.retiro(self.apuestas_jugadores[ganador]):
            print(f'{ganador} ganaste ${self.apuestas_jugadores[ganador]}')
            return self.apuestas_jugadores[ganador]
        else:
            # sobregiro, pide al dealer agregar mas dinero a la cuenta
            while self.cuenta.saldo <= self.apuestas_jugadores[ganador]:
                try :
                    deposito = int(input('No hay suficiente saldo para pagar! que cantidad deseas abonar a la cuenta de la casa?: '))
                    self.cuenta.deposito(deposito)
                except :
                    print('Elija solo numeros')

            # una vez que hay saldo en la cuenta se paga y se borra apuestas por pagar
            self.apuestas_jugadores = {}
            return self.cuenta.retiro(self.apuestas_jugadores[ganador])


    def registra_apuesta(self, jugador, cantidad):
        """ Registra las apuestas de los jugadores, una vez terminado el juego, el dinero se abona o se regresa + ganancias al ganador """
        # se asegura que el jugador no exista
        try:
            self.apuestas_jugadores[jugador]
            print(f'Ya existe un jugador  con el nombre {jugador}, cambialo para poder jugar')
        except KeyError:
            self.apuestas_jugadores[jugador] = cantidad
            
        
        
        

    def regresa_jugadores(self):
        """ regresa en una lista los nombres de los jugadores """
        return list(self.apuestas_jugadores.keys())


    def look_for_winner(self, cartas, jugador):
        """ checa estatus del juego, si las cartas suman 21 se para el juego y se pagan apuestas, si suma mas de 21 se toma dinero de la cuenta del perdedor"""
        sum = 0
        for carta in cartas:
            sum += carta['value']
        # verifica estatus del juego, si es 21 gana, si pasa 21 pierde, si ninguno de los 2 anteriores, se mantine.
        if sum == 21 or (sum > self.sum_dealer and sum < 21) :
            self._paga_apuesta(jugador)
            self.pintor.resumen(cartas,jugador)
            self.pintor.paint_winner(jugador)
            return 'winner'
        elif sum > 21 or sum < self.sum_dealer :
            self.apuestas_jugadores.pop(jugador, None)
            self.pintor.resumen(cartas,jugador)
            self.pintor.paint_loser(jugador)  
            return 'loser'
        else:
            self.pintor.paint_tie(jugador)
            self.pintor.resumen(cartas,jugador)
            return 'tie'
            
    def set_cards(self, cartas_nuevas):
        """ Agrega las cartas al mazo del jugador, las cartas"""
        sum = 0
        for i in cartas_nuevas:
            sum += i['value']
            self.cartas_dealer.append(i)
        self.sum_dealer = sum
        self.pintor.pinta_todo(self.cartas_dealer, self.nombre)

    def get_resumen_dealer(self):
        self.pintor.resumen(self.cartas_dealer, 'dealer')
