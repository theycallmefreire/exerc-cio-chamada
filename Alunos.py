from Pessoas import Pessoas

class Alunos(Pessoas):
  def __init__(self, presenca, nota, id, nome):
    self.presenca = presenca
    self.nota = nota
    super().__init__(id, nome)

  def media(self):
    if self.nota == 6:
      print("passou miseravi")
    else:
      print("reprovou burro")