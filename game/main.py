import pygame
import time
from class1 import *
from func1 import *
from variables import *
from mainGame import *

pygame.init()


nasi = [
    Division(zz, 500, blueDot, 100, 1,"blue" )
    for zz in range(360, 900, 60)
]

njihovi = [
    Division(ii, 100, redDot, 105, 1, "red")
    for ii in range(360, 900, 60)
]
medkit = []
for j in range(5):
    healKit=medKit(random.randint(110,490),random.randint(300,900),heal2,10)
    medkit.append(healKit)
swordL = []
for j in range(5):
    swordB=medKit(random.randint(110,490),random.randint(300,900),swordI,1)
    swordL.append(swordB)
sveDivs = nasi + njihovi
coinL = []
for j in range(12):
    coinB=coin(random.randint(300,800),random.randint(150,300),coinI,10)
    coinL.append(coinB)
    print(coinL)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button.collidepoint(event.pos):
                running = False
            if buttonQuit.collidepoint(event.pos):
                pygame.quit()
                quit()

    display_surface.blit(background, (0, 0))
    display_surface.blit(text, textRect)
  
    if button.collidepoint(pygame.mouse.get_pos()):
        color = "darkgreen"
    else:
        color = "green"
        
    if buttonQuit.collidepoint(pygame.mouse.get_pos()):
        color2 = "white"
    else:
        color2 = "gray"
        
    pygame.draw.rect(display_surface, color, button)
    pygame.draw.rect(display_surface, color2, buttonQuit)
    
    text2 = font.render("PLAY", True, "white")
    text3 = font3.render("QUIT", True, "black")
    text_rect2 = text3.get_rect(center=buttonQuit.center)
    text_rect = text2.get_rect(center=button.center)
    
    display_surface.blit(text2, text_rect)
    display_surface.blit(text3, text_rect2)
    pygame.display.update()
    clock.tick(60)


mainGame(sveDivs,medkit,njihovi,swordL,nasi,coinL)

