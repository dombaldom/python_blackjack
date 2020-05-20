import cartas
import dealer
import jugador
import random


'''
Clase que controla el juego
'''
class ControlJuego():

    def __init__(self):
        """ crea una cuenta de banco por jugador y un pinta cartas """
        self.dealer_player = dealer.Dealer(5000)
        self.jugadores = []
        self.otro = 'S'
        self.errorEntrada = False
        self.baraja = []


    def nuevo_juego(self):
        """ cada que se inicia un juego se crea un mazo nuevo y se crea lista de jugadores """
        self.baraja = cartas.Cartas()
        self.__agrega_jugadores()

        # cada jugador hace su apuesta, si la funcion regresa 0 el jugador no registra apuesta y queda fuera del juego
        for j in self.jugadores:
            # se pide una apuesta al jugador
            apuesta = j.paga_apuesta(self._pedir_apuesta(j))
            if apuesta != 0:
                self.dealer_player.registra_apuesta(j.nombre, apuesta) 
            else:
                print(f'Jugador {j.nombre} rechazado del juego')
                self.jugadores.remove(j)
        
        # reparto inicial 2 cartas a jugadors
        for d in self.jugadores:
            d.set_cards(self.baraja.get_cards(2, False))
        # reparto carta a dealer
        self.dealer_player.set_cards(self.baraja.get_cards(1, True))

        # reparto 1 carta a jugadores que asi lo deseen en esta segunda ronda
        for d in self.jugadores:
            while self.__pedir_cartas(d.nombre):
                d.set_cards(self.baraja.get_cards(1, False))

        # reparto aleatorio de cartas para dealer segunda ronda (deberia funcionar con algoritmo para elegir mejor opcion.)
        num_cartas_dealer = random.randint(0, 4)
        for ncd in range(0,num_cartas_dealer):
            self.dealer_player.set_cards(self.baraja.get_cards(1, True))
        
        # finaliza juego
        for d in self.jugadores:
            self.dealer_player.look_for_winner(d.cartas_jugador, d.nombre)
        
        print('\n+++++++++++++++++++++++++++++Resumen del dealer\n')
        self.dealer_player.get_resumen_dealer()

    def __agrega_jugadores(self):
        """ agrega jugadores, es necesario un nombre y una cantidad para jugar """
        # set de jugadores
        self.jugadores = []
        while self.otro == 'S':
            jug = input('Agregue el nombre del jugador: ')
            cantidad = 0
            try:
                cantidad = int(input('Agregue una cantidad de dinero para su cuenta: '))
                self.errorEntrada = False
                                 
            except:
                self.errorEntrada = True
                print('Jugador no registrado, necesita agregar una cantidad numerica positiva: ')

            if not self.errorEntrada: 
                self.errorEntrada = False
                # guarda los jugadores en un diccionario
                j = jugador.Jugador(cantidad, jug)
                self.jugadores.append(j)
                self.otro = input('Desea registrar otro jugador entre S para si cualquier otro caracter no? ').capitalize() 

        
    def __pedir_cartas(self, jugador):
        """ pregunta al usuario si desea una carta """
        continua = True

        while continua:
            respuesta = input(f'{jugador} desea otra carta (y/n)?').upper()
            if respuesta == 'Y':
                return True
            elif respuesta == 'N':
                return False
            else:
                print('Solo seleccione s o n.')


    def _pedir_apuesta(self, jugador):
        """ pregunta al usuario la cantidad de la apuesta. """
        continua = True
        while continua:
            try:
                respuesta = int(input(f'{jugador.nombre} que apuesta deseas hacer: ').upper())
                continua = False
            except :
                print('Escriba solo numeros')
        return respuesta

'''''
Inicia juego
'''''
continua = 'S'

while continua:
    continua = input(f'{jugador} desea seguir jugando (y/n)?').upper()
    if continua == 'Y':
        c = ControlJuego()
        c.nuevo_juego()    
    elif continua != 'N':
        print('Solo seleccione s o n.')

 
