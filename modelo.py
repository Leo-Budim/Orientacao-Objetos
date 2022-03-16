
class Programa:
    def __init__(self, titulo, ano):
        self._titulo = titulo
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    @property
    def titulo(self):
        return self._titulo.title()

    def dar_like(self):
        self._likes += 1


class Filme(Programa):
    def __init__(self, titulo, ano, duracao):
        super().__init__(titulo, ano)
        self.duracao = duracao

    def __str__(self):
        return f'{self.titulo} - {self.duracao} min - {self._likes}'


class Serie(Programa):
    def __init__(self, titulo, ano, temporadas):
        super().__init__(titulo, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'{self.titulo} - {self.temporadas} temporadas - {self._likes}'

class Playlist():
    def __init__(self, nome, programas):
        self.nome = nome
        self.programas = programas

    def __getitem__(self, item):
        return self.programas[item]

    @property
    def listagem(self):
        return self.programas

    def __len__(self):
        return len(self.programas)


a_chegada = Filme('a chegada', 2012, 160)
peaky_blinders = Serie('peaky blinders', 2019, 5)
avatar = Filme('avatar', 2008, 120)
got = Serie('game of thrones', 2015, 7)

a_chegada.dar_like()
a_chegada.dar_like()
peaky_blinders.dar_like()
avatar.dar_like()
avatar.dar_like()
avatar.dar_like()
avatar.dar_like()
got.dar_like()
got.dar_like()
got.dar_like()

filmes_e_series = [avatar, peaky_blinders, got, a_chegada]
playlist_ferias = Playlist("assistir nas ferias", filmes_e_series)

print(f'tamanho: {len(playlist_ferias)}')

for programa in playlist_ferias:
#for programa in filmes_e_series:
    print(programa)
    ''' #detalhe = programa.duracao if hasattr(programa, 'duracao') else programa.temporadas
    if hasattr(programa, 'duracao'):
        detalhe = programa.duracao
    else:
        detalhe = programa.temporadas
    print(f'{programa.titulo} - {detalhe} - {programa.likes}')'''


