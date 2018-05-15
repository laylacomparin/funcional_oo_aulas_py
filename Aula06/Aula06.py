################################################
# CENTRO UNIVERSITÁRIO METODISTA IZABELA HENDRIX
# PROGRAMAÇÃO FUNCIONAL ORIENTADA A OBJETOS PYTHON
# Aula 06
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


wvs[1].value_counts()
wvs[1].dtype

wvs.loc[(wvs[1] == 76) |
        (wvs[1] == 12),1].value_counts()

wvs[9].value_counts()

#Tira os nan das variáveis se é feliz
wvs.loc[wvs[9] == -2,9] = np.nan
wvs.loc[wvs[9] == -5,9] = np.nan
wvs.loc[wvs[9] == -1,9] = np.nan

round((wvs[9].value_counts()/wvs[9].value_counts().sum()) * 100,2)


wvs.loc[wvs[1] == 76, 9].value_counts()

round((wvs.loc[wvs[1] == 76, 9].value_counts()/\
       wvs.loc[wvs[1] == 76, 9].value_counts().sum()) * 100,2)

round((wvs.loc[wvs[1] == 840, 9].value_counts()/\
       wvs.loc[wvs[1] == 840, 9].value_counts().sum()) * 100,2)


# No Anaconda Prompt:
pip install -U ggplot

from ggplot import *

ggplot(wvs, aes(x=9))+geom_bar()

wvs[9] = wvs[9].astype("category")

sns.barplot(wvs[9].value_counts())















