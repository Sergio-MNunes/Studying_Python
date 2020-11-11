

class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("construindo objeto ... {}".format(self))

        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def deposito(self, valor):
        self.__saldo += valor

    def saque(self, valor):
        total_disponivel = self.__saldo + self.__limite
        if valor > total_disponivel:
            cod_retorno = 1
            self.__mensagens_saida_saque(cod_retorno, self.__saldo, self.__limite)

        elif total_disponivel >= valor > self.__saldo:
            self.__limite -= abs(self.__saldo - valor)
            self.__saldo -= valor
            cod_retorno = 0
            self.__mensagens_saida_saque(cod_retorno, self.__saldo, self.__limite)

        else:
            self.__saldo -= valor
            cod_retorno = 0
            self.__mensagens_saida_saque(cod_retorno, self.__saldo, self.__limite)

    def extrato(self):
        print("Olá {}, o seu saldo é de {}".format(self.titular, self.__saldo))

    def __mensagens_saida_saque(self, cod_retorno, __saldo, __limite):
        if cod_retorno == 0:
            print("Saque realizado com sucesso.")
            print("Saldo atual: {}.".format(self.__saldo))
            print("Limite disponível: {}".format(self.__limite))
        elif cod_retorno == 1:
            print("Não foi possível realizar o saque.")
            print("Saldo: {} ".format(self.__saldo))
            print("Limite: {} ".format(self.__limite))
        else:
            print("Falha ao realizar operação. Contate suporte técnico. ")

    @property
    def saldo(self):
        return self.__saldo

    @property
    def numero(self):
        return self.__numero

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, novo_limite):
        self.__limite = novo_limite

    @staticmethod
    def cod_banco():
        return "0033"
