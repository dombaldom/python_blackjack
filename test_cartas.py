import unittest
import cartas
import cuenta
'''
Clase que prueba la clase cards

'''
class TestCartas(unittest.TestCase):

    def test_crea_mazo(self):
        """ prueba que se genero un mazo de cartas 
            el mazo viene en una lista de diccionarios, con par 
            nombre:valor, son 72 cartas, se prueban los valores
            'diez-diamante': 10
            'ocho-corazon': 8
            'cinco-trebol': 5
            'rey-pica': 10
        """
        #mazo
        c = cartas.Cartas()
        self.assertEqual(len(c.mazo), 52, 'crear mazo')


    def test_get_cartas(self):
        """ Regresa #numero de cartas en una lista y las elimina del mazo """
        # para una carta
        c = cartas.Cartas()
        size = len(c.mazo)
        carta = c.get_cards(1)
        self.assertEqual(size-1, len(c.mazo))
        #para dos cartas
        size = len(c.mazo)
        carta = c.get_cards(2)
        self.assertEqual(size-2, len(c.mazo))


    def test_cuenta_creacion(self):
        """ Se crea una cuenta con saldo y nombre de cliente """
        c = cuenta.Cuenta('Jose Domingo Balderas', 1000)
        # realiza prueba de saldo y nombre
        self.assertEqual(c.cliente, 'Jose Domingo Balderas')
        self.assertEqual(c.saldo, 1000, f'saldo error {c.saldo}')

    def test_income(self):
        """ Se ingresa saldo a la cuenta """
        c = cuenta.Cuenta("Domingo")

        # saldo 0
        self.assertEqual(c.saldo, 0.0)

        # saldo 525.05  
        c.deposito(525.05)
        self.assertEqual(c.saldo, 525.05)

    def test_outcome(self):
        """ Se retira de la cuenta """
        c = cuenta.Cuenta("Domingo")

        # saldo 0
        self.assertEqual(c.saldo, 0.0)

        # retiro 1
        c.retiro(1)
        self.assertEqual(c.saldo, 0)

        # retiro 10  
        c.deposito(600)
        self.assertEqual(c.saldo, 600)
        c.retiro(100)
        self.assertEqual(c.saldo, 500)
    

if __name__ == '__main__':
    unittest.main()