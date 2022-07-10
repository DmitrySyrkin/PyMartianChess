import pygame
from MartianField import MartianField
from MartianPiece import MartianPiece 

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class MartianBoard:
    def __init__(self, screen):
        self._screen = screen
        self._fields : list[MartianField] = []
        self._font = pygame.font.Font(None, 48)

    def draw(self, currentPlayer, pieces: list[MartianPiece], endOfGame: bool):
      self._screen.fill(BLACK)
  
      if not endOfGame:
        label = self._font.render('Player: ' + ('GRAY' if currentPlayer == 0 else 'GREEN'), True, WHITE)
        self._screen.blit(label, (360, 20))

      score = ' ' + str(self.getScore(pieces, 0)) + ' : ' + str(self.getScore(pieces, 1)) + ' '
      scoreLabel = self._font.render(score, True, BLACK, WHITE)
      self._screen.blit(scoreLabel, (360, 80))
      
      if endOfGame:
        endOfGameLabel = self._font.render('GAME OVER', True, WHITE, BLACK)
        self._screen.blit(endOfGameLabel, (360, 120))

      self.fields.clear()
      for row in range(0,8):
        for column in range(0,4):
          field = MartianField(self._screen, row, column)
          field.draw()
          self.fields.append(field)
      pygame.display.flip()

    def getScore(self, pieces: list[MartianPiece], player: int):
        if pieces == None or pieces.count == 0:
            return 0
        score = 0
        for piece in pieces:
            if piece._isCapturedByPlayer == player:
                score = score + piece.points
        return score

    @property
    def fields(self):
        return self._fields

