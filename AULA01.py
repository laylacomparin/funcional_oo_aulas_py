################################################
# CENTRO UNIVERSITÁRIO METODISTA IZABELA HENDRIX
# PROGRAMAÇÃO FUNCIONAL ORIENTADA A OBJETOS PYTHON
# Aula 01
# por Layla Comparin
################################################

5**2 # Python usa dois * ao invés do R que usa ^
5%2 # Python usa % ao invés do R que usa %%
5//2 # Quociente inteiro da divisão

x = 6 # x recebe 6
print(x)
y = 8.5 # y recebe 8.5
x ** (1/2) # Exponecial de 1/2
25 ** (1/2) # Exponecial de 1/2

type(x) #Tipo de Dados - Algo como o class no R
type(y) #Tipo de Dados - Algo como o class no R

nome = "Layla"
sobrenome = "Comparin"

print(nome + ' ' + sobrenome)
print(sobrenome)

type(nome)

# Testes lógicos: True or False
x == 5
x < 5
x > 5

True is False


## Estruturas de Dados:
# Listas e Dicionários:

# Lista:
nomes = ['Layla', 'Gerson', 'Edésio', 'Iago']
print(nomes)
type(nomes)
len(nomes) # Quantidade de elementos na variável

nomes[0] # O primeiro elemento começa no 0, já no R começa no 1
nomes.append('Layla') # Insere um elemento na variável nomes
nomes.pop(0) # Remove um elemento na variável nomes
nomes[3] = 'Neylson' # Substitui um elemento na variável nomes por outro

nomes[:3] # Seleciona os elementos até a posição 3 - 0,1,2
nomes[1:3] # Seleciona os elementos da 2 até posição 3 - 1,2
nomes[1:] # Seleciona os elementos da 2 posição em diante - 2...
nomes[1:-1] # Seleciona os elementos da 2 posição até o penúltimo.
nomes[:-2] # Seleciona os elementos do inicio até o antepenúltimo.

# Mesma coisa acima, usando um nome:
nomeCompleto = "Layla Suellen Vilela Santos Comparin"
idade = 24

# A quebra de linha somente é para ser usada para quebrar o código dentro do PY.
nomeCompleto + ' tem ' + \
str(idade) +  ' anos.'

# O \n quebra a linha na visualização do Console.
print (nomeCompleto + ' tem\n' + \
str(idade) +  ' anos.')

### Dicionários:

# {'key': 'valor'}
alunos = {'nome':['Layla', 'Gerson'], 
          'idade':[24, 25],
          'curso':['CD','CD'],
          'natural':['Maceió', 'Recife']}
print(alunos)
alunos['nome'] # Printa o valor do elemento no Console
alunos['idade'] # Printa o valor do elemento no Console
alunos['curso'] # Printa o valor do elemento no Console
alunos['natural'] # Printa o valor do elemento no Console

alunos['idade'][1] # Printa o valor do elemento da segunda posição no Console

alunos.keys() # Retorna só o nome das colunas do dicionários

alunos.values() # Retorna o conteúdo das colunas do dicionários

alunos['bomAluno'] = True

alunos['bomAluno']


funcionalOO = {'Alunos':['Layla', 'Gerson', 'Bia', 'Warley', 'Adelvan',
                         'Ester', 'Vanessa', 'Marcos', 'Juliany',
                         'Nelson', 'Numiá', 'Iago'],
               'Professor':'Neylson Crepalde',
               'Sala': 2204,
               'Quantidade de Computadores': 25,
               'Cursos':['CD', 'BioInfo'],
               'IES': 'IMIH'} 


funcionalOO['professor']
funcionalOO['Quantidade de Computadores']
len(funcionalOO['Alunos'])

type(funcionalOO)

funcionalOO.keys() # Retorna só o nome das colunas do dicionários

funcionalOO.values() # Retorna o conteúdo das colunas do dicionários

listaAlunos = funcionalOO['Alunos']

print(funcionalOO)

funcionalOO['Alunos'] = {'nomes': listaAlunos,
                         'id':list(range(1,13)),
                         'idade':list(range(25,36))}






















































