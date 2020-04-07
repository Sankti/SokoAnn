import pygame
from pygame.locals import *

FPS = 60
fpsClock = pygame.time.Clock()

# Window Dimensions
WIDTH = 640
HEIGHT = 480

# Text Indent
TEXT_INDENT = WIDTH / 6

# Colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (129, 187, 129)
GRAY = (225, 225, 225)

# Tileset
TILESIZE = 32
GRID_WIDTH = int(WIDTH / TILESIZE) #20
GRID_HEIGHT = int(HEIGHT / TILESIZE) #15