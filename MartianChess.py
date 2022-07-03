import pygame
import sys

from MartianPiece import MartianPiece
from MoveValidator import MoveValidator

WIDTH = 640
HEIGHT = 640

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Martian chess v 0.0.1")
font = pygame.font.Font(None, 48)
validator = MoveValidator()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
PINK = (255,192,203)
GREEN = (0, 255, 0)
PALEGREEN3 = (124,205,124)
PALEGREEN4 = (84,139,84)
PALETURQUOISE3 = (150,205,205)
PALETURQUOISE4 = (102,139,139)

class MartianChess(object):
  fields : list[pygame.Rect] = []

  pieces : list[MartianPiece] = []
  currentPlayer = 0
  
  def draw_board(self):
    screen.fill(BLACK)
  
    label = font.render('Player: ' + ('GRAY' if self.currentPlayer == 0 else 'GREEN'), True, WHITE)
    screen.blit(label, (360, 20))
  
    self.fields.clear()
    for row in range(0,8):
      for col in range(0,4):
        if row > 3:
          color = PALETURQUOISE3 if (row+col) % 2 == 0 else PALETURQUOISE4
        else:
          color = PALEGREEN3 if (row+col) % 2 == 0 else PALEGREEN4
        field = pygame.draw.rect(screen, color, pygame.Rect(col*60, row*60, 60, 60))
        self.fields.append(field)
    pygame.display.flip()
  
  def init_position(self):
      self.draw_board()
      for pos in [(0,0), (0,1), (1,0), (3,7), (2,7), (3,6)]:
        piece = MartianPiece(screen, pos, 20)
        piece.draw()
        self.pieces.append(piece)
      for pos in [(0,2), (1,1), (2,0), (2,6),(1,7),(3,5)]:
        piece = MartianPiece(screen, pos, 15)
        piece.draw()
        self.pieces.append(piece)
      for pos in  [(1,2), (2,1), (2,2), (1,6),(2,5),(1,5)]:
        piece = MartianPiece(screen, pos, 10)
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
            for field in self.fields:
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
                  selectedPiece.move(clickedField.centerx, clickedField.centery)
                  self.currentPlayer = 1 - self.currentPlayer         
                  self.update_position()

            # capture piece
            elif clickedField != None \
                and selectedPiece != None \
                and pieceOnClickedField != None \
                and not pieceOnClickedField.belongsToPlayer(self.currentPlayer) \
                and validator.IsValidMove(selectedPiece, clickedField, self.pieces):
                  selectedPiece.select(False)
                  selectedPiece.move(clickedField.centerx, clickedField.centery)
                  pieceOnClickedField.capture(self.currentPlayer)
                  self.currentPlayer = 1 - self.currentPlayer         
                  self.update_position()

chess = MartianChess()
chess.Run()