import pygame
from variables import *



def handle_collisions(sveDivs):
    for i in range(len(sveDivs)):
        div1 = sveDivs[i]

        for j in range(i + 1, len(sveDivs)):
            div2 = sveDivs[j]


            if div1.team == div2.team:
                continue

            dx = div2.pos.x - div1.pos.x
            dy = div2.pos.y - div1.pos.y

            distance = (dx * dx + dy * dy) ** 0.5

            min_distance = 30

            if distance < min_distance:

                if distance == 0:
                    direction = pygame.math.Vector2(1, 0)
                else:
                    direction = pygame.math.Vector2(dx, dy)
                    direction.normalize_ip()



                overlap = min_distance - distance

                div1.pos -= direction * (overlap / 2)
                div2.pos += direction * (overlap / 2)

                div1.rect.center = (
                    int(div1.pos.x),
                    int(div1.pos.y)
                )

                div2.rect.center = (
                    int(div2.pos.x),
                    int(div2.pos.y)
                )



                if div1.attack_cooldown <= 0:
                    div2.health -= div1.damage
                    div1.attack_cooldown = 60

                if div2.attack_cooldown <= 0:
                    div1.health -= div2.damage
                    div2.attack_cooldown = 60


    sveDivs[:] = [
        div for div in sveDivs
        if div.health > 0
    ]
def handle_capital_combat(sveDivs, capitals):

    for capital in capitals:

        for div in sveDivs:

        
            if div.team == capital.team:
                    continue


            if div.rect.colliderect(capital.rect):


                direction = pygame.math.Vector2(
                    div.rect.centerx - capital.rect.centerx,
                    div.rect.centery - capital.rect.centery
                )


                if direction.length() == 0:
                    direction = pygame.math.Vector2(1, 0)
                else:
                    direction.normalize_ip()


                div.pos += direction * 2

                div.rect.center = (
                    int(div.pos.x),
                    int(div.pos.y)
                )

                if div.attack_cooldown <= 0:
                    capital.health -= div.damage
                    div.attack_cooldown = 30


                if capital.attack_cooldown <= 0:
                    div.health -= capital.damage
                    capital.attack_cooldown = 30
                if capital.team == "blue":
                    if capital.health <= 0:
                        

                        lost = True
                        won=False
                        gameOver(lost,won)
                        print(lost)
                if capital.team == "red":
                    if capital.health <= 0:
                        
                        
                        

                        lost=False
                        won=True
                        gameOver(lost,won)
                        print(won)
    sveDivs[:] = [
        div for div in sveDivs
        if div.health > 0
    ]
def gameOver(lost,won):

    radi=True
    while radi:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

        if lost == True and won == False:
            
            display_surface.blit(endScreen, (0, 0))
            textEnd2= font.render("You lose",True,white)
            textEnd2Rect = text.get_rect(center=(X // 2, 240))
            display_surface.blit(textEnd2, textEnd2Rect)
              
        elif won == True and lost == False:

            display_surface.blit(endScreen2, (0, 0))
            textEnd1= font.render("You win",True,white)
            textEndRect = text.get_rect(center=(X // 2, 240))
            display_surface.blit(textEnd1, textEndRect)
              
        pygame.display.update()
        clock.tick(60)
    pygame.quit()
def heal(sveDivs, medNjihovi):
    for div in sveDivs:
        if div.rect.colliderect(medNjihovi.rect):
            if div.health < 100:
                div.health +=1
                
def healSpawn(sveDivs, medkit):
    for div in sveDivs:
        for med in medkit:
            if div.rect.colliderect(med.rect):
                div.health +=10
                medkit.remove(med)
def boost(sveDivs,swordL):
        for div in sveDivs:
            for s in swordL:
                if div.rect.colliderect(s.rect):
                    div.damage +=1
                    swordL.remove(s)
def red_ai(sveDivs, njihovi, medNjihovi, capitalBlue,nasi):
    red_alive = [div for div in sveDivs if div.team == "red"]

    original_red = len(njihovi)

    if original_red == 0:
        return

    red_dead_percent = (original_red - len(red_alive)) / original_red


    if red_dead_percent >= 0.70:

        for red in red_alive:
            red.target = pygame.math.Vector2(capitalBlue.rect.center)
    
        return

    blue_alive = [div for div in sveDivs if div.team == "blue"]
    original_blue = len(nasi)
    if original_blue == 0:
        return
    blue_dead_percent = (original_blue - len(blue_alive)) / original_blue
    if blue_dead_percent >= 0.60:

        for red in red_alive:
            red.target = pygame.math.Vector2(capitalBlue.rect.center)
    
        return
    
    for red in red_alive:

        if red.health < 20:
            red.target = pygame.math.Vector2(medNjihovi.rect.center)