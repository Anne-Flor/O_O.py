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
    
    def imprime(self):
        print(f'{self._nome} - {self.ano} - {self.likes}')

class Filme(Programa):
    def __init__(self, titulo, ano, duracao):
        super().__init__(titulo, ano) #chamando o inicializador da classe mãe, o meu objeto recebe a instacia que foi criada pela classe mãe
        self.duracao   = duracao

    def __str__(self):
        return f' Titulo: {self._titulo} - Minutos: {self.duracao} - Ano: {self.ano} - Likes: {self._likes}'

class Series(Programa):
    def __init__(self, titulo, ano, temporadas):
        super().__init__(titulo, ano)
        self.temporadas   = temporadas

    def __str__(self):
        return f' Título: {self._titulo} - Temporadas : {self.temporadas} - ANo: {self.ano} - Likes {self._likes}'

class Playlist(list):
    def __init__(self, nome, programas):
        self.nome = nome 
        self._programas = programas
    
    def __getitem__(self, item):
        return self._programas[item]
    
    @property
    def listagem(self):
        return self._programas
    
    def __len__(self):
        return len(self._programas)
    

vingadores = Filme('vingadores - guerra infinita', 2018, 160)
atlanta = Series('atlanta', 2018, 2)
tmep = Filme('Todo mundo em panico', 1999, 100)
demolidor = Series('demolidor', 2016, 2)

vingadores.dar_like()
tmep.dar_like()
tmep.dar_like()
tmep.dar_like()
tmep.dar_like()
demolidor.dar_like()
demolidor.dar_like()
atlanta.dar_like()
atlanta.dar_like()
atlanta.dar_like()

filmes_e_series = [vingadores, atlanta, demolidor, tmep]
playlist_fim_de_semana = Playlist('fim de semana', filmes_e_series)

print(f'Tamanho da Playlist: {len(playlist_fim_de_semana)}')

print(playlist_fim_de_semana[0])

for programa in playlist_fim_de_semana: 
    print(programa)