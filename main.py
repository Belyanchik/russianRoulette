import pygame

import menu
import play
import wingame
import lossgame

pygame.init()
win = pygame.display.set_mode((750, 500))

pygame.display.set_caption("Russian Roulette")

logo = pygame.image.load("sprites/logo/minilogo.png")
pygame.display.set_icon(logo)

clock = pygame.time.Clock()
FPS = 30
run = True
scene = "menu"
wait = 0

while(run == True):
    clock.tick(FPS)
    press = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONUP:
            press = True

    win.fill((246, 223, 152))
    position = pygame.mouse.get_pos()

    if(scene == "menu"):
        play.updatescene()
        wingame.updatescene()
        lossgame.updatescene()

        menu.playbtn(position, press)
        menu.githubbtn(position, press)
        menu.logo()
        menu.bootle()
        menu.revolverlogo()
        menu.version()
        scene = menu.scene

    if(scene == "play"):
        menu.updatescene()
        wingame.updatescene()
        lossgame.updatescene()

        wait = 0
        play.startshuffle()
        while(scene == "play"):
            step = play.step
            clock.tick(FPS)
            press = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    scene = "quit"
                    play.quitgame()
                if event.type == pygame.MOUSEBUTTONUP:
                    press = True

            win.fill((246, 223, 152))
            position = pygame.mouse.get_pos()

            play.bar()
            play.banana1()
            play.banana2()
            play.revolver()
            play.printchance()

            if(step == True):
                play.shot(position, press)
                play.spin(position, press)
            else:
                wait = wait + 1
                if(wait >= 45):
                    play.botrandom()
                    wait = 0

            pygame.display.update()
            scene = play.scene
        if(run == True):
            run = play.kill()

    if(scene == "win"):
        play.updatescene()

        wingame.tombstone()
        wingame.wingame(wait)
        wingame.retry(position, press)
        wingame.menu(position, press)
        if(wait >= 39):
            wait = 0
        else:
            wait = wait + 1
        scene = wingame.scene

    if(scene == "loss"):
        play.updatescene()

        lossgame.tombstone()
        lossgame.lossgame(wait)
        lossgame.retry(position, press)
        lossgame.menu(position, press)
        if(wait >= 39):
            wait = 0
        else:
            wait = wait + 1
        scene = lossgame.scene

    pygame.display.update()