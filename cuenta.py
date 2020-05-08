'''
Clase que se encarga de la administracion de cuentas
contiene entradas, salidas y balance

'''
class Cuenta():
    cliente = ''
    saldo = 0.0

    def __init__(self, nombre, saldo = 0.0):
        """ Crea un cuenta para un cliente con su nombre """
        self.cliente = nombre
        self.saldo = saldo

    def deposito(self, cantidad):
        """ Agrega un deposito a la cuenta del cliente """
        self.saldo += cantidad
        print(f'se deposito ${cantidad} a la cuenta, el saldo actual es ${self.saldo}')

    def retiro(self, cantidad):
        """ Retira dinero de la cuenta, si es que este no sobregira """
        if cantidad > self.saldo:
            print('Sobregirado!')
        else:
            self.saldo -= cantidad
            print(f'Retiro de ${cantidad} realizado con exito, saldo actual ${self.saldo}')

    def estado_cuenta(self):
        """ imprime el saldo y nombre del cliente """
        print(f'El saldo de la cuenta de {self.cliente} es de ${self.saldo}')