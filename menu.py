import pygame
import webbrowser

pygame.init()
win = pygame.display.set_mode((750, 500))

play = [pygame.image.load("sprites/button/play/play0.png"), pygame.image.load("sprites/button/play/play1.png")]
revolverlogospr = pygame.image.load("sprites/revolver/revolverandstand.png")
logospr = pygame.image.load("sprites/logo/logo.png")
bootlespr = pygame.image.load("sprites/bootle/bootle.png")
github = [pygame.image.load("sprites/button/github/github0.png"), pygame.image.load("sprites/button/github/github1.png")]

text = pygame.font.SysFont("Impact", 20)

scene = "menu"

def playbtn(position, press):
    global scene
    x = 266
    y = 200
    if(position[0] > x and position[0] < x + 168 and position[1] > y and position[1] < y + 56):
        win.blit(play[1], (x, y))
        if(press == True):
            scene = "play"
    else:
        win.blit(play[0], (x, y))

def githubbtn(position, press):
    x = 266
    y = 320
    if(position[0] > x and position[0] < x + 168 and position[1] > y and position[1] < y + 56):
        win.blit(github[1], (x, y))
        if(press == True):
            webbrowser.open_new("https://github.com/Belyanchik")
    else:
        win.blit(github[0], (x, y))

def logo():
    x = 182
    y = 50
    win.blit(logospr, (x, y))

def revolverlogo():
    x = 570
    y = 90
    win.blit(revolverlogospr, (x, y))

def bootle():
    x = 70
    y = 340
    win.blit(bootlespr, (x, y))

def version():
    x = 710
    y = 470
    win.blit(text.render("v1.0", 1, (107, 50, 0), (246, 223, 152)), (x, y))

def updatescene():
    global scene
    scene = "menu"