import pygame
from pygame.locals import *
from settings import *

sprite_empty = pygame.image.load('empty.png')
sprite_empty = pygame.transform.scale(sprite_empty, (TILESIZE, TILESIZE))
sprite_wall = pygame.image.load('wall.png')
sprite_wall = pygame.transform.scale(sprite_wall, (TILESIZE, TILESIZE))
sprite_socket = pygame.image.load('socket.png')
sprite_socket = pygame.transform.scale(sprite_socket, (TILESIZE, TILESIZE))
sprite_orb_unlit = pygame.image.load('orb_unlit.png')
sprite_orb_unlit = pygame.transform.scale(sprite_orb_unlit, (TILESIZE, TILESIZE))
sprite_orb = pygame.image.load('orb.png')
sprite_orb = pygame.transform.scale(sprite_orb, (TILESIZE, TILESIZE))

pygame.init()
ROOT = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Engine")

level1 = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 9, 9, 9, 9, 9, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 9, 9, 9, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 9, 9, 9, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 9, 0, 9, 9, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 9, 0, 9, 0, 0, 0, 9, 9, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 9, 9, 9, 9, 9, 9, 9, 9, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

def createMap(level):
    """
    Used to draw a level map: collection of
    coordinates and types of tiles.
    level - matrix, definition of a level.
    """
    level_map = []
    for column in range(0, GRID_WIDTH):
        column_raw = level[column]
        for row in range(0, GRID_HEIGHT):
            cell = [row, column, column_raw[row]]
            print(cell)
            level_map.append(cell)
    return level_map

def drawMap(level_map):
    """
    Used to print graphical representation
    of a level map, using tiles.
    level_map - matrix, result of createMap(level)
    """
    for tile in level_map:
        coord_x = int(tile[0] * TILESIZE)
        coord_y = int(tile[1] * TILESIZE)
        print (str(tile) + "Coords: X " + str(coord_x) + " Y " + str(coord_y))
        if tile[2] == 0:
            ROOT.blit(sprite_empty, (coord_x, coord_y))
        elif tile[2] == 1:
            ROOT.blit(sprite_socket, (coord_x, coord_y))
        elif tile[2] == 2:
            ROOT.blit(sprite_orb_unlit, (coord_x, coord_y))
        elif tile[2] == 3:
            ROOT.blit(sprite_orb, (coord_x, coord_y))
        elif tile[2] == 9:
            ROOT.blit(sprite_wall, (coord_x, coord_y))

maps = createMap(level1)
drawMap(maps)

while True:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FPS)
