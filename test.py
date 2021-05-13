import pickle


class Pokemon_Class:
    def __init__(self, numero, nome, hp, ataque, defesa, peso, altura):
        self.num = numero
        self.nome = nome
        self.hp = hp
        self.atk = ataque
        self.deff = defesa
        self.peso = peso
        self.altura = altura


poke1 = Pokemon_Class(1,"Bulbassaur",5,5,5,5,5)
poke2 = Pokemon_Class(4, "Charmander", 5, 5, 5, 5, 5)
poke3 = Pokemon_Class(7, "Squirtle", 5, 5, 5, 5, 5)
best_poke = Pokemon_Class(131, "Ditto", 5, 5, 5, 5, 5)

# Dumping step
data = [poke1,poke2,poke3]
with open('test.pkl', 'wb') as f:
    for d in data:
        pickle.dump(d, f)

# Loading step
data2 = []
with open('test.pkl', 'rb') as f:
    while True:
        try:
            data2.append(pickle.load(f))
        except EOFError:
            break

for item in data2:
    print(item.__getstate__)
# x = pickle.Unpickler(data2[1])