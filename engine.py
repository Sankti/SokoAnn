import pygame, sys
from pygame.locals import *
from settings import *

sprite_player = pygame.image.load('player.png')
sprite_player = pygame.transform.scale(sprite_player, (TILESIZE, TILESIZE))
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
    [0, 0, 0, 0, 0, 0, 9, 1, 0, 2, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 9, 9, 9, 0, 2, 1, 9, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 9, 1, 9, 9, 2, 0, 9, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 9, 0, 9, 0, 1, 0, 9, 9, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 9, 2, 0, 3, 2, 2, 1, 9, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 1, 0, 0, 9, 0, 0, 0, 0, 0, 0],
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
            level_map.append(cell)
    return level_map

class Player():
    """
    Defines starting position and later positions of the player.
    row - int, position on x axis
    column - int, position on y axis
    level - matrix, level to be summoned on
    """
    def __init__(self, column, row, level):
        self.row = int(row)
        self.column = int(column)
        self.level = level

    def move(self, direction):
        if direction == "LEFT":
            if self.can_move("LEFT") == True:
                self.push("LEFT")
                self.row -= 1
                drawMap(createMap(self.level))
                win(check_win(self.level))

        elif direction == "UP":
            if self.can_move("UP") == True:
                self.push("UP")
                self.column -= 1
                drawMap(createMap(self.level))
                win(check_win(self.level))

        elif direction == "DOWN":
            if self.can_move("DOWN") == True:
                self.push("DOWN")
                self.column += 1
                drawMap(createMap(self.level))
                win(check_win(self.level))

        elif direction == "RIGHT":
            if self.can_move("RIGHT") == True:
                self.push("RIGHT")
                self.row += 1
                drawMap(createMap(self.level))
                win(check_win(self.level))

    def can_move(self, direction):
        if direction == "LEFT":
            destination_x = self.get_column()
            destination_y = self.get_row() - 1
            pushed_x = self.get_column()
            pushed_y = self.get_row() -2
            if self.level[destination_x][destination_y] in (2, 3) and self.level[pushed_x][pushed_y] in (2, 3, 9):
                return False
            elif self.level[destination_x][destination_y] != 9:
                return True
            else:
                return False

        elif direction == "UP":
            destination_x = self.get_column() - 1
            destination_y = self.get_row()
            pushed_x = self.get_column() - 2
            pushed_y = self.get_row()
            if self.level[destination_x][destination_y] in (2, 3) and self.level[pushed_x][pushed_y] in (2, 3, 9):
                return False
            elif self.level[destination_x][destination_y] != 9:
                return True
            else:
                return False

        elif direction == "DOWN":
            destination_x = self.get_column() + 1
            destination_y = self.get_row()
            pushed_x = self.get_column() + 2
            pushed_y = self.get_row()
            if self.level[destination_x][destination_y] in (2, 3) and self.level[pushed_x][pushed_y] in (2, 3, 9):
                return False
            elif self.level[destination_x][destination_y] != 9:
                return True
            else:
                return False

        elif direction == "RIGHT":
            destination_x = self.get_column()
            destination_y = self.get_row() + 1
            pushed_x = self.get_column()
            pushed_y = self.get_row() + 2
            if self.level[destination_x][destination_y] in (2, 3) and self.level[pushed_x][pushed_y] in (2, 3, 9):
                return False
            elif self.level[destination_x][destination_y] != 9:
                return True
            else:
                return False

    def push(self, direction):
        if direction == "LEFT":
            destination_x = self.get_column()
            destination_y = self.get_row() - 1
            pushed_x = self.get_column()
            pushed_y = self.get_row() - 2
            if self.level[destination_x][destination_y] == 2 and self.level[pushed_x][pushed_y] == 1:
                self.level[destination_x][destination_y] = 0
                self.level[pushed_x][pushed_y] = 3
            elif self.level[destination_x][destination_y] == 2 and self.level[pushed_x][pushed_y] != 9:
                self.level[destination_x][destination_y] = 0
                self.level[pushed_x][pushed_y] = 2
            elif self.level[destination_x][destination_y] == 3 and self.level[pushed_x][pushed_y] != 9:
                self.level[destination_x][destination_y] = 1
                self.level[pushed_x][pushed_y] = 2

        elif direction == "UP":
            destination_x = self.get_column() - 1
            destination_y = self.get_row()
            pushed_x = self.get_column() - 2
            pushed_y = self.get_row()
            if self.level[destination_x][destination_y] == 2 and self.level[pushed_x][pushed_y] == 1:
                self.level[destination_x][destination_y] = 0
                self.level[pushed_x][pushed_y] = 3
            elif self.level[destination_x][destination_y] == 2 and self.level[pushed_x][pushed_y] != 9:
                self.level[destination_x][destination_y] = 0
                self.level[pushed_x][pushed_y] = 2
            elif self.level[destination_x][destination_y] == 3 and self.level[pushed_x][pushed_y] != 9:
                self.level[destination_x][destination_y] = 1
                self.level[pushed_x][pushed_y] = 2

        elif direction == "DOWN":
            destination_x = self.get_column() + 1
            destination_y = self.get_row()
            pushed_x = self.get_column() + 2
            pushed_y = self.get_row()
            if self.level[destination_x][destination_y] == 2 and self.level[pushed_x][pushed_y] == 1:
                self.level[destination_x][destination_y] = 0
                self.level[pushed_x][pushed_y] = 3
            elif self.level[destination_x][destination_y] == 2 and self.level[pushed_x][pushed_y] != 9:
                self.level[destination_x][destination_y] = 0
                self.level[pushed_x][pushed_y] = 2
            elif self.level[destination_x][destination_y] == 3 and self.level[pushed_x][pushed_y] != 9:
                self.level[destination_x][destination_y] = 1
                self.level[pushed_x][pushed_y] = 2

        elif direction == "RIGHT":
            destination_x = self.get_column()
            destination_y = self.get_row() + 1
            pushed_x = self.get_column()
            pushed_y = self.get_row() + 2
            if self.level[destination_x][destination_y] == 2 and self.level[pushed_x][pushed_y] == 1:
                self.level[destination_x][destination_y] = 0
                self.level[pushed_x][pushed_y] = 3
            elif self.level[destination_x][destination_y] == 2 and self.level[pushed_x][pushed_y] != 9:
                self.level[destination_x][destination_y] = 0
                self.level[pushed_x][pushed_y] = 2
            elif self.level[destination_x][destination_y] == 3 and self.level[pushed_x][pushed_y] != 9:
                self.level[destination_x][destination_y] = 1
                self.level[pushed_x][pushed_y] = 2

    def get_row(self):
        return self.row

    def get_column(self):
        return self.column

def drawMap(level_map):
    """
    Used to print graphical representation
    of a level map, using tiles.
    level_map - matrix, result of createMap(level)
    """
    for tile in level_map:
        coord_x = int(tile[0] * TILESIZE)
        coord_y = int(tile[1] * TILESIZE)
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
    
    ROOT.blit(sprite_player, (ann.get_row() * TILESIZE, ann.get_column() * TILESIZE))

def check_win(level):
    unlit_orbs = 0
    for row in level:
        for cell in row:
            if cell == 2:
                unlit_orbs += 1
    if unlit_orbs == 0:
        return True
    else:
        return False

def win(boolean):
    if boolean == False:
        pass
    elif boolean == True:
        prompt = pygame.font.SysFont("monospace", 48).render("Maciej pokonany!", 1, WHITE)
        ROOT.blit(prompt, (TEXT_INDENT, 50))
        pygame.draw.rect(ROOT, WHITE, (30, 195, 580, 110))
        pygame.draw.rect(ROOT, BLACK, (35, 200, 570, 100))
        line1 = pygame.font.SysFont("monospace", 32).render("Kolejny poziom: wciśnij ENTER", 1, WHITE)
        line2 = pygame.font.SysFont("monospace", 32).render("Powrót do menu: wciśnij Z", 1, WHITE)
        ROOT.blit(line1, (40, 205))
        ROOT.blit(line2, (40, 245))

def next_level(level):
    pass

# Starting Position
ann = Player(7, 8, level1)
drawMap(createMap(level1))

# while True:
#     pygame.time.delay(100)

#     for event in pygame.event.get():
#         if event.type == QUIT:
#             pygame.quit()
#             sys.exit()

#     KEYS = pygame.key.get_pressed()

#     if KEYS[pygame.K_UP]:
#         ann.move("UP")
#     if KEYS[pygame.K_LEFT]:
#         ann.move("LEFT")
#     if KEYS[pygame.K_RIGHT]:
#         ann.move("RIGHT")
#     if KEYS[pygame.K_DOWN]:
#         ann.move("DOWN")

#     pygame.display.update()
#     fpsClock.tick(FPS)