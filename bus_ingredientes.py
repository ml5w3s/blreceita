#importar bibliotecas para ler e manipular páginas web
from requests import get
from bs4 import BeautifulSoup

#página alvo
url = 'https://www.panelinha.com.br/receita/Biscoitos-amanteigados'
resposta = get(url)

#bibliotecas manipuladora do html recebem e tipificam a página alvo
ht_soup = BeautifulSoup(resposta.text, 'html.parser')
type(ht_soup)

#localização da classe na tag alvo e cria um vetor para ingredientes
vt_ingred = ht_soup.find_all('li', class_ = 'ng-star-inserted')

#abrir arquivo para conter dicionario de ingrediente buscado
arq = open('dic_ingredientes.py', 'w')

#variável contador do laço (8 devido a aproveitamento da classe css no menu)
flag = 10
#laço para exibir ingredientes
while flag <= len(vt_ingred)-1:
    #separação do ingrediente no letor
    vr_ingred = vt_ingred[flag]
    #variável recebe ingrediente da lista de ingrediente
    tx_ingred = vt_ingred[flag].text
    #escrevendo arquivo de dicionario de ingredientes
    arq.write(tx_ingred)
    #para inserir quebra de linha
    arq.write("\n")
    #incremento da repetição do laço
    flag +=1

#fechar arquvivo
arq.close
