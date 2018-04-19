"""
CENTRO UNIVERSITÁRIO METODISTA IZABELA HENDRIX
PROGRAMAÇÃO FUNCIONAL ORIENTADA A OBJETOS PYTHON
Aula 02
por Layla Comparin

"""

# Atributo são nome, idade, raça...
# Método são as funções. 
# Self - Remete a tudo que for da classe Cachorro. (Init é um método - construtor.)

class Cachorro:
  def __init__(self, n, i, r):  
      self.nome = n
      self.idade = i
      self.raca = r
      
  def latir(self):
      print("Au, Au!")
      
  def comandos(self, acao):
      if(acao == "Dá a pata!"):
          print("Toma a patinha... ")
      if(acao == "Deita!"):
          print("Estou deitado. Au! Au!")
      if(acao == "Pula!"):
          print("Estou pulando.. ")
      if(acao == "Fiz Aniversário!"):
          self.idade += 1
          print('Agora eu tenho ' + str(self.idade) + ' anos!')
