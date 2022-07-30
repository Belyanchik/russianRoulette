import pygame
import random

pygame.init()
win = pygame.display.set_mode((750, 500))

barspr = pygame.image.load("sprites/bar/bar0.png")
banana1spr = [pygame.image.load("sprites/banana/banana1_0.png"), pygame.image.load("sprites/banana/banana1_1.png")]
banana2spr = [pygame.image.load("sprites/banana/banana2_0.png"), pygame.image.load("sprites/banana/banana2_1.png")]
revolverspr = pygame.image.load("sprites/revolver/revolver.png")
shotbtn = [pygame.image.load("sprites/button/shot/shot0.png"), pygame.image.load("sprites/button/shot/shot1.png")]
spinbtn = [pygame.image.load("sprites/button/spin/spin0.png"), pygame.image.load("sprites/button/spin/spin1.png")]
killspr = [pygame.image.load("sprites/kill/kill0.png"), pygame.image.load("sprites/kill/kill1.png"), pygame.image.load("sprites/kill/kill2.png"), pygame.image.load("sprites/kill/kill3.png")]

text = pygame.font.SysFont("Impact", 20)

shotsnd = pygame.mixer.Sound("sounds/shot.mp3")
misssnd = pygame.mixer.Sound("sounds/miss.mp3")
rollsnd = pygame.mixer.Sound("sounds/roll.mp3")

scene = "play"
step = bool(random.getrandbits(1))
roll = [1, 0, 0, 0, 0, 0]
chance = 16

ms = 0

def bar():
    x = 119
    y = 240
    win.blit(barspr, (x, y))

def banana1():
    x = 612
    y = 10
    win.blit(banana1spr[0], (x, y))

def banana2():
    x = 10
    y = 10
    win.blit(banana2spr[0], (x, y))

def revolver():
    x = 311
    y = 10
    if(step == False):
        win.blit(revolverspr, (x, y))
    else:
        newrevolver = pygame.transform.flip(revolverspr, True, False)
        win.blit(newrevolver, (x, y))

def shot(position, press):
    x = 135
    y = 160
    if(step == True):
        if (position[0] > x and position[0] < x + 168 and position[1] > y and position[1] < y + 56):
            win.blit(shotbtn[1], (x, y))
            if (press == True):
                plshot()
        else:
            win.blit(shotbtn[0], (x, y))

def spin(position, press):
    x = 435
    y = 160
    if(step == True):
        if (position[0] > x and position[0] < x + 168 and position[1] > y and position[1] < y + 56):
            win.blit(spinbtn[1], (x, y))
            if (press == True):
                plspin()
        else:
            win.blit(spinbtn[0], (x, y))



def botrandom():
    global chance, step, scene
    if(random.randint(1, 2) == 1):
        if(roll[0] == 1):
            shotsnd.play()
            scene = "win"
        else:
            chance = chance + 16
            roll.append(roll[0])
            roll.pop(0)
            step = True
            misssnd.play()
    else:
        random.shuffle(roll)
        chance = 16
        rollsnd.play()

def plshot():
    global chance, step, scene
    if(roll[0] == 1):
        shotsnd.play()
        scene = "loss"
    else:
        chance = chance + 16
        roll.append(roll[0])
        roll.pop(0)
        step = False
        misssnd.play()

def plspin():
    global chance
    random.shuffle(roll)
    chance = 16
    rollsnd.play()

def updatescene():
    global scene
    scene = "play"

def quitgame():
    global scene
    scene = "quit"

def printchance():
    global chance
    x = 300
    y = 10
    if(chance == 48):
        chance = 50
    elif(chance == 98):
        chance = 100
    win.blit(text.render(f"Shot chance: {chance}%", 1, (107, 50, 0), (246, 223, 152)), (x,y))

def startshuffle():
    global roll, chance
    random.shuffle(roll)
    chance = 16

def kill():
    run = True
    wait = 0
    x = 64
    y = 70
    if(step == True):
        win.blit(banana1spr[1], (612, 10))
    else:
        win.blit(banana2spr[1], (10, 10))
    while(wait <= 59 and run == True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        pygame.time.Clock().tick(30)
        win.blit(killspr[wait // 15], (x, y))
        wait = wait + 1
        pygame.display.update()
        if(run == False):
            break
    return run