#importar biblioteca para comparar similaridade
from difflib import SequenceMatcher

#classe para definir receitas
class Receita:
	def __init__(self, nome_receita, ingred_receita, preparo):
		self.nome = nome_receita
		self.ingred = ingred_receita
		self.prep = preparo

#objeto para receber dados da receita
receita = Receita('Biscoito amanteigado',open("dic_ingredientes.dat", "r"), 'lista')

#saida com dados do objeto
print (receita.nome)
#repeticao para ler cada linha do dic_proporcoes
for linha in receita.ingred :
	#linha do ingrediente
	print(linha.rstrip())
	#variável recebe ingrediente buscado e compara com dicionario de proporções
	sm = SequenceMatcher(None, linha.rstrip(), "farinha")
	#imprimir o valor de similaridade
	print(sm.ratio())
