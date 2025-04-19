from pygame import *
from random import randint 


window = display.set_mode((700, 500))
display.set_caption("Rases")
background = transform.scale(image.load("road.jpg"), (700, 500))
game = True
clock = time.Clock()
FPS = 60

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_widht, player_height, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (player_widht, player_height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))


class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 635:
            self.rect.y += self.speed
        if keys[K_a] and self.rect.x > 5:
             self.rect.x -= self.speed 
        if keys[K_d] and self.rect.x  < 635:
             self.rect.x += self.speed 
    def update_r(self):
        keys = key.get_pressed() 
        if keys[K_DOWN] and self.rect.y < 400:
            self.rect.y += self.speed
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed 
        if keys[K_RIGHT] and self.rect.x  < 635:
            self.rect.x += self.speed 
car1 = Player('car1.png', 100, 400, 150, 100, 10)
car2 = Player('car2.png', 500, 400, 100, 100, 10)


lost = 0 
count = 0 
class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed 
        global lost
        if self.rect.y > 635:
            self.rect.x = randint(80, 635)
            self.rect.y = 0
            lost = lost + 1 
 
balls = sprite.Group()
for i in range(1, 6):
    ball = Enemy("ball.png", randint(80, 635), -40, 80, 50, randint(1, 5))
    balls.add(ball)


finish = False


while game:
    window.blit(background, (0, 0))
    car1.update_l()
    car2.update_r()
    car1.reset()
    car2.reset()
    balls.update()
    balls.draw(window)


    
    
    for e in event.get():
        if e.type == QUIT:
            game = False



    clock.tick(FPS)
    display.update()















