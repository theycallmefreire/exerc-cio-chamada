# pessoas(id, nome)
#   alunos(id,nome, presença, nota)
#     chamada(nome, presença)
class Pessoas:
  def __init__(self, id, nome):
    self.id = id
    self.nome = nome

class Alunos(Pessoas):
  def __init__(self, presenca, nota, id, nome):
    self.presenca = presenca
    self.nota = nota

# class Chamada:
  