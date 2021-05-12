import csv
import pickle
from os.path import dirname, join
import pandas as pd

# , nome, num, hp, atk, deff, peso, altura,
class PokeHash:
    def __init__(self, size):
        self.size = size
        self.used = [0]*size
        self.dic = [0]*size
        self.nome = [0]*size
        self.num = [0]*size
        self.hp = [0]*size
        self.atk = [0]*size
        self.deff = [0]*size
        self.peso = [0]*size
        self.altura = [0]*size
  # poke = PokeHash(10)
# poke.print()

    def print(self):
        for indice in range(0, self.size):
           print(
               "NUM: " + (str(self.num[indice]))+"  NOME: " + (str(self.nome[indice]))+"  HP: "+(str(self.hp[indice])) + "  ATK: " + (str(self.atk[indice])) + "  DEF: "+(str(self.deff[indice]))+"  PESO: "+(str(self.peso[indice]))+"  ALTURA: "+(str(self.altura[indice])))
        # return " * SIZE: {} | USED: {} | NUM: {}".format(self.size, self.used, self.num)

    def add(self, chave, nome, num, hp, atk, deff, peso, altura):
        pos = pos_inic = chave % self.size  # usa o módulo

        if self.dic[pos] == 0:            # se estiver vazio
            self.dic[pos] = chave          # coloca a chave
            self.used[pos] = 1
            self.nome[pos] = nome
            self.num[pos] = num
            self.hp[pos] = hp
            self.atk[pos] = atk
            self.deff[pos] = deff
            self.peso[pos] = peso
            self.altura[pos] = altura
            return pos
        else:                                         # se estiver ocupado, tenta achar lugar usando linear probing
            first_pass = True
            while pos != pos_inic or first_pass:
                first_pass = False
                # incrementa posição (mas fica dentro do intervalo do array de chaves)
                pos = (pos + 1) % self.size
                if self.dic[pos] == 0:
                    self.dic[pos] = chave
                    self.used[pos] = 1
                    self.nome[pos] = nome
                    self.num[pos] = num
                    self.hp[pos] = hp
                    self.atk[pos] = atk
                    self.deff[pos] = deff
                    self.peso[pos] = peso
                    self.altura[pos] = altura
                    return pos

        if pos == pos_inic:                  # se posicao igual à inicial é porque fez a volta e não achou
            # informa que deu problema (está cheio)
            return -1
        else:
            return pos

    def searchNome(self, nome):
        n = 0
    	while self.used[n] == 1:
		    if self.nome[n] == nome:
                return self.chave[n]
            else:
                n = n+1

    def searchNum(self, num):
        n = 0
    	while self.used[n] == 1:
		    if(self.num[n] == num):
                return self.chave[n]
            else:
                n = n+1

'''
    def searchTipo(self, num):
       '''            



'''
poke = PokeHash(10)
poke.print()
print("\n\n")
poke.add(1,"Bulbassaur", 1, 12,12,12,12,12)
poke.print()
poke.add(2,"Vennusaur",2,10,10,10,10,10)

poke.print()
'''


class PokeHash:

    def __init__(self, size):
        self.size = size
        self.used = [0]*size
        self.dic = [0]*size
        self.nome = [0]*size
        self.num = [0]*size
        self.hp = [0]*size
        self.atk = [0]*size
        self.deff = [0]*size
        self.peso = [0]*size
        self.altura = [0]*size
  # poke = PokeHash(10)
# poke.print()

    

    def print(self):
        for indice in range(0, self.size):
           print(
               "NUM: " + (str(self.num[indice]))+"  NOME: " + (str(self.nome[indice]))+"  HP: "+(str(self.hp[indice])) + "  ATK: " + (str(self.atk[indice])) + "  DEF: "+(str(self.deff[indice]))+"  PESO: "+(str(self.peso[indice]))+"  ALTURA: "+(str(self.altura[indice])))
        # return " * SIZE: {} | USED: {} | NUM: {}".format(self.size, self.used, self.num)

    def add(self, chave, nome, num, hp, atk, deff, peso, altura,):
        pos = pos_inic = chave % self.size  # usa o módulo

        if self.dic[pos] == 0:            # se estiver vazio
            self.dic[pos] = chave          # coloca a chave
            self.used[pos] = 1
            self.nome[pos] = nome
            self.num[pos] = num
            self.hp[pos] = hp
            self.atk[pos] = atk
            self.deff[pos] = deff
            self.peso[pos] = peso
            self.altura[pos] = altura
            return pos
        else:                                         # se estiver ocupado, tenta achar lugar usando linear probing
            first_pass = True
            while pos != pos_inic or first_pass:
                first_pass = False
                # incrementa posição (mas fica dentro do intervalo do array de chaves)
                pos = (pos + 1) % self.size
                if self.dic[pos] == 0:
                    self.dic[pos] = chave
                    self.used[pos] = 1
                    self.nome[pos] = nome
                    self.num[pos] = num
                    self.hp[pos] = hp
                    self.atk[pos] = atk
                    self.deff[pos] = deff
                    self.peso[pos] = peso
                    self.altura[pos] = altura
                    return pos

        if pos == pos_inic:                  # se posicao igual à inicial é porque fez a volta e não achou
            # informa que deu problema (está cheio)
            return -1
        else:
            return pos


        
     
            
   



'''
poke = PokeHash(10)
poke.print()
print("\n\n")
poke.add(1,"Bulbassaur", 1, 12,12,12,12,12)
poke.print()
poke.add(2,"Vennusaur",2,10,10,10,10,10)

poke.print()
'''


def inicializaPokeHash():
    n = 0
    tam = 0
    poke = PokeHash(1000)
    current_dir = dirname(__file__)
    file_path = join(current_dir, "./poke.csv")
    # read specific columns of csv file using Pandas
    df = pd.read_csv(file_path, sep=";", error_bad_lines=False, usecols=[
                     "national_number", "english_name", "height_m", "weight_kg", "hp", "attack", "defense"])
    poke_list = df.values.tolist()

    for x in poke_list:
        tam = tam+1

    for x in range(0, tam-1):
        num = poke_list[n][0]
        nome = poke_list[n][1]
        altura = poke_list[n][2]
        peso = poke_list[n][3]
        hp = poke_list[n][4]
        atk = poke_list[n][5]
        deff = poke_list[n][6]
        n = n+1
        poke.add(n, nome, num, hp, atk, deff, peso, altura)
     
    return poke
    #poke.print()
    # print(poke_list)

    # print("\n\n"+ str(poke_list[1][2]))

# print(poke_list)
   # print(poke_list[0][0])
# poke = PokeHash(1000)

    
    
class HashTipo:
    def __init__(self, size):
        self.size = size
        self.used = [0]*size
        self.dic = [0]*size
        self.primario = [0]*size
        self.secundario = [0]*size
    # print("\n\n"+ str(poke_list[1][2]))

    def print(self):
        for indice in range(0, self.size):
           print(
               "Tipo1: " + (self.primario[indice])+"  Tipo2: " + (self.secundario[indice]))

    def add(self, chave, tipo1,tipo2):
        pos = pos_inic = chave % self.size  # usa o módulo

        if self.dic[pos] == 0:            # se estiver vazio
            self.dic[pos] = chave          # coloca a chave
            self.used[pos] = 1
            self.primario= tipo1
            self.secundario = tipo2
            return pos
        else:                                         # se estiver ocupado, tenta achar lugar usando linear probing
            first_pass = True
            while pos != pos_inic or first_pass:
                first_pass = False
                # incrementa posição (mas fica dentro do intervalo do array de chaves)
                pos = (pos + 1) % self.size
                if self.dic[pos] == 0:
                    self.dic[pos] = chave          # coloca a chave
                    self.used[pos] = 1
                    self.primario = tipo1
                    self.secundario = tipo2
                    return pos

        if pos == pos_inic:                  # se posicao igual à inicial é porque fez a volta e não achou
            # informa que deu problema (está cheio)
            return -1
        else:
            return pos


def inicializaHashTipo():
    n = 0
    tam = 0
    hashTipo = HashTipo(1000)
    current_dir = dirname(__file__)
    file_path = join(current_dir, "./poke.csv")
     # read specific columns of csv file using Pandas
    df = pd.read_csv(file_path, sep=";", error_bad_lines=False, usecols=[
         "primary_type" ,"secondary_type"])
    poke_list = df.values.tolist()
    # print(poke_list)

    ''' print(poke_list[0][1])
    print(n)
    '''
    for x in poke_list:
        tam = tam+1

    for x in range(0, tam-1):
        tipo1 = poke_list[n][0]
        tipo2 = poke_list[n][1]
        n = n+1
        # print(tipo1)
        # print(tipo2)
        hashTipo.add(n, tipo1, tipo2)
    
    #hashTipo.print()


# print(poke_list)
   # print(poke_list[0][0])
# poke = PokeHash(1000)


# inicializaPokeHash()

# inicializaHashTipo()

'''
hashTipo = HashTipo(10)
hashTipo.add(1,"Grass","Poison")
hashTipo.add(2, "Grass", "Poison")
hashTipo.add(4, "Fire", "0")
hashTipo.print()
'''


poke = inicializaPokeHash()
x = poke.searchNome("Bulbassaur")
print(poke.num[x])
