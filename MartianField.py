import pygame

PALEGREEN3 = (124,205,124)
PALEGREEN4 = (84,139,84)
PALETURQUOISE3 = (150,205,205)
PALETURQUOISE4 = (102,139,139)

class MartianField:

    def __init__(self, screen, row, column):
        self._screen = screen
        self._row = row
        self._column = column
        self._bounds = None

    def draw(self):
        if self._row > 3:
          color = PALETURQUOISE3 if (self._row + self._column) % 2 == 0 else PALETURQUOISE4
        else:
          color = PALEGREEN3 if (self._row + self._column) % 2 == 0 else PALEGREEN4
        self._bounds = pygame.draw.rect(self._screen, color, pygame.Rect(self._column * 60, self._row * 60, 60, 60))

    def collidepoint(self, pos):
        return self._bounds.collidepoint(pos)

    @property
    def row(self):
        return self._row

    @property
    def column(self):
        return self._column