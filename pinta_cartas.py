'''
Clase que pinta el numero de cartas, se recibe una lista de diccionarios, [nombre:dos-picas, valor:2]

'''
class PintaCartas():

    def oculta_primera_carta(self, cartas):
        """ muestra todas las cartas excepto la primera en el mazo las cartas vienen con el formato lista de diccionarios
        'diez-diamante': 10, 'ocho-corazon': 8, 'cinco-trebol': 5, 'rey-pica': 10
        se extrae la llave nombre y se separa por '-' se pinta la carta.
        
        ***************   ***************   ***************  ***************           
        ***************   *  8 corazon  *   *   5 trebol  *  *   rey pica  *
        ***************   ***************   ***************  ***************
        """
        inicial = True
        print('*'.ljust(18,'*'))
        print('*'.ljust(18,'*'))
        print('*'.ljust(18,'*') + '\n')

        for c in cartas:
            if inicial:
                inicial = False
            else:
                nombre = c.get('nombre')
                lista = nombre.split('-')
                self._cuadros(lista)
        

    def pinta_todo(self, cartas):
        """ muestra todas las cartas del mazo las cartas vienen con el formato 
        'diez-diamante': 10, 'ocho-corazon': 8, 'cinco-trebol': 5, 'rey-pica': 10
        se extrae la llave nombre y se separa por '-' se pinta la carta.
        
        ***************   ***************   ***************  ***************           
        * 10 diamante *   * 8 corazon  *    *  5 trebol   *  *  rey pica   *
        ***************   ***************   ***************  ***************
        """
        for c in cartas:
            nombre = c.get('nombre')
            lista = nombre.split('-')
            self._cuadros(lista)
        

    def resumen(self, cartas, jugador):
        """ se muestra el total de cartas y el total sumado de las cartas
        ****************              
        *  Jugador 1   *   
        *  10 cartas   *
        *    suman     *
        *              *
        *      21      *
        ****************         
        """
        num = len(cartas)
        total = 0

        for c in cartas:
            total += c.get('valor')
        
        print(f'*'.ljust(17,'*'))
        print(f'*    {jugador}'.ljust(16,' ') + '*')
        print(f'*    {num} cartas'.ljust(16,' ') + '*')
        print(f'*     suman'.ljust(16,' ') + '*')
        print(f'*       {total}'.ljust(16,' ') + '*')
        print(f'*'.ljust(17,'*'))

    def _cuadros(self, par):
        """ pinta las cartas, se recibe una lista como par [0]--> numero en letras  [1]--> el tipo """
        try:
            num_word = par[0]
            nombre = par[1]
            n = 0
            
            if num_word == 'dos':
                n = 2
            elif num_word == 'tres':
                n =3
            if num_word == 'cuatro':
                n = 4
            elif num_word == 'cinco':
                n =5
            if num_word == 'seis':
                n = 6
            elif num_word == 'siete':
                n =7
            if num_word == 'ocho':
                n = 8
            elif num_word == 'nueve':
                n =9
            else:
                n = num_word

            # pinta el cuadro
            print('*'.ljust(18,'*'))
            print(f'* {n} {nombre}'.ljust(17,' ') + '*')    
            print('*'.ljust(18,'*') + '\n')
        except:
            print('Algo salio mal!')
        


a = PintaCartas()
l = [{'nombre':'dos-picas', 'valor':2},{'nombre':'cinco-corazon', 'valor':5}]
a.pinta_todo(l)
print('\n')
a.oculta_primera_carta(l)
a.resumen(l, 'Jugador1')