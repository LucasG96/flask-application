class Programa:
    def __init__(self, nome, ano):
        self.__nome = nome
        self.ano = ano
        self.__likes = 0

    @property
    def nome(self):
        return self.__nome.title()

    @nome.setter
    def nome(self, valor):
        self.__nome = valor

    def dar_like(self):
        self.__likes += 1

    @property
    def likes(self):
        return self.__likes

    # Imprime o objeto
    def __str__(self):
        return '{} - {} - {} Likes'.format(self.nome, self.ano, self.likes)

# Define uma classe com herança da classe Programa
class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        # Chama o construtor da classe mãe
        super().__init__(nome, ano)
        self.duracao = duracao

    # Imprime o objeto
    def __str__(self):
        return "{} - {} - {} min : {}".format(self.nome, self.ano, self.duracao, self.likes)

# Define uma classe com herança da classe Programa
class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        # Chama o construtor da classe mãe
        super().__init__(nome, ano)
        self.temporadas = temporadas 
    
    # Imprime o objeto
    def __str__(self):
        return "{} - {} - {} temporadas : {}".format(self.nome, self.ano, self.temporadas, self.likes)

# A classe playlist herda agora de list e pode ser iterada
class Playlist:
    def __init__(self, nome, programas):        
        self.nome = nome
        self._programas = programas

    # Método que libera a classe para se tornar um objeto iterável,
    # informa ao python que essa classe tem um list (Duck Typing)
    def __getitem__(self, item):
        return self._programas[item]

    # Permite que essa classe tenha a função len() de list
    def __len__(self):
        return len(self._programas)

    @property
    def listagem(self):
        return self._programas

vingadores = Filme('vingadores guerra infinita', 2018, 160)
tmep = Filme('todo mundo em pânico', 1999, 100)
atlanta = Serie('atlanta', 2018, 2)
demolidor = Serie('demolidor', 2016, 2)
vingadores.dar_like()
vingadores.dar_like()

programas = [vingadores, tmep, atlanta, demolidor]
play_list = Playlist('Lucas', programas)

# Por conta da classe PlayList herdar de list pode-se ter acesso a fuções próprias de list
print("Tamanho da playlist {} é {}".format(play_list.nome, len(play_list)))
for programa in play_list:
    print(programa)