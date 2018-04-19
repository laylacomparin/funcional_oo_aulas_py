"""
CENTRO UNIVERSITÁRIO METODISTA IZABELA HENDRIX
PROGRAMAÇÃO FUNCIONAL ORIENTADA A OBJETOS PYTHON
Aula 02.1
por Layla Comparin

"""

""" from Script import Classe """

from Cachorro import Cachorro

dog1 = Cachorro('Totó', 2, 'Vira-Lata')

print("Meu nome é : " + dog1.nome)
dog1.latir()
print("Sou da raça: " + dog1.raca)
dog1.latir()
print("Tenho: " + str(dog1.idade) + " anos")
dog1.comandos("Fiz Aniversário!")

