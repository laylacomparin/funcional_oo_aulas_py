"""
CENTRO UNIVERSITÁRIO METODISTA IZABELA HENDRIX
PROGRAMAÇÃO FUNCIONAL ORIENTADA A OBJETOS PYTHON
Aula 03
por Layla Comparin
"""

# Atributo são nome, idade, raça...
# Método são as funções em negrito. 
# Self - Remete a tudo que for da classe Cachorro. (Init é um método - construtor.)

class Cachorro:
  def __init__(self, n, d, r):  
      self.nome = n
      self.datanasc = d
      self.raca = r
      self.temOsso = False
      
  def latir(self):
      print("Au, Au!")
      
  def comandos(self, acao):
      if(acao == "Dá a pata!"):
          print("Toma a patinha... ")
      if(acao == "Deita!"):
          print("Estou deitado. Au! Au!")
      if(acao == "Pula!"):
          print("Estou pulando.. ")
          
  def pegaOsso(self):
      if self.temOsso:
          print("Já tenho osso!")
      else:
          self.temOsso = True
          print("Humm.. Que osso gostoso!")

  def largaOsso(self):
      if self.temOsso:
         self.temOsso = False
         print("Larguei o osso!")
      else:
         print("Osso? Onde??")