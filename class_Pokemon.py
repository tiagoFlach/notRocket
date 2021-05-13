import pickle

# Classe Pokemon
# Atributos: hash, numero, nome, hp, atk, deff, peso, altura
class Pokemon_Class:
    def __init__(self):
        self.size   = None
        self.used   = None
        self.dic    = None
        self.num    = None
        self.nome   = None
        self.hp     = None
        self.atk    = None
        self.deff   = None
        self.peso   = None
        self.altura = None
    # def __init__(self, size):
    #     self.size   = size
    #     self.used   = [0]*size
    #     self.dic    = [0]*size
    #     self.num    = [0]*size
    #     self.nome   = [0]*size
    #     self.hp     = [0]*size
    #     self.atk    = [0]*size
    #     self.deff   = [0]*size
    #     self.peso   = [0]*size
    #     self.altura = [0]*size
    # poke = PokeHash(10)

    def __hash__(self):
        return hash(self.num)

    # Função print()
    # Imprime as informações do objeto
    def print(self):
        print('Número:  ' + self.num)
        print('Nome:    ' + self.nome)
        print('HP:      ' + self.hp)
        print('Ataque:  ' + self.atk)
        print('Defesa:  ' + self.deff)
        print('Peso:    ' + self.peso)
        print('Altura:  ' + self.altura + '\n')

        return " * SIZE: {} | USED: {} | NUM: {}".format(self.size, self.used, self.num)

    # Função create()
    # Define os atributos do objeto
    def create(self, numero, nome, hp, ataque, defesa, peso, altura):
        self.num = numero
        self.nome = nome
        self.hp = hp
        self.atk = ataque
        self.deff = defesa
        self.peso = peso
        self.altura = altura

    # Função save()
    # Salva o objeto através das funções pickle
    def save(self):
        file = ('pokemons.pkl')
        database = open(file, 'ab')
        pickle.dump(self, database)
        database.close()

        return hash(self)

    # Função add()
    # Cria e e salva o objeto
    def add(self, chave, nome, num, hp, atk, deff, peso, altura):

        pos = pos_inic = chave % self.size  # usa o módulo

        if self.dic[pos] == 0:            # se estiver vazio
            self.dic[pos]    = chave          # coloca a chave
            self.used[pos]   = 1
            self.num[pos]    = num
            self.nome[pos]   = nome
            self.hp[pos]     = hp
            self.atk[pos]    = atk
            self.deff[pos]   = deff
            self.peso[pos]   = peso
            self.altura[pos] = altura
            return pos
        else:                                         # se estiver ocupado, tenta achar lugar usando linear probing
            first_pass = True
            while pos != pos_inic or first_pass:
                first_pass = False
                # incrementa posição (mas fica dentro do intervalo do array de chaves)
                pos = (pos + 1) % self.size
                if self.dic[pos] == 0:
                    self.dic[pos]    = chave
                    self.used[pos]   = 1
                    self.nome[pos]   = nome
                    self.num[pos]    = num
                    self.hp[pos]     = hp
                    self.atk[pos]    = atk
                    self.deff[pos]   = deff
                    self.peso[pos]   = peso
                    self.altura[pos] = altura
                    return pos

        if pos == pos_inic:                  # se posicao igual à inicial é porque fez a volta e não achou
            # informa que deu problema (está cheio)
            return -1
        else:
            return pos