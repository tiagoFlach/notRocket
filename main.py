__author__ = "Bibiana Duarte"
__author__ = "Tiago Lucas Flach"

import csv
import pickle                                                                   # https://docs.python.org/3/library/pickle.html        
from os.path import dirname, join
import pandas as pd

# Classes
# ------------------------------------------------------------------------------
from class_Node import Node
# from class_BPlusTree import BPlusTree
from class_Trie import Trie

from class_Ability import Ability_Class
from class_Pokemon import Pokemon_Class


# Funções
# ------------------------------------------------------------------------------
def createDatabase():
    pokemon = Pokemon_Class()
    current_dir = dirname(__file__)
    file_name = 'pokemon.csv'
    file_path = join(current_dir, file_name)
    
    # database = open('pokemons.pkl', 'wb')
    # database.close()

    with open(file_name, 'r', encoding='utf16') as dataset:
        reader = csv.DictReader(dataset, delimiter='\t')

        for row in reader:
            number  = row['national_number']
            name    = row['english_name']
            hp      = row['hp']
            attack  = row['attack']
            defense = row['defense']
            height  = row['height_m']
            weight  = row['weight_kg']

            pokemon.create(number, name, hp, attack, defense, height, weight)
            pokemon.save()
            # pokemonsName.insert(pokemon.nome, pokemon.num)

            # pokemon.save()
            # database.append(hash)

def createTrieName():
    
    pass



# Salva os dados em arquivo pickle
def storeData(file, data):      
    dbfile = open(file + '.pkl', 'wb')
    pickle.dump(data, dbfile)                     
    dbfile.close()

def loadData(file):
    # for reading also binary mode is important
    data = []
    with open(file + '.pkl', 'rb') as db:
        while True:
            try:
                data.append(pickle.load(db))
            except EOFError:
                break

    return data


# Main
# ------------------------------------------------------------------------------
print('  _____      _            _            ')
print(' |  __ \    | |          | |           ')
print(' | |__) |__ | | _____  __| | _____  __ ')
print(' |  ___/ _ \| |/ / _ \/ _` |/ _ \ \/ / ')
print(' | |  | (_) |   <  __/ (_| |  __/>  <  ')
print(' |_|   \___/|_|\_\___|\__,_|\___/_/\_\ \n')


createDatabase()


pokemons = loadData('pokemons')
trie = Trie()
for pokemon in pokemons:
    trie.insert(pokemon.nome, pokemon.num)

storeData('trie_Pokemon_Nome', trie)

buscaNome = input('Pesquise por um Pokemon: ')
busca = trie.search(buscaNome)

for item in busca:
    for pokemon in pokemons:
        if pokemon.num == item:
            pokemon.print()
            break

# Print the tree
# def printTree(tree):
#     lst = [tree.root]
#     level = [0]
#     leaf = None
#     flag = 0
#     lev_leaf = 0

#     node1 = Node(str(level[0]) + str(tree.root.values))

#     while (len(lst) != 0):
#         x = lst.pop(0)
#         lev = level.pop(0)
#         if (x.check_leaf == False):
#             for i, item in enumerate(x.keys):
#                 print(item.values)
#         else:
#             for i, item in enumerate(x.keys):
#                 print(item.values)
#             if (flag == 0):
#                 lev_leaf = lev
#                 leaf = x
#                 flag = 1


# record_len = 3
# BPlusTree = BPlusTree(record_len)
# BPlusTree.insert('5', '33')
# BPlusTree.insert('15', '21')
# BPlusTree.insert('25', '31')
# BPlusTree.insert('35', '41')
# BPlusTree.insert('45', '10')

# printTree(BPlusTree)

# if(BPlusTree.find('5', '34')):
#     print("Found")
# else:
#     print("Not found")


















#, nome, num, hp, atk, deff, peso, altura,
# class PokeHash:
#     def __init__(self, size):
#         self.size = size
#         self.used = [0]*size
#         self.dic = [0]*size
#         self.nome = [0]*size
#         self.num = [0]*size
#         self.hp =  [0]*size
#         self.atk = [0]*size
#         self.deff = [0]*size
#         self.peso = [0]*size
#         self.altura = [0]*size
#   #poke = PokeHash(10)
# #poke.print()

#     def print(self):
#         for indice in range(0, self.size):
#            print(
#                "NUM: " + (str(self.num[indice]))+"  NOME: " + (str(self.nome[indice]))+"  HP: "+(str(self.hp[indice])) + "  ATK: " + (str(self.atk[indice])) + "  DEF: "+(str(self.deff[indice]))+"  PESO: "+(str(self.peso[indice]))+"  ALTURA: "+(str(self.altura[indice]) ))
#         #return " * SIZE: {} | USED: {} | NUM: {}".format(self.size, self.used, self.num)

#     def add(self, chave, nome, num, hp, atk, deff, peso, altura,):
#         pos = pos_inic = chave % self.size  # usa o módulo

#         if self.dic[pos] == 0:            # se estiver vazio
#             self.dic[pos] = chave          # coloca a chave
#             self.used[pos] = 1
#             self.nome[pos] = nome
#             self.num[pos] = num
#             self.hp[pos] = hp
#             self.atk[pos] = atk
#             self.deff[pos] = deff
#             self.peso[pos] = peso
#             self.altura[pos] = altura
#             return pos
#         else:                                         # se estiver ocupado, tenta achar lugar usando linear probing
#             first_pass = True
#             while pos != pos_inic or first_pass:
#                 first_pass = False
#                 # incrementa posição (mas fica dentro do intervalo do array de chaves)
#                 pos = (pos + 1) % self.size
#                 if self.dic[pos] == 0:
#                     self.dic[pos] = chave
#                     self.used[pos] = 1
#                     self.nome[pos] = nome
#                     self.num[pos] = num
#                     self.hp[pos] = hp
#                     self.atk[pos] = atk
#                     self.deff[pos] = deff
#                     self.peso[pos] = peso
#                     self.altura[pos] = altura
#                     return pos

#         if pos == pos_inic:                  # se posicao igual à inicial é porque fez a volta e não achou
#             # informa que deu problema (está cheio)
#             return -1
#         else:
#             return pos

# '''
# poke = PokeHash(10)
# poke.print()
# print("\n\n")
# poke.add(1,"Bulbassaur", 1, 12,12,12,12,12)
# poke.print()
# poke.add(2,"Vennusaur",2,10,10,10,10,10)

# poke.print()
# '''