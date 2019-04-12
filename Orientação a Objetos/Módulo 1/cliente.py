class Cliente:
    def __init__(self, valor):
        self.__nome = valor

    # Funciona como se fosse o setter, funciona chamando o atributo assim: cliente.nome
    @property
    def nome(self):
        return self.__nome.title()

    # Funciona como se fosse o getter, funciona chamando o atributo assim: cliente.nome = "Seu Nome"
    @nome.setter
    def nome(self, valor):
        self.__nome = valor