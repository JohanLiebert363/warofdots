import pygame

pygame.init()
clock = pygame.time.Clock()
X = 1340
Y = 690


lost = False
won= False


white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
display_surface = pygame.display.set_mode((X, Y))
endScreen = pygame.image.load("mainScreen2.png").convert()
endScreen = pygame.transform.scale(endScreen, (X, Y))
endScreen2 = pygame.image.load("endScreen2.png").convert()
endScreen2 = pygame.transform.scale(endScreen2, (X, Y))

pygame.display.set_caption("War of Dots 2")

font = pygame.font.Font("freesansbold.ttf", 50)
font2 = pygame.font.Font("freesansbold.ttf", 19)
font3 = pygame.font.SysFont("freesansbold.ttf", 27) 
text = font.render("War of dots 2", True, blue)
textRect = text.get_rect(center=(X // 2, 240))

button = pygame.Rect(570, Y // 2, 200, 70)
buttonQuit = pygame.Rect(1260, 10, 70, 70)


background = pygame.image.load("mainScreen.png").convert()
background = pygame.transform.scale(background, (X, Y))
background2 = pygame.image.load("mainGame.png")
background2 = pygame.transform.scale(background2, (X, Y))
redDot = pygame.image.load("redDot.png").convert_alpha()
redDot = pygame.transform.scale(redDot, (30, 30))
blueDot = pygame.image.load("blueDot.png").convert_alpha()
blueDot = pygame.transform.scale(blueDot, (30, 30))
blueCapital = pygame.image.load("blueCapital.png").convert_alpha()
blueCapital = pygame.transform.scale(blueCapital, (40, 40))
redCapital = pygame.image.load("redCapital.png").convert_alpha()
redCapital = pygame.transform.scale(redCapital, (40, 40))
medRed = pygame.image.load("medRed.png").convert_alpha()
medRed = pygame.transform.scale(medRed,(150,90))
heal2 = pygame.image.load("heal.png").convert_alpha()
heal2 = pygame.transform.scale(heal2,(30,30))
swordI = pygame.image.load("sword.png").convert_alpha()
swordI = pygame.transform.scale(swordI,(30,30))
coinI = pygame.image.load("coin.png").convert_alpha()
coinI = pygame.transform.scale(coinI,(20,20))
buttonNuke = pygame.Rect(1100, 600, 200, 60)

NUCLEAR_COST = 100


keys= pygame.key.get_pressed()
coins =0
