import pygame

PURPLE = (128,0,128)
BANANA = (227,207,87)

class MartianPiece:
    def __init__(self, screen, center, radius, isSelected = False, isCapturedByPlayer = None):
        self._bounds = None        
        self._screen = screen
        self._center = (center[0] * 60 + 30, center[1] * 60 + 30)        
        self._radius = radius
        self._isSelected = isSelected              
        self._isCapturedByPlayer = isCapturedByPlayer

    def draw(self):
        if self._isCapturedByPlayer == None:
          self._bounds = pygame.draw.circle(self._screen, self.color, self._center, self._radius)

    def collidepoint(self, point):
        return self._bounds != None and self._bounds.collidepoint(point)

    def select(self, isSelected):
        self._isSelected = isSelected
 
    def move(self, x, y):
      self._center = (x, y) 

    def capture(self, currentPlayer):
        self._isCapturedByPlayer = currentPlayer

    def belongsToPlayer(self, currentPlayer: int):
        row = (self._center[1] - 30) / 60
        return row > 3 if currentPlayer == 0 else row < 4

    @property
    def isSelected(self):
        return self._isSelected == True 

    @property
    def color(self):
        return BANANA if self.isSelected else PURPLE    
