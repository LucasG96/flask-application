class Conta:
    # Construtor
    def __init__(self, numero, titular, saldo, limite):
        print("Iniciei o construtor... {}".format(self))
        # __ (dois undeline) mudam a visibilidade do atributo para privado
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    # Métodos Getters e Setters
    def getTitular(self):
        return self.__titular

    def setTitular(self, valor):
        self.__titular = valor

    # Métodos da clase (Métodos estáticos)
    @staticmethod
    def codigos_banco():
        return {'BB': '001', 'Caixa': '104', 'Bradesco': '237'}
    
    @staticmethod
    def codigo_banco():
        return "001"

    # Métodos da classe 
    def extrato(self):
        print("Saldo {} do titular {}".format(self.__saldo, self.__titular))

    # Método privado
    def __podeSacar(self, valor):
        return valor <= self.__saldo + self.__limite

    def sacar(self, valor):
        if(self.__podeSacar(valor)):
            self.__saldo -= valor
            print("Sacou {} sobrou {}".format(valor,self.__saldo))
        else:
            print("Você não possui limite suficiente para sacar R${}.".format(valor))

    def depositar(self, valor):
        self.__saldo += valor
        print("Depositou {} ficou {}".format(valor, self.__saldo))

    def transferir(self, contaFavorecido, valor):
        contaFavorecido.__saldo += valor
        self.__saldo -= valor