import pygame
from variables import *
from variables import white
from variables import font2

class Capital:
    def __init__(self, x, y, image, health, damage, team):
        self.image = image
        self.damage = damage
        self.rect = self.image.get_rect(center=(x, y))
        self.health = health
        self.team = team

        self.attack_cooldown = 0

    def draw(self, screen):
        screen.blit(self.image, self.rect)

        text = font2.render(str(self.health), True, white)
        screen.blit(text, (self.rect.left, self.rect.bottom))

        if self.attack_cooldown > 0:
            self.attack_cooldown -= 1

class Division:
    def __init__(self, x, y, image, health, damage, team):
        self.image = image
        self.rect = self.image.get_rect(center=(x, y))
        self.health = health
        self.damage = damage
        self.team = team

        self.pos = pygame.math.Vector2(self.rect.center)
        self.target = None


        self.attack_cooldown = 0

    def draw(self, screen):
        screen.blit(self.image, self.rect)

        text = font2.render(str(self.health), True, white)
        screen.blit(text, (self.rect.left, self.rect.bottom))

    def update_movement(self, brzina):
        if self.target:
            direction = self.target - self.pos
            distance = direction.length()

            if distance > 0:
                direction.normalize_ip()

                self.pos += direction * min(brzina, distance)

            else:
                self.target = None


        half_w = self.rect.width // 2
        half_h = self.rect.height // 2

        self.pos.x = max(half_w, min(X - half_w, self.pos.x))
        self.pos.y = max(half_h, min(Y - half_h, self.pos.y))

        self.rect.center = (
            int(self.pos.x),
            int(self.pos.y)
        )

        if self.attack_cooldown > 0:
            self.attack_cooldown -= 1
class medCenter:
    def __init__(self,x,y,image,team):
        self.image = image
        self.rect = self.image.get_rect(center=(x,y))
        self.team =team
        self.pos = pygame.math.Vector2(self.rect.center)
    def draw(self, screen):
        screen.blit(self.image, self.rect)
class medKit:
    def __init__(self,x,y,image,boost):
        self.image = image
        self.rect = self.image.get_rect(center=(x,y))
        self.boost = boost
    def draw(self,screen):
        screen.blit(self.image,self.rect)
class sword:
    def __init__(self,x,y,image,boost):
        self.image = image
        self.rect = self.image.get_rect(center=(x,y))
        self.boost = boost
    def draw(self,screen):
        screen.blit(self.image,self.rect)

