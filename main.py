import pygame
from pygame.locals import *
from settings import *

# PYGAME Initialization
pygame.init()
ROOT = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SokoAnn")

# Fonts
font_large = pygame.font.SysFont("monospace", 48)
font_medium = pygame.font.SysFont("monospace", 32)
font_small = pygame.font.SysFont("monospace", 12)

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

def chooseDisplay(screen):
    """
    Chooses the screen to be currently displayed.
    Affects menus and button mapping.
    """
    screen_menu.display = False
    screen_game.display = False
    screen_tutorial.display = False
    screen_credits.display = False
    screen.display = True

image_rubens_full = pygame.image.load('Rubens.png')
image_rubens_medium = pygame.transform.scale(image_rubens_full, (100, 100))
image_rubens = pygame.transform.scale(image_rubens_full, (30, 30))
pygame.display.set_icon(image_rubens)

class Cursor():
    """
    Cursor used for navigating through menu selections.
    Used within startMenu() function.
    selection - int, default position of cursor
    """
    def __init__(self, selection):
        self.selection = selection

# Setting up cursor display positions
menu_cursor = Cursor(0)

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
    
    title = font_large.render("SecretProject", 1, WHITE)
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

class Tile():
    """
    Tiles which are used to draw level maps.
    passable: boolean, if the tile can be stepped on or not.
    """
    def __init__(self, passable=False):
        self.passable = passable

def game():
    chooseDisplay(screen_game)
    ROOT.fill(BLACK)


# COMMENCING LOOP, getting key input
startMenu()

while True:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    KEYS = pygame.key.get_pressed()

    # Button mapping for various screens
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
                pass
            elif menu_cursor.selection == 1:
                tutorial()
            elif menu_cursor.selection == 2:
                creditsMenu()

    elif screen_game.display == True:
        pass

    elif screen_tutorial.display == True:
        if KEYS[pygame.K_SPACE] or KEYS[pygame.K_RETURN]:
            startMenu()

    elif screen_credits.display == True:
        if KEYS[pygame.K_SPACE] or KEYS[pygame.K_RETURN]:
            startMenu()
        
            
    pygame.display.update()
    fpsClock.tick(FPS)

startMenu()