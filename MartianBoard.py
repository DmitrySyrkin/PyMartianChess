import pygame
from MartianField import MartianField 

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class MartianBoard:
    def __init__(self, screen):
        self._screen = screen
        self._fields : list[MartianField] = []
        self._font = pygame.font.Font(None, 48)

    def draw(self, currentPlayer):
      self._screen.fill(BLACK)
  
      label = self._font.render('Player: ' + ('GRAY' if currentPlayer == 0 else 'GREEN'), True, WHITE)
      self._screen.blit(label, (360, 20))
  
      self.fields.clear()
      for row in range(0,8):
        for column in range(0,4):
          field = MartianField(self._screen, row, column)
          field.draw()
          self.fields.append(field)
      pygame.display.flip()

    @property
    def fields(self):
        return self._fields