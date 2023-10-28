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
        self._titulo  = titulo.title() # 2 undescore para privar o atributo  
        self.ano       = ano
        self.duracao   = duracao
        self._likes   = 0 

class Series(Programa):
    def __init__(self, titulo, ano, temporadas):
        self._titulo     = titulo.title()
        self.ano          = ano 
        self.temporadas   = temporadas 
        self._likes      = 0

vingadores = Filme('vingadores - guerra infinita', 2018, 160)
vingadores.dar_like()
print(f"Nome {vingadores.titulo} - Ano {vingadores.ano} - Duração {vingadores.duracao} - Likes {vingadores.likes}")


atlanta = Series('atlanta', 2018, 2)
atlanta.dar_like()
print(f'Nome {atlanta.titulo} - Ano {atlanta.ano} - Temporadas {atlanta.temporadas} - likes {atlanta.likes}')