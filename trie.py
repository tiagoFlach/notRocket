#coding=UTF-8

#Nodo da árvore trie
class Trie:
	def __init__(self, char = '', children = [], isLeaf = False, value = None):
		#Char do nodo atual
		self.char = char
	
		#Lista de ponteiros p/ os nodos filhos
		self.children = []
		
		#Booleano que indica se é folha ou não
		self.isLeaf = False
		
		#Valor (caso seja folha)
		self.value = None
		
	#Função que insere uma palavra na trie
	def insert(self, word, value):
		nodo = self
		
		for chr in word:
			found = False
			
			for child in nodo.children:
				if child.char == chr:
					nodo = child
					found = True
					break
			if not found:
				novo_nodo = Trie(char= chr)
				nodo.children.append(novo_nodo)
				nodo = novo_nodo
				
		nodo.isLeaf = True
		nodo.value = value
		
	def search(self, prefix):
		nodo = self
		lista = []

		for chr in prefix:
			found = False
			for child in nodo.children:
				if child.char == chr:
					nodo = child
					found = True
			if not found:
				return []
			
		return nodo.listIDs()
	
	def listIDs(self):
		lista = []
		self.listIDsAux(lista)
		return lista

	def listIDsAux(self, lista):
		if self.isLeaf:
			lista.append(self.value)

		for child in self.children:
			child.listIDsAux(lista)

	def listWords(self, prefix):
		lista = []
		self.listWordsAux(prefix, lista)
		return lista

	def listWordsAux(self, prefix, lista):
		if self.isLeaf:
			lista.append(prefix + self.character)

		for child in self.children:
			child.listWordsAux(prefix + self.character, lista)

	def __str__(self):
		return str(self.listWords(""))


t =Trie()
t.insert("Bulbassaur",1)
t.insert("Ivysaur",2)
t.insert("Charmander",4)
t.insert("Charmeleon",5)
t.insert("Charizard",6)


l = t.search("Char")
print(l)
