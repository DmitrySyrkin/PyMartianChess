import pygame
from MartianPiece import MartianPiece 

class MoveValidator:

    def IsValidMove(self, selectedPiece: MartianPiece, field: pygame.Rect, pieces: list[MartianPiece]):
      return True