"""
CENTRO UNIVERSITÁRIO METODISTA IZABELA HENDRIX
PROGRAMAÇÃO FUNCIONAL ORIENTADA A OBJETOS PYTHON
Aula 02.1
por Layla Comparin

"""

""" from Script import Classe """

from Cachorro import Cachorro
from datetime import date
from datetime import datetime

dog1 = Cachorro('Totó', "11/Feb/2014", 'Vira-Lata')

datanasc = datetime.strptime(dog1.datanasc, '%d/%b/%Y')
today = date.today()
age = today.year - datanasc.year - ((today.month, today.day) < (datanasc.month, datanasc.day))


print("Meu nome é : " + dog1.nome)
dog1.latir()
print("Sou da raça: " + dog1.raca)
dog1.latir()
print("Tenho: " + str(age) + " anos")



