
class Conta:
    def __init__(self, numero, titular, saldo, limite = 1000.0):
        print("Objeto Construido")
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("O saldo do titular {} é de {}".format(self.__titular, self.__saldo))

    def depositar(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel = self.__saldo +self.limite
        return valor_a_sacar <= valor_disponivel

    def sacar(self, valor):
        if (self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print('O valor {} é maior que o limite'.format(valor))

    def transferir(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def numero(self):
        return self.__numero

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, valor):
        self.__limite = valor

    @staticmethod
    def codigo_banco():
        return "001"

    @staticmethod
    def codigos_bancos():
        return {'BB': '001', 'ST': '002', 'BR': '003'}