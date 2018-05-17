################################################
# CENTRO UNIVERSITÁRIO METODISTA IZABELA HENDRIX
# PROGRAMAÇÃO FUNCIONAL ORIENTADA A OBJETOS PYTHON
# Aula 07
# por Layla Comparin
################################################


import pandas as pd
import matplotlib.pyplot as plt
import seaborn  as sns 
import numpy  as np 
import os
from scipy import stats

os.listdir()

wvs = pd.read_csv("WV6_Data_ascii_v_2015_04_18.dat",
                  header = None)

wvs.shape 
wvs.columns 

######### Separando as variáveis para análise
#### Familia, Amigos, Tempo Livre, Politica, Trabalho e Religião

wvs[4].value_counts() #Familia
wvs[4].dtype

##Tira os nan das variáveis
wvs.loc[wvs[4] == -1,4] = np.nan
wvs.loc[wvs[4] == -2,4] = np.nan
wvs.loc[wvs[4] == -5,4] = np.nan


wvs[7].value_counts() #Politica
wvs[7].dtype

##Tira os nan das variáveis
wvs.loc[wvs[7] == -1,7] = np.nan
wvs.loc[wvs[7] == -2,7] = np.nan
wvs.loc[wvs[7] == -3,7] = np.nan
wvs.loc[wvs[7] == -5,7] = np.nan


#Plotando o valor da familia usando seaborn
sns.set(color_codes = True)
sns.countplot(y = wvs[4])
plt.title("Valor dado à Família")
plt.xlabel("Família")
plt.ylabel("Frequência")
plt.show()

#Plotando o valor da familia usando matplotlib
plt.bar(x = wvs[4], height = wvs[7])
plt.title("Valor dado à Família")
plt.xlabel("Família")
plt.ylabel("Frequência")
plt.show()

#Plotando o valor da familia usando panda
wvs[4].value_counts().plot(kind = "bar")
plt.title("Valor dado à Família")
plt.xlabel("Família")
plt.ylabel("Frequência")
plt.show()

## Plotando politica
sns.set(color_codes = True)
sns.countplot(y = wvs[7])
plt.title("Valor dado à Politica")
plt.xlabel("Família")
plt.ylabel("Frequência")
plt.show()


# Teste correlação familia e politica
fampol = pd.crosstab(wvs[4],wvs[7])
print("Cruzando informações - Familia e Politica" + "\n")
print(fampol)


# Teste correlação familia e politica
fampol = pd.crosstab(wvs[4],wvs[7])
print("Cruzando informações - Familia e Politica" + "\n")
print(fampol)


# ---
chi2, p, dof, expec = stats.chi2_contingency(fampol)
print("Chi-square: " + str(chi2))
print("P-value: " + str(p))
print("Degrees of Freedom: " + str(dof))
















