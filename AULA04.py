################################################
# CENTRO UNIVERSITÁRIO METODISTA IZABELA HENDRIX
# PROGRAMAÇÃO FUNCIONAL ORIENTADA A OBJETOS PYTHON
# Aula 04
# por Layla Comparin
################################################


# Quando uma estrutura é delimitada por colchetes (lista), 
# chaves (dicionários), parenteses (tuplas)

import pandas as pd


#Importando dados da internet (CSV)
pnad = pd.read_csv('C:/Users/Administrator/Downloads/introducao_ao_python-master/introducao_ao_python-master/pes_2012.csv')

# Trás as linhas, colunas
pnad.shape 

# Nome das variáveis
pnad.columns

# Primeiros Casos
pnad.head()

# Trás os dados, o tamanho e o tipo.
pnad['V8005']
pnad['V8005'].dtype #Retorna o tipo do númerico. 
pnad['V0302']

# Estudando a idade:
pnad['V8005'].describe() #minimo, maximo, quartis, desvio padrão. 
pnad['V8005'].mean() #minimo
pnad['V8005'].describe().round() # Arrendondando os números
pnad['V8005'].describe().round(decimals = 2) # Arrendondando os números

m = pnad['V8005'].mean()
round(m,2)

pnad.describe() # Mostra as estatisticas descritivas numéricas


# Estudando sexo e cor/raça:

pnad['V0302'].value_counts() #Retorna o número de valores para variáveis categóricas.

tab_sexo =  pd.crosstab(index=pnad['V0302'],
            columns=['count'])

print("Distribuição da Frequência - Sexo" + "\n")
##porcentsexo = (tab_sexo/tab_sexo.sum()) * 100
porcentsexo.round()

pnad['V0404'].value_counts() #Retorna o número de valores para variáveis categóricas.

tab_cor = pnad['V0404'].value_counts() 

print("Distribuição da Frequência - Cor" + "\n")
print(tab_cor)

porcentcor = (tab_cor/tab_cor.sum()) * 100
print("Porcentagem - Cor" + "\n")
porcentcor.round(decimals = 3)

# Cruzando Informações
sexo_cor = pd.crosstab(index=pnad['V0404'],
           columns=pnad['V0302'])

print(sexo_cor)

# Estudando a renda:

pnad.columns
renda = pnad['V4720']
type(renda)

pnad['V4720'].describe()

print(renda)

renda = float(renda)

renda = pnad['V4720'].astype(float)

import numpy as np

ast.literal_eval(pnad['V4720'].astype(float))

np.genfromtxt(np.array(['Sem declaração']).astype('bytes'))

np.set_printoptions(precision=3, suppress=True)

p.renda = u' '.join((agent_contact, agent_telno)).encode('utf-8').strip()
































