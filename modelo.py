class Programa():
    def __init__(self, titulo, ano):
        self._titulo = titulo.title()
        self.ano      = ano
        self._likes   = 0

    @property                   #Criando um elemento que retorna o atributo __likes 
    def likes(self):
        return self._likes

    def dar_like(self):
        self._likes += 1

    @property
    def titulo(self):
        return self._titulo
    
    @titulo.setter
    def titulo(self, novo_titulo):
        self._titulo = novo_titulo.title()

class Filme(Programa):
    def __init__(self, titulo, ano, duracao):
        super().__init__(titulo, ano) #chamando o inicializador da classe mãe, o meu objeto recebe a instacia que foi criada pela classe mãe
        self.duracao   = duracao

class Series(Programa):
    def __init__(self, titulo, ano, temporadas):
        super().__init__(titulo, ano)
        self.temporadas   = temporadas 

vingadores = Filme('vingadores - guerra infinita', 2018, 160)
atlanta = Series('atlanta', 2018, 2)
vingadores.dar_like()
vingadores.dar_like()
vingadores.dar_like()

atlanta.dar_like()
atlanta.dar_like()

print(f" Nome {vingadores.titulo} - {vingadores.ano} - {vingadores.duracao} - Likes {vingadores.likes}")
print(f' Nome {atlanta.titulo} - {atlanta.ano} - {atlanta.temporadas} - Likes {atlanta.likes}')

filmes_e_series = [vingadores, atlanta]

for programa in filmes_e_series:
    detalhes = programa.duracao if hasattr(programa, 'duracao') else programa.temporadas
    print(f'{programa.titulo} - D {detalhes} - {programa.likes}')