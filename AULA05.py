################################################
# CENTRO UNIVERSITÁRIO METODISTA IZABELA HENDRIX
# PROGRAMAÇÃO FUNCIONAL ORIENTADA A OBJETOS PYTHON
# Aula 05
# por Layla Comparin
################################################


# Quando uma estrutura é delimitada por colchetes (lista), 
# chaves (dicionários), parenteses (tuplas)

import pandas as pd #Dataframes - Estrutura de dados
import numpy as np #Cálculo e estatísticas
import matplotlib.pyplot as plt #Gráficos
import seaborn  as sns #Gráficos

#plotnine (ggplot)

#Importando dados da internet (CSV)
pnad = pd.read_csv('https://raw.githubusercontent.com/neylsoncrepalde/introducao_ao_python/master/pes_2012.csv')

pnad.shape # Trás as linhas, colunas
pnad.columns # Nome das variáveis
pnad.head() # Primeiros Casos
pnad.dtypes # Tipos das Variáveis

# Trás os dados, o tamanho e o tipo.
pnad['V0101'].head()
pnad.V0101.dtype #Retorna o tipo do númerico. 
pnad.V0101.head() #Sem os colchetes funcionam da mesma forma.

# Altera o tipo da variável para categórica UF:
pnad.UF.head()
pnad.UF = pnad.UF.astype("category")
pnad.UF.dtype

# Altera o tipo da variável para categórica sexo:
pnad.V0302.head()
pnad["sexo"] = pnad.V0302.astype("category")
pnad.V0302.dtype
pnad.sexo.dtype

# Altera o tipo da variável para categórica cor/raça:
pnad.V0404.head()
pnad.V0404.value_counts()
#Subsetting de Sem Declaração : NaN
print(np.NaN)
pnad.loc[9,'V8005'] # Nome da variável (Extrai a décima linha de idade)
pnad.iloc[2,9]  # Index (número) da variável, ou seja, o local da pnad.columns
pnad.loc[pnad["V0404"]== "Sem declaração", "V0404"] = np.nan # Seleciona só as NaN
pnad["V0404"] = pnad.V0404.astype("category")
pnad.V0404.dtype

# Estudando a renda:

pnad.V4720.head()
pnad.loc[pnad["V4720"]== "Sem declaração", "V4720"] = np.nan # Seleciona só as NaN
pnad["renda"] = pnad.V4720.astype("float")
pnad.renda.dtype

m = pnad['renda'].describe()
round(m,2)


# Estudando sexo - Análise viesada, porque no caso da Pnad, precisamos 
# levar em conta o desenho amostral!!!:

pnad.sexo.value_counts() #Retorna o número de valores para variáveis categóricas.
porcentsexo = (pnad.sexo.value_counts()/pnad.sexo.value_counts().sum())*100
porcentsexo.round()

# Estudando idade.
pnad.V8005.describe() #minimo, maximo, quartis, desvio padrão.
pnad.V8005.mean() #Média (não é boa, é viesada)
pnad.V8005.describe().round() # Arrendondando os números
pnad.V8005.describe().round(decimals = 2) # Arrendondando os números
pnad.V8005.var() #variancia
pnad.V8005.std() #desvio padrão
np.average(pnad.V8005, weights = pnad.V4729).round() # Média considerando os pesos amostrais.

# Cor/Raça - Distribuição de frequencia:
cor = pd.crosstab(index=pnad.V0404,
           columns = "Counts")
print(cor)

corpercent = pd.crosstab(index=pnad.V0404,
           columns = "%",
           normalize = True) * 100
print(corpercent)

#Cruzando informações:
cor_sexo = pd.crosstab(index=pnad.V0404,
           columns = pnad.sexo)
print(cor_sexo)

corsexo_percent = pd.crosstab(index=pnad.V0404,
           columns = pnad.sexo,
           normalize = True, margins_name = "Total",
           margins = True) * 100
print("Cruzando informações - Sexo e Cor" + "\n")
print(corsexo_percent.round(3))

# Calculando os percentuais por linhas
corsexo_percent = pd.crosstab(index=pnad.V0404,
           columns = pnad.sexo,
           normalize = "index", margins = True, margins_name = "Total") * 100
print("Cruzando informações - Sexo e Cor" + "\n")
print(corsexo_percent.round(3))

# Calculando os percentuais por colunas
corsexo_percent = pd.crosstab(index=pnad.V0404,
           columns = pnad.sexo,
           normalize = "columns", margins = True, margins_name = "Total") * 100
print("Cruzando informações - Sexo e Cor" + "\n")
print(corsexo_percent.round(3))

# Calculando os percentuais da tabela inteira
corsexo_percent = pd.crosstab(index=pnad.V0404,
           columns = pnad.sexo,
           normalize = "all", margins = True, margins_name = "Total") * 100
print("Cruzando informações - Sexo e Cor" + "\n")
print(corsexo_percent.round(3))

# Gráficos - Sexo

sns.countplot(x=pnad.sexo)
plt.title("Distribuição de sexo no Brasil - 2012")
plt.xlabel("Sexo")
plt.ylabel("Frequência")
plt.show()

sns.countplot(y=pnad.sexo)
plt.title("Distribuição de sexo no Brasil - 2012")
plt.xlabel("Frequência")
plt.ylabel("Sexo")
plt.show()

# Gráficos - Cor/Raça

sns.set(color_codes = True)
sns.countplot(y=pnad.V0404) # Caso queira colocar uma cor só : , color = "c"
plt.title("Distribuição de Cor/Raça no Brasil - 2012")
plt.ylabel("Cor/Raça")
plt.xlabel("Frequência")
plt.show()

# Gráficos - renda

sns.distplot(pnad.renda.dropna())
plt.show()

sns.distplot(pnad.renda.dropna(), kde = False) # Sem densidade
plt.show()

sns.distplot(pnad.renda.dropna(), hist = False) # Somente densidade
plt.show()

fig, ax = plt.subplots()
fig.set_size_inches(8,6)
sns.distplot(pnad.renda.dropna(), hist = False)
plt.show()

#Cruzar uma numérica e uma categórica

sns.boxplot(x = 'V0404', y = 'V8005', data = pnad)
plt.show()


sns.boxplot(y = 'V0404', x = 'V8005', data = pnad)
plt.show()

#Cruzar duas numéricas
# Scatterplot - Gráfico de dispersão

plt.scatter(x = pnad.renda, y = pnad.V8005)
plt.show()

sns.jointplot(x = pnad.renda, y = pnad.V8005)
plt.show()



























