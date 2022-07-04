import pygame

PURPLE = (128,0,128)
BANANA = (227,207,87)

PAWN = 'Pawn'
DRONE = 'Drone'
QUEEN = 'Queen'

class MartianPiece:
    def __init__(self, screen, position, pieceType, isSelected = False, isCapturedByPlayer = None):
        self._bounds = None        
        self._screen = screen
        self._pieceType = pieceType
        self._isSelected = isSelected              
        self._isCapturedByPlayer = isCapturedByPlayer
        self._position = position

    def draw(self):
        if self._isCapturedByPlayer == None:          
          self._bounds = pygame.draw.circle(self._screen, self.color, self.center, self.radius)

    def collidepoint(self, point):
        if self._isCapturedByPlayer != None \
           or self._bounds == None:
           return False

        if self._bounds.collidepoint(point):
            return True
        
        rect = pygame.rect.Rect(self.center[0] - 30, self.center[1] - 30, 60, 60)
        return rect.collidepoint(point)

    def select(self, isSelected):
        self._isSelected = isSelected
 
    def move(self, column, row):
      self._position = (column, row) 

    def capture(self, currentPlayer):
        self._isCapturedByPlayer = currentPlayer       

    def belongsToPlayer(self, currentPlayer: int):
        return self.row > 3 if currentPlayer == 0 else self.row < 4

    @property
    def isSelected(self):
        return self._isCapturedByPlayer == None and self._isSelected == True 

    @property
    def color(self):
        return BANANA if self.isSelected else PURPLE    

    @property
    def radius(self):
        return 10 if self._pieceType == PAWN  \
             else (15 if self._pieceType == DRONE \
                else ( 20 if self._pieceType == QUEEN else None))

    @property
    def row(self):
        return self._position[1]

    @property
    def column(self):
        return self._position[0]

    @property
    def center(self):
        return self.column * 60 + 30, self.row * 60 + 30

    @property
    def pieceType(self):
        return self._pieceType