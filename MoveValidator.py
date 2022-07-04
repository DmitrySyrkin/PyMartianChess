import pygame
from MartianField import MartianField
from MartianPiece import MartianPiece 

class MoveValidator:

    def IsValidMove(self, selectedPiece: MartianPiece, field: MartianField, pieces: list[MartianPiece]):
      
      if selectedPiece.pieceType == 'Pawn':
        return max(selectedPiece.row, field.row) - min(selectedPiece.row, field.row) == 1 \
              and max(selectedPiece.column, field.column) - min(selectedPiece.column, field.column) == 1

      return True