from Alunos import Alunos

class Chamada(Alunos):
  def __init__(self, presenca, nota, id, nome):
    super().__init__(presenca, nota, id, nome)

  def media(self):
    if self.nota > 4:
      print("passou miseravi")
    else:
      print("reprovou burro")