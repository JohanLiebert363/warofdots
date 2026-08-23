import pygame 
from variables import *
from func1 import *
from class1 import *
import time
import random

CapitalRed = Capital(600, 30,redCapital,180,2, "red")
CapitalBlue = Capital(600, 600,blueCapital,180,2,"blue")
medNjihovi = medCenter(100,Y//2,medRed,"red")
timer = time.time()
def mainGame(sveDivs,medkit,njihovi,swordL,nasi):
    running = True
    brzina = 0.5


    clicked_div = None
    is_dragging = False

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if keys[pygame.K_ESCAPE]:
                running = False
                
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:

                    for divizija in sveDivs:
                        if divizija.team == "red":
                            for div in nasi:
                                redTarget = div
                        if divizija.rect.collidepoint(event.pos):
                            clicked_div = divizija
                            is_dragging = True
                            break

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:

                    if is_dragging and clicked_div:
                        clicked_div.target = pygame.math.Vector2(event.pos)
                    is_dragging = False
                    clicked_div = None
        
        for div in sveDivs:
            div.update_movement(brzina)

        handle_collisions(sveDivs)

        handle_capital_combat(
            sveDivs,
            [CapitalRed, CapitalBlue]
        )
        heal(
            sveDivs,
            medNjihovi
        )
        healSpawn(
            sveDivs,
            medkit
        )
        boost(
            sveDivs,
            swordL
        )
        red_ai(
            sveDivs,
            njihovi,
            medNjihovi,
            CapitalBlue,
            nasi
        )

        for div in sveDivs:
            div.update_movement(brzina)
        end = time.time()
        seconds = int(end - timer)
        minut = seconds // 60
        seconds = seconds % 60
        for i in njihovi:





            if seconds >= 15:
                for red, blue in zip(njihovi, nasi):
                    red.target = blue.rect.center
        textTimer = font.render(f"{minut:02d}:{seconds:02d}", True, white)
        

        display_surface.blit(background2, (0, 0))
        display_surface.blit(textTimer, (0, 10))
        medNjihovi.draw(display_surface)
        for div in sveDivs:
            div.draw(display_surface)  
        CapitalRed.draw(display_surface)
        CapitalBlue.draw(display_surface)
        for kit in medkit:
                kit.draw(display_surface)  
        for s in swordL:
            s.draw(display_surface)
        if is_dragging and clicked_div:
            trenutni_mis = pygame.mouse.get_pos()
            pygame.draw.line(display_surface, white, clicked_div.rect.center, trenutni_mis, 3)

        '''if lost == True or won == True:
            gameOver()'''
            
        pygame.display.update()
        clock.tick(60)
        
    pygame.quit()
