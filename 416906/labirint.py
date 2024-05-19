# Разработай свою игру в этом фай
from pygame import *
from time import *
window = display.set_mode((900,800))
display.set_caption('Моя первая игра')
run = True
clock = clock()
class GameSprite(sprite.Sprite):
    def __init__(self, picture, w,h,x,y):
        super().__init__()
        self.image=transform.scale(image.load(picture),(w,h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))


class Player(sprite.Sprite):
    def __init__(self, picture,  w,h,x,y, x_speed=0, y_speed=0):
        super().__init__()
        self.image=transform.scale(image.load(picture),(w,h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.x_speed = 10
        self.y_speed = 10
    def update():
        self.rect.x = self.x_speed
        self.rect.y = self.y_speed
        

     


fon = GameSprite('fon.png',900,800,0,0)

walls = []
for i in range(2):
    walls.append(GameSprite('wall.png',20,180,100,250))
    walls.append(GameSprite('wall.png',20,180,100,430))

player = Player('player.png',10,90,5,215)

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    fon.reset()
    for i in walls:
        i.reset()
    display.update() 
