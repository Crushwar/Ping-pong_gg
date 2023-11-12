from pygame import *
from random import randint

class GameSprite(sprite.Sprite):
  # конструктор класса
    def __init__(self, player_image, player_x, player_y,player_speed,width,height):
        # Вызываем конструктор класса (Sprite):
        super.__init__(self)

        # каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (width,height))
        self.speed = player_speed

        # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
def reset(self):
    window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.x > 5:
            self.rect.y -= self.speed
        if keys[K_Down] and self.rect.x < win_width - 80:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.x > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.x < win_width - 80:
            self.rect.y += self.speed
  # метод "выстрел" (используем место игрока, чтобы создать там пулю)
Back = (255,255,255)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(Back)

font.init()
font = font.Font(None, 35)

r_img = 'racket.png'
speed = 20
hight = 150
width = 100



run = True
clock =time.Clock()
FPS = 60
racket1 = Player(r_img,30,200,speed,width,hight)
racket2 = Player(r_img,520,200,speed,width,hight)
ball = GameSprite('tennis_ball.png',200,200,speed,50,50)
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    if finish != True:

        window.fill(Back)



        racket1.update_left()
        racket2.update_right()
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        racket1.reset()
        racket2.reset()
        ball.reset()

        if ball.rect.y > win_height - 50 or ball.rect.y < 0:
            speed_y *=-1
        if sprite.collide_rect(racket1,ball) or sprite.collide_rect(racket2,ball):
            speed_x *=-1
        if ball.rect.x > 0:
            window.blit(losel(200,200))
            finish = True
        if ball.rect.x > win_width:
            window.blit(lose2 ,(200,200))
            finish - True


        display.update()
        clock.tick(FPS)