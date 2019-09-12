#importar bibliotecas para comparar similaridade, ler e manipular páginas web
from difflib import SequenceMatcher
from requests import get
from bs4 import BeautifulSoup

#dicionario para classificar ingrediente
dc_categorias = {'leite': 'liquido', 'água': 'liquido', 'óleo': 'liquido', 'bebidas alcoólicas': 'liquido', 'café': 'liquido', 'manteiga': 'gordura', 'margarina': 'gordura', 'gordura vegetal': 'gordura', 'amêndoa': 'castanha', 'noz': 'castanha','farinha de trigo':'farinha'}
#Leite, água, óleo, bebidas alcoólicas, café, etc...
dc_liquidos = {'1 xícara': '250','1/2 xícara': '120','1/3 xícara': '80','1/4 xícara': '60','1 colher de sopa': '15','1 colher de chá': '5'};
#Manteiga, margarina e gordura vegetal
dc_gordutras = {'1 xícara': '200','1/2 xícara': '100','1/3 xícara': '65','1/4 xícara': '50','1 colher de sopa': '12','1 colher de chá': '4'};
dc_fuba = {'1 xícara': '120','1 colher de sopa': '7,5','1 colher de chá': '2,5'};
dc_farinha_trigo = {'1 xícara': '120','1/2 xícara': '100','1/3 xícara': '60','1/4 xícara': '50','1 colher de sopa': '12','1 colher de chá': '4'};
#Maizena
dc_amido = {'1 xícara': '150','1 colher de sopa': '9','1 colher de chá': '3'};
dc_mel = {'1 xícara': '300','1 colher de sopa': '18','1 colher de chá': '6'};
#Cacal em pó
dc_chocolate = {'1 xícara': '90','1/2 xícara': '45','1/3 xícara': '30','1/4 xícara': '20','1 colher de sopa': '6','1 colher de chá': '2'};
dc_acucar = {'1 xícara': '180','1/2 xícara': '90','1/3 xícara': '65','1/4 xícara': '45','1 colher de sopa': '19','1 colher de chá': '3,5'};
dc_polvilho = {'1 xícara': '150','1 colher de sopa': '9','1 colher de chá': '3'};
dc_fermento = {'1 colher de sopa': '15','1 colher de chá': '5'};
dc_bicarbonato = {'1 colher de chá': '5'};
dc_sal = {'1 colher de sopa': '20','1 colher de chá': '5'};
dc_gotas_chocolate = {'1 xícara': '30'};
dc_frutas_cristalizadas = {'1 xícara': '150'};
#Amêndoas, Nozes e Castanhas
dc_castanhas = {'1 xícara': '140'};
dc_aveia = {'1 xícara': '80','1 colher de sopa': '5','1 colher de chá': '1,5'};
dc_coco_ralado = {'1 xícara': '80','1 colher de sopa': '5','1 colher de chá': '1,5'};

#página alvo
url = 'https://www.panelinha.com.br/receita/Biscoitos-amanteigados'
resposta = get(url)

#bibliotecas manipuladora do html recebem e tipificam a página alvo
ht_soup = BeautifulSoup(resposta.text, 'html.parser')
type(ht_soup)

#localização da classe na tag alvo e cria um vetor para ingredientes
vt_ingred = ht_soup.find_all('li', class_ = 'ng-star-inserted')

#abrir arquivo para conter dicionario de ingrediente buscado
vr_arq = open('dic_ingredientes.dat', 'w')

#variável contador do laço (8 devido a aproveitamento da classe css no menu)
flag = 8
#laço para exibir ingredientes
while flag <= len(vt_ingred)-1:
	#separação do ingrediente no vetor
	vr_ingred = vt_ingred[flag]
	#variável recebe ingrediente da lista de ingrediente
	tx_ingred = vt_ingred[flag].text
	#escrevendo arquivo de dicionario de ingredientes
	vr_arq.write(tx_ingred)
	#para inserir quebra de linha
	vr_arq.write("\n")
	#laço para comparar cada linha do arquivo de ingredientes raspasdos com o dicionário de categorias
	for ingrediente in dc_categorias:
		#variável recebe linha do arquivo com ingrediente buscado e compara com dicionario de proporções
		vr_seqmat = SequenceMatcher(None, tx_ingred,dc_categorias[ingrediente])
		#saída com nomes de itens comparados
		print ('{0}: {1}'.format(tx_ingred,dc_categorias[ingrediente]))
		#saída com similaridade entre o ingrediente com as chaves
		print(vr_seqmat.ratio())
	#incremento da repetição do laço
	flag +=1

tx_ingred='manteiga e farinha de'
#tx_ing.find('farinha')

print('farinha' in tx_ingred)

#fechar arquvivo
vr_arq.close
