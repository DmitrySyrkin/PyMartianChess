from lib2to3.pgen2.driver import Driver
import pygame
from MartianField import MartianField
from MartianPiece import MartianPiece, PAWN, DRONE, QUEEN

class MoveValidator:

    def IsValidMove(self, selectedPiece: MartianPiece, field: MartianField, pieces: list[MartianPiece]):
      
      if selectedPiece.pieceType == PAWN:
      # One space at a time, in any of the diagonal directions
        return max(selectedPiece.row, field.row) - min(selectedPiece.row, field.row) == 1 \
              and max(selectedPiece.column, field.column) - min(selectedPiece.column, field.column) == 1

      if selectedPiece.pieceType == DRONE:
      #  One or two spaces, on either the horizontal or vertical lines. Jumping is not allowed.
        if selectedPiece.row == field.row and max(selectedPiece.column, field.column) - min(selectedPiece.column, field.column) == 1:
          return True
        
        if selectedPiece.column == field.column and max(selectedPiece.row, field.row) - min(selectedPiece.row, field.row) == 1:
          return True
        
        if selectedPiece.row == field.row \
          and max(selectedPiece.column, field.column) - min(selectedPiece.column, field.column) == 2 \
          and self.fieldIsEmpty(min(selectedPiece.column, field.column) + 1, selectedPiece.row, pieces):
          return True

        if selectedPiece.column == field.column \
          and max(selectedPiece.row, field.row) - min(selectedPiece.row, field.row) == 2 \
          and self.fieldIsEmpty(selectedPiece.column, min(selectedPiece.row, field.row) + 1, pieces):
          return True
        
        return False

      return True

    def fieldIsEmpty(self, column: int, row: int, pieces: list[MartianPiece]):
        for piece in pieces:
          if piece.column == column and piece.row == row:
            return False
        return True    