"""
CENTRO UNIVERSITÁRIO METODISTA IZABELA HENDRIX
PROGRAMAÇÃO FUNCIONAL ORIENTADA A OBJETOS PYTHON
Aula 03.1
por Layla Comparin
"""

""" from Script import Classe """

from Cachorro import Cachorro
from datetime import date
from datetime import datetime

dog1 = Cachorro('Totó', "11/Feb/2010", 'Vira-Lata')

datanasc = datetime.strptime(dog1.datanasc, '%d/%b/%Y')
today = date.today()
age = today.year - datanasc.year

# Acessando os atributos do meu cachorro. Métodos são acessados com parenteses. 

print(f"Meu nome é : {dog1.nome}")
dog1.latir()
print(f"Sou da raça: {dog1.raca}")
dog1.latir()
print(f"Tenho: {age} anos")
dog1.comandos("Dá a pata!")
dog1.pegaOsso()
dog1.pegaOsso()
dog1.largaOsso()
dog1.largaOsso()

