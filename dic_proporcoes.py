#importar bibliotecas para comparar similaridade, ler e manipular páginas web
from difflib import SequenceMatcher

#dicionario para classificar ingrediente
dc_categorias = {'leite': 'liquido', 'água': 'liquido', 'óleo': 'liquido', 'bebidas alcoólicas': 'liquido', 'café': 'liquido', 'Manteiga': 'gordura', 'margarina': 'gordura', 'gordura vegetal': 'gordura', 'amêndoa': 'castanha', 'noz': 'castanha','farinha de trigo':'farinha'}
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

#laço para comparar cada linha do arquivo de ingredientes raspasdos com o dicionário de categorias
for ingrediente in dc_categorias:
#variável recebe linha do arquivo com ingrediente buscado e compara com dicionario de proporções
	#vr_ingred = line
	print(dc_categorias[ingrediente])
	#vr_seqmat = SequenceMatcher(None, vr_ingred,dc_categorias)
    #saída com similaridade entre o ingrediente com as chaves
    #print(vr_seqmat.ratio())
    #saída das chaves e valores do dicionário de proporções
    #print ('{0}: {1}'.format(dc_categorias,dc_categorias[vt_ingred]))

ingrediente = '1 xícara (chá) de farinha de trigo'
#laço para comparar similaridade entre ingrediente e categoria
#for ingrediente in dc_categorias:
    #vr_ingred = ingrediente
    #vr_seqmat = SequenceMatcher(None, vr_ingred,dc_categorias)
    #print (vr_seqmat.ratio())
