''' Данная программа предназначена для
    отисовки небольшой анимации на языке Python
    с использованием Pygame
                            Козлова Ирина ИУ7-22Б
'''

import pygame as pg
import random as rd

'''Параметры окна'''
w = 800
h = 600

'''Цвета'''
BLUE = (145, 159, 245)
WHITE = (255, 255, 255)
W_WW = (244, 255, 255)
YELLOW = (239, 255, 0)
Y_B = (173, 216, 230)
SEA = (51, 0, 255)
BROWN = (117, 62, 20)
BLACK = (0, 0, 0)
GREY = (119, 119, 119)
RED = (245, 105, 180)
DARK_GREEN = (34, 139, 34)
SKY = (135, 206, 250)
GREEN = (60, 179, 113)
HOUSE = (204, 82, 0)
HOUSE1 = (200, 162, 200)
N_B = (160, 82, 45)

'''Спрайт "машина"'''
class Car(pg.sprite.Sprite):
    def __init__(self, x, filename):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(filename).convert_alpha()
        self.image = pg.transform.scale(self.image, (200, 140))
        self.rect = self.image.get_rect(center=(x, 500))
    def update(self):
        if self.rect.x < w:
            self.rect.x += 2
        else:
            self.rect.x = 0

'''Спрайт "человек"'''
class Men(pg.sprite.Sprite):
    def __init__(self, x, filename):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(filename).convert_alpha()
        self.image = pg.transform.scale(self.image, (60, 160))
        self.rect = self.image.get_rect(center=(x, 400))

'''Отрисовка неба'''
def draw_sky():
    pg.draw.rect(screen, SKY, (0, 0, 800, 600 - 130))

'''Отрисовка солнца с лучами(обстрактными)'''
def draw_sun():
    pg.draw.circle(screen, Y_B, (10, 10), 200)
    pg.draw.circle(screen, YELLOW, (10, 10), 90)
    
'''Отрисовка дороги.'''
def draw_road():
    pg.draw.rect(screen, GREY,(0, h - 130, w, h))
    pg.draw.line(screen, WHITE, (0, h - 65), (w, h - 65), 2)
    for i in range(5):
        pg.draw.rect(screen, WHITE,(600, h - 125 + (i * 30), 80, 20))

'''Отрислвка деревьев.'''        
def draw_tree():
    for i in range(5):
        pg.draw.rect(screen, BROWN,(130 * i + 10, 330, 20, 140))
        if (i % 2 == 0):
            pg.draw.circle(screen, DARK_GREEN, (130 * i + 20, 350), 50)
        else:
            pg.draw.circle(screen, GREEN, (130 * i + 20, 350), 50)

'''Отрисовка дома.'''           
def draw_house():
    pg.draw.rect(screen, HOUSE,(620, h - 300, 150, 170))
    pg.draw.polygon(screen, N_B, [(620, h - 300),
                                  (695, h - 350),
                                  (770, h - 300)])
    pg.draw.rect(screen, HOUSE1, (660, h - 250, 75, 120))

''' Отрисовка облака 1 формы.

    start_x - координата начала облака
'''
def draw_cloud(start_x, w):
    pg.draw.circle(screen, W_WW, (start_x + 90, 125), 48)
    pg.draw.circle(screen, W_WW, (start_x + 130, 120), 40)
    pg.draw.circle(screen, W_WW, (start_x + 50, 130), 30)
    pg.draw.circle(screen, W_WW, (start_x + 170, 130), 25)

'''Отрисовка облака 2 формы.

    start_x - координата начала облака
    w - ширина
'''
def draw_cloud1(start_x, w):
    pg.draw.ellipse(screen, W_WW, (start_x, 100, w, 60))
    pg.draw.circle(screen, W_WW, (start_x + 90, 125), 48)
    pg.draw.circle(screen, W_WW, (start_x + 130, 120), 40)
    pg.draw.circle(screen, W_WW, (start_x + 50, 130), 30)
    pg.draw.circle(screen, W_WW, (start_x + 170, 135), 20)

'''Инициализация окна программы'''  
pg.init()
screen = pg.display.set_mode((w, h))
pg.display.set_caption('CAR AND SUN')
clock = pg.time.Clock()
screen.fill(SKY)
pg.display.flip()

'''Главная функция программы'''
def main():
    cstart = rd.randint(0, 200)
    cstart1 = rd.randint(200, 600)
    cstart2 = rd.randint(500, 800)
    cwidth = 250
    cwidth1 = 200
    cwidth2 = 200
    running = True
    car1 = Car(100, 'car2.png')
    men = Men(650, 'men.png')
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                pg.quit()
                return
        '''Отрисовка всех деталей(статических)'''
        draw_sky()
        draw_road()
        draw_tree()
        draw_house()
        draw_sun()
        
        '''Отрисовка облаков(динамические объекты)'''
        draw_cloud(cstart, cwidth)
        draw_cloud1(cstart1, cwidth1)
        draw_cloud(cstart2, cwidth2)
        #pg.draw.circle(screen, BLUE, (513, 600 - 245), 2)

        '''Отрисовка машины'''
        screen.blit(car1.image, car1.rect)

        '''Движение облаков'''
        cstart -= 1
        cstart1 -= 2
        cstart2 -= 1
        if cstart <= -250:
            cstart = w + 200
        if cstart1 <= -250:
            cstart1 = w + 200
        if cstart2 <= -250:
            cstart2 = w + 200

        '''Движение машины'''
        if car1.rect.x < w - 100:
            car1.rect.x += 1
        else:
            '''Появление человека, когда машина доезжает до дома'''
            screen.blit(men.image, men.rect)
        pg.display.update()
        clock.tick(90)

'''Запуск окна'''
if __name__ == '__main__':
    main()
