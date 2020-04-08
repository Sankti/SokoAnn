"""
Game by Sankti Goździelewski
    github.com/Sankti
Made in Cracow, March - April 2020
"""
import pygame, sys
from pygame.locals import *
from settings import *
from levels import *

# PYGAME Initialization
pygame.init()
ROOT = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SokoAnn")
KEYS = pygame.key.get_pressed()

# Fonts
font_large = pygame.font.SysFont("monospace", 48)
font_medium = pygame.font.SysFont("monospace", 32)
font_small = pygame.font.SysFont("monospace", 12)

# Graphics
logo = pygame.image.load('graphics\\logo.png').convert()
image_rubens_full = pygame.image.load('graphics\\Rubens.png')
image_rubens_medium = pygame.transform.scale(image_rubens_full, (100, 100))
image_rubens = pygame.transform.scale(image_rubens_full, (30, 30))
pygame.display.set_icon(image_rubens)

# Music & Sound Effects
music = pygame.mixer.music.load('sound\\bez_instrukcji.ogg')
sound_splash = pygame.mixer.Sound('sound\\splash.ogg')
sound_intro1 = pygame.mixer.Sound('sound\\intro1.ogg')
sound_intro2 = pygame.mixer.Sound('sound\\intro1.ogg')
sound_intro3 = pygame.mixer.Sound('sound\\intro1.ogg')
sound_mizer_v = pygame.mixer.Sound('sound\\mizer_v.ogg')
sound_mizer_f = pygame.mixer.Sound('sound\\mizer_f.ogg')
sound_magister = pygame.mixer.Sound('sound\\magister.ogg')

# Sprites
sprite_player = pygame.image.load('sprites\\player.png')
sprite_player = pygame.transform.scale(sprite_player, (TILESIZE, TILESIZE))
sprite_empty = pygame.image.load('sprites\\empty.png')
sprite_empty = pygame.transform.scale(sprite_empty, (TILESIZE, TILESIZE))
sprite_wall = pygame.image.load('sprites\\wall.png')
sprite_wall = pygame.transform.scale(sprite_wall, (TILESIZE, TILESIZE))
sprite_socket = pygame.image.load('sprites\\socket.png')
sprite_socket = pygame.transform.scale(sprite_socket, (TILESIZE, TILESIZE))
sprite_orb_unlit = pygame.image.load('sprites\\orb_unlit.png')
sprite_orb_unlit = pygame.transform.scale(sprite_orb_unlit, (TILESIZE, TILESIZE))
sprite_orb = pygame.image.load('sprites\\orb.png')
sprite_orb = pygame.transform.scale(sprite_orb, (TILESIZE, TILESIZE))

# Program Map
class Screen():
    """
    Used to navigate through various screens in-game.
    display - boolean, is the screen to be displayed
    """
    def __init__(self, display=False):
        self.display = display

screen_menu = Screen()
screen_game = Screen()
screen_tutorial = Screen()
screen_credits = Screen()
screen_campaign_menu = Screen()
screen_intro = Screen()
screen_next = Screen()

def logoDisplay(clock):
    display = True
    while display == True:
        start_time = pygame.time.get_ticks()
        while pygame.time.get_ticks() < start_time + 5600:
            ROOT.fill(WHITE)
            ROOT.blit(logo, (TEXT_INDENT / 4, 50))
            pygame.display.update()
        display = False

def chooseDisplay(screen):
    """
    Chooses the screen to be currently displayed.
    Affects menus and button mapping.
    """
    screen_menu.display = False
    screen_game.display = False
    screen_tutorial.display = False
    screen_credits.display = False
    screen_campaign_menu.display = False
    screen_intro.display = False
    screen_next.display = False
    screen.display = True

class Cursor():
    """
    Cursor used for navigating through menu selections.
    Used within startMenu() function.
    selection - int, default position of cursor
    """
    def __init__(self, selection):
        self.selection = selection

def buttonDisplay():
    pygame.draw.rect(ROOT, BLACK, (50, 200, 50, 200))
    if menu_cursor.selection == 0:
        ROOT.blit(image_rubens, (TEXT_INDENT - 50, 250))
    elif menu_cursor.selection == 1:
        ROOT.blit(image_rubens, (TEXT_INDENT - 50, 300))
    elif menu_cursor.selection == 2:
        ROOT.blit(image_rubens, (TEXT_INDENT - 50, 350))

def startMenu():
    """
    Function used to display the start menu.
    """
    chooseDisplay(screen_menu)
    ROOT.fill(BLACK)
    
    title = font_large.render("SokoAnn", 1, WHITE)
    author = font_small.render("©2020 Sankti Goździelewski", 1, WHITE)

    # Buttons TO BE MADE
    button_play = font_medium.render("New Game", 1, WHITE)
    button_tutorial = font_medium.render("Tutorial", 1, WHITE)
    button_credits = font_medium.render("Credits", 1, WHITE)
    # END

    ROOT.blit(title, (TEXT_INDENT, 50))
    ROOT.blit(author, (TEXT_INDENT, 100))

    # Buttons TO BE MADE
    ROOT.blit(button_play, (TEXT_INDENT, 250))
    ROOT.blit(button_tutorial, (TEXT_INDENT, 300))
    ROOT.blit(button_credits, (TEXT_INDENT, 350))
    # END

    buttonDisplay()

def tutorial():
    """
    Function used to display the tutorial menu.
    """
    chooseDisplay(screen_tutorial)
    ROOT.fill(BLACK)

    title = font_large.render("Tutorial", 1, WHITE)
    line0 = font_medium.render("<- Rubens", 1, WHITE)
    line1 = font_medium.render("An evil magician has", 1, WHITE)
    line2 = font_medium.render("kidnapped Rubens!", 1, WHITE)
    line3 = font_medium.render("You must free him", 1, WHITE)
    line4 = font_medium.render("before it's too late!", 1, WHITE)
    line5 = font_small.render("Press the arrow keys and push objects until you can access Rubens.", 1, WHITE)
    info = font_small.render("Press SPACE or ENTER to continue.", 1, WHITE)

    ROOT.blit(title, (TEXT_INDENT, 50))
    ROOT.blit(image_rubens_medium, (TEXT_INDENT, 100))
    ROOT.blit(line0, (TEXT_INDENT + 125, 125))
    ROOT.blit(line1, (TEXT_INDENT, 200))
    ROOT.blit(line2, (TEXT_INDENT, 225))
    ROOT.blit(line3, (TEXT_INDENT, 250))
    ROOT.blit(line4, (TEXT_INDENT, 275))
    ROOT.blit(line5, (TEXT_INDENT, 325))
    ROOT.blit(info, (TEXT_INDENT, 350))

def creditsMenu():
    """
    Function used to display the credits menu.
    """
    chooseDisplay(screen_credits)
    ROOT.fill(BLACK)

    title = font_large.render("Credits", 1, WHITE)
    line1 = font_medium.render("Game by Sankti Goździelewski", 1, WHITE)
    line2 = font_medium.render("", 1, WHITE)
    line3 = font_medium.render("sanktimarus@gmail.com", 1, WHITE)
    line4 = font_medium.render("github.com/Sankti", 1, WHITE)
    line5 = font_small.render("", 1, WHITE)
    info = font_small.render("Press SPACE or ENTER to continue.", 1, WHITE)

    ROOT.blit(title, (TEXT_INDENT, 50))
    ROOT.blit(line1, (TEXT_INDENT, 200))
    ROOT.blit(line2, (TEXT_INDENT, 225))
    ROOT.blit(line3, (TEXT_INDENT, 250))
    ROOT.blit(line4, (TEXT_INDENT, 275))
    ROOT.blit(line5, (TEXT_INDENT, 325))
    ROOT.blit(info, (TEXT_INDENT, 350))

def campaignMenu():
    """
    Function used to display the campaign choices menu.
    """
    chooseDisplay(screen_campaign_menu)
    ROOT.fill(BLACK)
    
    title = font_large.render("Wybierz Kampanię", 1, WHITE)
    author = font_small.render("", 1, WHITE)

    # Buttons TO BE MADE
    button_play = font_medium.render("Wyświetl intro", 1, WHITE)
    button_tutorial = font_medium.render("Główna Kampania", 1, WHITE)
    button_credits = font_medium.render("Dodatek: Büm i Mokrun", 1, WHITE)
    # END

    ROOT.blit(title, (TEXT_INDENT, 50))
    ROOT.blit(author, (TEXT_INDENT, 100))

    # Buttons TO BE MADE
    ROOT.blit(button_play, (TEXT_INDENT, 250))
    ROOT.blit(button_tutorial, (TEXT_INDENT, 300))
    ROOT.blit(button_credits, (TEXT_INDENT, 350))
    # END

    buttonDisplay()
    
def play_level(x, y, level):
    """
    Executes a given level.
    x - player's starting coordinate on axis x
    y - player's starting coordinate on axis y
    level - matrix, level definition
    """
    chooseDisplay(screen_game)
    ann.column = x
    ann.row = y
    ann.level = level
    drawMap(createMap(level))

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
            elif self.level[destination_x][destination_y] == 3 and self.level[pushed_x][pushed_y] == 1:
                self.level[destination_x][destination_y] = 1
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
            elif self.level[destination_x][destination_y] == 3 and self.level[pushed_x][pushed_y] == 1:
                self.level[destination_x][destination_y] = 1
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
            elif self.level[destination_x][destination_y] == 3 and self.level[pushed_x][pushed_y] == 1:
                self.level[destination_x][destination_y] = 1
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
            elif self.level[destination_x][destination_y] == 3 and self.level[pushed_x][pushed_y] == 1:
                self.level[destination_x][destination_y] = 1
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

    def get_level(self):
        return self.level

def drawMap(level_map):
    """
    Used to print graphical representation
    of a level map, using tiles.
    level_map - matrix, result of createMap(level)
    """
    ROOT.fill(BLACK)
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
        chooseDisplay(screen_next)
        prompt = pygame.font.SysFont("monospace", 48).render("Maciej pokonany!", 1, WHITE)
        ROOT.blit(prompt, (TEXT_INDENT, 50))
        pygame.draw.rect(ROOT, WHITE, (30, 195, 580, 110))
        pygame.draw.rect(ROOT, BLACK, (35, 200, 570, 100))
        line1 = pygame.font.SysFont("monospace", 32).render("Kolejny poziom: wciśnij ENTER", 1, WHITE)
        line2 = pygame.font.SysFont("monospace", 32).render("Powrót do menu: wciśnij ESC", 1, WHITE)
        ROOT.blit(line1, (40, 205))
        ROOT.blit(line2, (40, 245))

# Setting up cursor display position
menu_cursor = Cursor(0)

# Setting up the main "ann" variable for player character
ann = Player(0, 0, level1)

# COMMENCING LOOP, getting key input
sound_splash.play()
logoDisplay(fpsClock)
pygame.mixer.music.play(-1)
startMenu()



while True:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    KEYS = pygame.key.get_pressed()

    # Button mapping for various screens
    # ---------------------------------------------- START MENU
    if screen_menu.display == True:
        if KEYS[pygame.K_UP]:
            if menu_cursor.selection == 0:
                menu_cursor.selection = 0
            else:
                menu_cursor.selection -= 1
            buttonDisplay()

        if KEYS[pygame.K_DOWN]:
            if menu_cursor.selection == 2:
                menu_cursor.selection = 2
            else:
                menu_cursor.selection += 1
            buttonDisplay()

        if KEYS[pygame.K_SPACE] or KEYS[pygame.K_RETURN]:
            if menu_cursor.selection == 0:
                campaignMenu()
            elif menu_cursor.selection == 1:
                tutorial()
            elif menu_cursor.selection == 2:
                creditsMenu()

    # ---------------------------------------------- CAMPAIGN MENU
    elif screen_campaign_menu.display == True:
        if KEYS[pygame.K_UP]:
            if menu_cursor.selection == 0:
                menu_cursor.selection = 0
            else:
                menu_cursor.selection -= 1
            buttonDisplay()

        if KEYS[pygame.K_DOWN]:
            if menu_cursor.selection == 2:
                menu_cursor.selection = 2
            else:
                menu_cursor.selection += 1
            buttonDisplay()

        if KEYS[pygame.K_SPACE] or KEYS[pygame.K_RETURN]:
            if menu_cursor.selection == 0:
                tutorial()
            elif menu_cursor.selection == 1:
                play_level(7, 8, level1)
            elif menu_cursor.selection == 2:
                creditsMenu()
            
        if KEYS[pygame.K_ESCAPE]:
            startMenu()

    # ---------------------------------------------- TUTORIAL
    elif screen_tutorial.display == True:
        if KEYS[pygame.K_SPACE] or KEYS[pygame.K_RETURN]:
            startMenu()

    # ---------------------------------------------- CREDITS
    elif screen_credits.display == True:
        if KEYS[pygame.K_SPACE] or KEYS[pygame.K_RETURN]:
            startMenu()

    # ---------------------------------------------- GAME
    elif screen_game.display == True:
        if KEYS[pygame.K_UP]:
            ann.move("UP")
        if KEYS[pygame.K_LEFT]:
            ann.move("LEFT")
        if KEYS[pygame.K_RIGHT]:
            ann.move("RIGHT")
        if KEYS[pygame.K_DOWN]:
            ann.move("DOWN")
        if KEYS[pygame.K_ESCAPE]:
            startMenu()

# -------------------------------------------------- NEXT
    elif screen_next.display == True:
        if KEYS[pygame.K_SPACE] or KEYS[pygame.K_RETURN]:
            if ann.get_level() == level1:
                play_level(11, 7, level2)
            elif ann.get_level() == level2:
                play_level(9, 6, level3)
                # play_level(8, 5, level4)

        if KEYS[pygame.K_ESCAPE]:
            startMenu()
            
    pygame.display.update()
    fpsClock.tick(FPS)