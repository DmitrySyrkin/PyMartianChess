import pygame
import sys
from MartianBoard import MartianBoard

import MartianField
from MartianPiece import MartianPiece, PAWN, DRONE, QUEEN
from MoveValidator import MoveValidator

WIDTH = 640
HEIGHT = 640

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Martian chess v 0.0.1")

validator = MoveValidator()

RED = (255, 0, 0)
PINK = (255,192,203)
GREEN = (0, 255, 0)


class MartianChess(object):
  board : MartianBoard = None
  pieces : list[MartianPiece] = []
  currentPlayer = 0
  
  def draw_board(self):
     self.board = MartianBoard(screen)
     self.board.draw(self.currentPlayer, self.pieces)
  
  def init_position(self):
      self.draw_board()
      for pos in [(0,0), (0,1), (1,0), (3,7), (2,7), (3,6)]:
        piece = MartianPiece(screen, pos, QUEEN)
        piece.draw()
        self.pieces.append(piece)
      for pos in [(0,2), (1,1), (2,0), (2,6),(1,7),(3,5)]:
        piece = MartianPiece(screen, pos, DRONE)
        piece.draw()
        self.pieces.append(piece)
      for pos in  [(1,2), (2,1), (2,2), (1,6),(2,5),(1,5)]:
        piece = MartianPiece(screen, pos, PAWN)
        piece.draw()
        self.pieces.append(piece)
      pygame.display.update()
  
  def update_position(self):      
      self.draw_board()
      for piece in self.pieces:
        piece.draw()
      pygame.display.update()
      
  def Run(self):
    self.init_position()
  
    while True:  
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()     
               
          elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            
            selectedPiece = None
            for piece in self.pieces:
             if piece.isSelected:
               selectedPiece = piece
               break
            
            clickedField = None
            for field in self.board.fields:
              if field.collidepoint(pygame.mouse.get_pos()):
                 clickedField = field
                 break

            pieceOnClickedField = None   
            for piece in self.pieces:
              if piece.collidepoint(pygame.mouse.get_pos()):
                 pieceOnClickedField = piece
                 break

            # select piece
            if clickedField != None \
              and selectedPiece == None \
              and pieceOnClickedField != None \
              and pieceOnClickedField.belongsToPlayer(self.currentPlayer):
                pieceOnClickedField.select(True)
                self.update_position()  

            # change selection
            elif clickedField != None \
              and selectedPiece != None \
              and pieceOnClickedField != None \
              and selectedPiece.belongsToPlayer(self.currentPlayer) \
              and pieceOnClickedField.belongsToPlayer(self.currentPlayer):
                pieceOnClickedField.select(True)
                selectedPiece.select(False)
                self.update_position()

            # move piece
            elif clickedField != None \
                and selectedPiece != None \
                and pieceOnClickedField == None \
                and validator.IsValidMove(selectedPiece, clickedField, self.pieces):
                  selectedPiece.select(False)
                  selectedPiece.move(clickedField.column, clickedField.row)
                  self.currentPlayer = 1 - self.currentPlayer         
                  self.update_position()

            # capture piece
            elif clickedField != None \
                and selectedPiece != None \
                and pieceOnClickedField != None \
                and not pieceOnClickedField.belongsToPlayer(self.currentPlayer) \
                and validator.IsValidMove(selectedPiece, clickedField, self.pieces):
                  selectedPiece.select(False)
                  selectedPiece.move(clickedField.column, clickedField.row)
                  pieceOnClickedField.capture(self.currentPlayer)
                  self.currentPlayer = 1 - self.currentPlayer         
                  self.update_position()

chess = MartianChess()
chess.Run()