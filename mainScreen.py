import pygame
import time

pygame.init()

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
X = 1340
Y = 690

clock=pygame.time.Clock()

display_surface = pygame.display.set_mode((X, Y),pygame.FULLSCREEN) #,pygame.FULLSCREEN
pygame.display.set_caption("War of Dots 2")

#X, Y = display_surface.get_size()
display_surface = pygame.display.set_mode((X, Y))
font = pygame.font.Font("freesansbold.ttf", 50)
font2 = pygame.font.Font("freesansbold.ttf", 19)
text = font.render("War of dots 2", True, blue)
textRect = text.get_rect(center=(X // 2, 240))

button = pygame.Rect(570, Y // 2, 200, 70)

background = pygame.image.load("mainScreen.png").convert()
background = pygame.transform.scale(background, (X, Y))
background2 = pygame.image.load("mainGame.png")
background2 = pygame.transform.scale(background2, (X, Y))
redDot = pygame.image.load("redDot.png").convert_alpha()
redDot = pygame.transform.scale(redDot, (30, 30))
blueDot = pygame.image.load("blueDot.png").convert_alpha()
blueDot = pygame.transform.scale(blueDot, (30, 30))

div1 = 100 # health for division 1
class Division:
    def __init__(self, x, y, image, health):
        self.rect = image.get_rect(center=(x, y))
        self.image = image

        self.health = health

    def draw(self, screen):

        screen.blit(self.image, self.rect)


        text = font2.render(str(self.health), True, white)



        screen.blit(text, (self.rect.left , self.rect.bottom))
nasi=[Division(zz,500,blueDot,100) for zz in range(360,900,60)]
njihovi = [Division(ii, 100, redDot, 100) for ii in range(360,900,60)]
sveDivs = nasi+njihovi
division1 = Division(360, 500, blueDot, 100)
division2 = Division(420, 500, blueDot, 100)
division3 = Division(480, 500, blueDot, 100)
division4= Division(540, 500, blueDot, 100)
division5 = Division(600, 500, blueDot, 100)
division6 = Division(660, 500, blueDot, 100)
division7 = Division(720, 500, blueDot, 100)
division8 = Division(780, 500, blueDot, 100)
division9= Division(840, 500, blueDot, 100)
division10 = Division(900, 500, blueDot, 100)
division1R = Division(360, 100, redDot, 100)
division2R = Division(420, 100, redDot, 100)
division3R = Division(480, 100, redDot, 100)
division4R= Division(540, 100, redDot, 100)
division5R = Division(600, 100, redDot, 100)
division6R = Division(660, 100, redDot, 100)
division7R = Division(720, 100, redDot, 100)
division8R = Division(780, 100, redDot, 100)
division9R= Division(840, 100, redDot, 100)
division10R = Division(900, 100, redDot, 100)
def mainGame(sveDivs):
    running = True
    timer = time.time()
    display_surface.fill(white)
    clicked=None
    tacke = []
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        for divizija in sveDivs:
            if event.type == pygame.K_RIGHT:
                pass # todo: make the div go tho the next click
        end = time.time()
        seconds = end - timer
        seconds = int(seconds)
        minut = seconds //60
        seconds = seconds % 60
        clock.tick(60)


        textTimer = font.render(f"{minut:02d}:{seconds:02d}", True, white)
        
        display_surface.blit(background2, (0, 0))

        display_surface.blit(textTimer,(0,100))
        division1.draw(display_surface)
        division2.draw(display_surface)
        division3.draw(display_surface)
        division4.draw(display_surface)
        division5.draw(display_surface)
        division6.draw(display_surface)
        division7.draw(display_surface)
        division8.draw(display_surface)
        division9.draw(display_surface)
        division10.draw(display_surface)
        division1R.draw(display_surface)
        division2R.draw(display_surface)
        division3R.draw(display_surface)
        division4R.draw(display_surface)
        division5R.draw(display_surface)
        division6R.draw(display_surface)
        division7R.draw(display_surface)
        division8R.draw(display_surface)
        division9R.draw(display_surface)
        division10R.draw(display_surface)    
        pygame.display.update()
    clock.tick(60)
    pygame.quit()


running = True

while running:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if button.collidepoint(event.pos):
                print("play dugme kliknuto")
                running = False
            

    if keys[pygame.K_ESCAPE]:
        pygame.quit()
        quit()

    display_surface.blit(background, (0, 0))

    display_surface.blit(text, textRect)

  
    if button.collidepoint(pygame.mouse.get_pos()):
        color = "darkgreen"
    else:
        color = "green"

    pygame.draw.rect(display_surface, color, button)

    text2 = font.render("PLAY", True, "white")
    text_rect = text2.get_rect(center=button.center)
    display_surface.blit(text2, text_rect)

    pygame.display.update()
    clock.tick(60)
mainGame()
