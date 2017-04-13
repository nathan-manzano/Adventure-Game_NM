import time
import sys, pygame
from random import randint

class Character:
    def _init_(self):
        self.name = ""
        self.health = 5
        self.max_health = 10
    def attack(self, enemy):
        damage = min(
            max(randint(0, self.health) - randint(0, enemy.health), 0), enemy. health)
        enemy.health = enemy.health - damage
        if damage == 0:
            print("%s evaded %s's attack!" % (enemy.name, self.name))
        else:
            print("%s hurts %s!" % (self.name, enemy.name))
        return enemy.health <= 0

class Enemy(Character):
    def _init_(self, player):
        Character._init_(self)
        self.name = 'a monster'
        self.health = randint(1, player.health)

class Player(Character):
    def _init_(self):
        Character._init_(self)
        self.health = 10
        self.max_health = 10


pygame.init()
size = width, height = 320, 240
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

ball = pygame.image.load("ball.bmp")
ballrect = ball.get_rect()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()


#Start game
p = Player()
p.name = input("What is your name? ")
print("%s, your adventure has begun." % (p.name))

#Go
print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print ("Welcome to your doom", '\u2122')
print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
time.sleep(3)


#First location

