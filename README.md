Listagem de Requisitos 
Funcionais:

As funcionalidades e operações que o sistema deve oferecer para seus usuários são as seguintes:

•Permitir que os usuários raspem ingredientes de receitas do site panelinha.com. 
•Reconhecer a quantidade e a categoria de cada ingrediente. 
•Permitir que um usuário possa alterar informacoes como quantidade de um ingrediente especifico 
ou rendimento da receita.
•Recalcular demais ingredientes proporcionalmente. 

Glossário de Termos 

•Receita:
 Uma receita é uma entidade abstrata que tem por objetivo guiar alguém no preparo de
determinado alimento. Ela é composta por uma lista de ingredientes com suas respectivas
quantidades, e de um modo de preparo (descrição da seqüência de passos necessários para
preparar o alimento), além, é claro, de ser associada a um nome. Opcionalmente, uma receita
possui informações diversas que auxiliam no preparo, como dicas, rendimento, autoria, etc.
•Ingrediente:
 Um ingrediente é simplesmente um alimento usado na preparação de outro
alimento.
•Usuário:
 Os usuários do sistema, ou usuários cadastrados no sistema, incluem todas as pessoas
que se interessam por culinária, seja para fins pessoais (como cozinhar para a família) ou
profissionais (como em um restaurante). Entre os usuários cadastrados no S.O.G.R.A., podemos
citar cozinheiros profissionais, ajudantes de cozinha, donas de casa, empregadas domésticas,
vovós, etc. 

Casos de Uso Preliminares 
Aqui são apresentados os casos de uso preliminares que, devido a sua natureza intuitiva e grau de
abstração, não receberão mais detalhes além de sua descrição textual.
-|ver diagramas/caso de uso|- caso_uso.png

Descrição Textual dos Casos de Uso Preliminares 

# receitas
Repositório principal das Receitas Lene

Notação de nome dos arquivos:
 bus_ buscar
 com_ comparar
 con_ converter
 dic_ dicionários
 ins_ instruções
 ler_ leitura
 _dev desenvolvimento
 _mod modificador

Notação de código
 dc_ dicionário
 ls_ lista
 vr_ variável
 vt_ vetor
 tx_ texto
 
Classes
 Receitas
  Atributos (nome, ingredientes, preparo)
  Metodos (vetor para separar quantidade de unidade e ingrediente)
 Ingredientes
  Atributos (quantidade, unidade, ingrediente)
  Metodos (vetor para converter unidades)
          (vetor para balancear quantidades)
