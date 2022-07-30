import pygame

pygame.init()
win = pygame.display.set_mode((750, 500))

tombstonespr = pygame.image.load("sprites/tombstone/tombstone0.png")
lossspr = [pygame.image.load("sprites/loss/loss0.png"), pygame.image.load("sprites/loss/loss1.png")]
retrybtn = [pygame.image.load("sprites/button/retry/retry0.png"), pygame.image.load("sprites/button/retry/retry1.png")]
menubtn = [pygame.image.load("sprites/button/menu/menu0.png"), pygame.image.load("sprites/button/menu/menu1.png")]

scene = "loss"

def tombstone():
    x = 247
    y = 80
    win.blit(tombstonespr, (x, y))

def lossgame(wait):
    x = 249
    y = 10
    win.blit(lossspr[wait // 20], (x, y))

def retry(position, press):
    global scene
    x = 135
    y = 370
    if (position[0] > x and position[0] < x + 168 and position[1] > y and position[1] < y + 56):
        win.blit(retrybtn[1], (x, y))
        if (press == True):
            scene = "play"
    else:
        win.blit(retrybtn[0], (x, y))

def menu(position, press):
    global scene
    x = 435
    y = 370
    if (position[0] > x and position[0] < x + 168 and position[1] > y and position[1] < y + 56):
        win.blit(menubtn[1], (x, y))
        if (press == True):
            scene = "menu"
    else:
        win.blit(menubtn[0], (x, y))

def updatescene():
    global scene
    scene = "loss"