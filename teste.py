
def cria_conta(numero, nome, saldo, limite):
    conta = {"numero": numero, "nome": nome, "saldo": saldo, "limite": limite}
    return conta

def deposita(conta, valor):
    conta["saldo"] += valor

def saca(conta, valor):
    conta["saldo"] -= valor

def extrato(conta):
    print("O saldo é: {}".format(conta["saldo"]))


class Data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano


    def formatada(self):
        print('{}/{}/{}'.format(self.dia, self.mes, self.ano))
