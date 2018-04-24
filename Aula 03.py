################################################
# CENTRO UNIVERSITÁRIO METODISTA IZABELA HENDRIX
# PROGRAMAÇÃO FUNCIONAL ORIENTADA A OBJETOS PYTHON
# Aula 03
# por Layla Comparin
################################################

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

# Mesma coisa acima, usando um nome completo:
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

funcionalOO = {'Nome Disciplina':'Funcional e OO',
               'Professor':'Neylson Crepalde',
               'Sala': '2202',
               'Quantidade de Alunos': 20,
               'Cursos':['CD', 'BioInfo']} 

print(funcionalOO)

funcionalOO.keys() # Retorna só o nome das colunas do dicionários
funcionalOO.values() # Retorna o conteúdo das colunas do dicionários

funcionalOO['Professor']
funcionalOO['Quantidade de Computadores']
funcionalOO['Cursos'][0]

len(funcionalOO['Sala']) #Retorna o número de variáveis dentro do atributo.
type(funcionalOO)

listaCursos = funcionalOO['Cursos']

funcionalOO['Cursos'] = {'nomes': listaCursos,
                         'id':list(range(1,13)),
                         'idade':list(range(25,36))}


import numpy as np #Importar pacote numpy - Análise de Dados
import scipy as sc #Importar pacote scipy - Análise de Dados
import pandas as pd #Importar pacote pandas - Análise de Dados

x = [3,5,4,7,6,9]

print(x) 
len(x) #Retorna o número de variáveis dentro do atributo.
np.mean(x) # Tira a média do números de x.
min(x) # Tira o minimo do números de x.
max(x) # Tira o maximo do números de x.
np.var(x) # Tira a variancia do números de x.

np.sqrt(x) # Tira a raiz quadrada do números de x.
np.sqrt(x[0]) # Tira a raiz quadrada apenas do primeiro elemento de x.

tuple_exemple = 0,1,4,9,16,25 # Tuples são "listas" imutáveis, não aceitam alteração, apenas inserção.
tuple_exemple
tuple_exemple[2]
tuple_exemple[2] = 6 # Como não aceitam alteração, esse código dará erro.


import math as m
math.factorial(5)



























