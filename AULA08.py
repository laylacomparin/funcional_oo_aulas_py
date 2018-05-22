################################################
# CENTRO UNIVERSITÁRIO METODISTA IZABELA HENDRIX
# PROGRAMAÇÃO FUNCIONAL ORIENTADA A OBJETOS PYTHON
# Aula 08
# por Layla Comparin
################################################


import pandas as pd
import matplotlib.pyplot as plt
import seaborn  as sns 
import numpy  as np 
import os

os.listdir()

wvs = pd.read_csv("WV6_Data_ascii_v_2015_04_18.dat",
                  header = None)

wvs.shape 
wvs.columns 

# Objetivo do dia:
# Felicidade, Engajamento Politico, Religião
# País: Brasil(76), Canadá(124), Azerbaijão(31), China(156), 
# Latvia (428), Suiça(756)

wvs[10].value_counts() #Felicidade
wvs[10].dtype

##Tira os nan das variáveis
wvs.loc[wvs[10] == -1,10] = np.nan
wvs.loc[wvs[10] == -2,10] = np.nan
wvs.loc[wvs[10] == -5,10] = np.nan

wvs[7].value_counts() #Política
wvs[7].dtype

##Tira os nan das variáveis
wvs.loc[wvs[7] == -1,7] = np.nan
wvs.loc[wvs[7] == -2,7] = np.nan
wvs.loc[wvs[7] == -5,7] = np.nan
wvs.loc[wvs[7] == -3,7] = np.nan

wvs[9].value_counts() #Religião
wvs[9].dtype

##Tira os nan das variáveis
wvs.loc[wvs[9] == -1,9] = np.nan
wvs.loc[wvs[9] == -2,9] = np.nan
wvs.loc[wvs[9] == -5,9] = np.nan

#Plotando o valor da Felicidade usando seaborn
sns.set(color_codes = True)
sns.countplot(y = wvs[10])
plt.title("Valor dado à Felicidade")
plt.xlabel("Felicidade")
plt.ylabel("Frequência")
plt.show()

#Plotando o valor da Política usando seaborn
sns.set(color_codes = True)
sns.countplot(y = wvs[7])
plt.title("Valor dado à Política")
plt.xlabel("Política")
plt.ylabel("Frequência")
plt.show()

#Plotando o valor da Religião usando seaborn
sns.set(color_codes = True)
sns.countplot(y = wvs[9])
plt.title("Valor dado à Religião")
plt.xlabel("Religião")
plt.ylabel("Frequência")
plt.show()

##Médias da Felicidade
felizBrasil = wvs.loc[wvs[1] == 76, 10].mean()
felizChina = wvs.loc[wvs[1] == 156, 10].mean()
felizAzerbaijão = wvs.loc[wvs[1] == 31, 10].mean()
felizEgito = wvs.loc[wvs[1] == 818, 10].mean()

print ("A média de Felicidade do Brasil é " + str(round(felizBrasil,2)))
print ("A média de Felicidade do China é " + str(round(felizChina,2)))
print ("A média de Felicidade do Azerbaijão é " + str(round(felizAzerbaijão,2)))
print ("A média de Felicidade do Egito é " + str(round(felizEgito,2)))

dicFelicidade = {"Brasil": round(felizBrasil,2),
                 "China": round(felizChina,2),
                 "Azerbaijão": round(felizAzerbaijão,2),
                 "Egito": round(felizEgito,2)}

min(dicFelicidade.keys())
max(dicFelicidade.keys())
max(dicFelicidade.values())

print('Menor valor da lista é: ', menor, 'Obj ->', objMenor)

print('O país mais feliz é o '+ min(dicFelicidade)+ '. Sua média de felicidade é ' +str(min(dicFelicidade.values())))

##Médias da Política
polBrasil = wvs.loc[wvs[1] == 76, 7].mean()
polChina = wvs.loc[wvs[1] == 156, 7].mean()
polAzerbaijão = wvs.loc[wvs[1] == 31, 7].mean()
polEgito = wvs.loc[wvs[1] == 818, 7].mean()

print ("A média de Política do Brasil é " + str(round(polBrasil,2)))
print ("A média de Política do China é " + str(round(polChina,2)))
print ("A média de Política do Azerbaijão é " + str(round(polAzerbaijão,2)))
print ("A média de Política do Egito é " + str(round(polEgito,2)))

dicPolitica = {"Brasil": round(polBrasil,2),
               "China": round(polChina,2),
               "Azerbaijão": round(polAzerbaijão,2),
               "Egito": round(polEgito,2)}

min(dicPolitica.keys())
max(dicPolitica.keys())
max(dicPolitica.values())

##Médias da Religião
relBrasil = wvs.loc[wvs[1] == 76, 9].mean()
relChina = wvs.loc[wvs[1] == 156, 9].mean()
relAzerbaijão = wvs.loc[wvs[1] == 31, 9].mean()
relEgito = wvs.loc[wvs[1] == 818, 9].mean()

print ("A média de Religião do Brasil é " + str(round(relBrasil,2)))
print ("A média de Religião do China é " + str(round(relChina,2)))
print ("A média de Religião do Azerbaijão é " + str(round(relAzerbaijão,2)))
print ("A média de Religião do Egito é " + str(round(relEgito,2)))

dicReligiao = {"Brasil": round(relBrasil,2),
               "China": round(relChina,2),
               "Azerbaijão": round(relAzerbaijão,2),
               "Egito": round(relEgito,2)}

min(dicReligiao.keys())
max(dicReligiao.keys())
max(dicReligiao.values())






























felicidadePaises = pd.crosstab(wvs[felizBrasil],wvs[felizChina], wvs[felizAzerbaijão], wvs[felizEgito])
print("Cruzando informações - Felicidade" + "\n")
print(felicidadePaises)



















