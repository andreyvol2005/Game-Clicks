import pygame
from random import *
from math import *

pygame.init()
screen = pygame.display.set_mode((1200, 800))
pygame.display.set_caption('Клики')
pygame.display.set_icon(pygame.image.load("game_images/ava.png"))

cr = pygame.image.load("game_images/cr.png").convert_alpha()
br = pygame.image.load("game_images/del.png").convert_alpha()
button = [pygame.image.load("game_images/b1.png").convert_alpha(),
          pygame.image.load("game_images/b4.png").convert_alpha()]
b_w = [pygame.image.load("game_images/w.png").convert_alpha(),
       pygame.image.load("game_images/b.png").convert_alpha()]
arr = [randint(0, 1), randint(0, 1), randint(0, 1),
       randint(0, 1), randint(0, 1), randint(0, 1),
       randint(0, 1), randint(0, 1), randint(0, 1)]
img = [b_w[arr[0]], b_w[arr[1]], b_w[arr[2]],
       b_w[arr[3]], b_w[arr[4]], b_w[arr[5]],
       b_w[arr[6]], b_w[arr[7]], b_w[arr[8]]]
x = 60
y = 290
x_ = 400
y_ = 25
x__ = 850
y__ = 515
br1 = button[0].get_rect(topleft=(x, y))
br2 = button[0].get_rect(topleft=(x + 150, y))
br3 = button[0].get_rect(topleft=(x + 300, y))
br4 = button[0].get_rect(topleft=(x, y + 150))
br5 = button[0].get_rect(topleft=(x + 150, y + 150))
br6 = button[0].get_rect(topleft=(x + 300, y + 150))
br7 = button[0].get_rect(topleft=(x, y + 300))
br8 = button[0].get_rect(topleft=(x + 150, y + 300))
br9 = button[0].get_rect(topleft=(x + 300, y + 300))
b1, b2, b3, b4, b5, b6, b7, b8, b9 = 0, 0, 0, 0, 0, 0, 0, 0, 0
mu1, mu2, mu3, mu4, mu5, mu6, mu7, mu8, mu9 = True, True, True, True, True, True, True, True, True
mu10 = False
text = pygame.font.Font('game_fonts/font.ttf', 40)
time = 1200
angle = 0
score = 0
gr = [0, 45, 90, 135, 180, 225, 270, 315][randint(0, 7)]
but = pygame.mixer.Sound('game_songs/кнопка.mp3')
crut = pygame.mixer.Sound('game_songs/круток.mp3')
lev = pygame.mixer.Sound('game_songs/уровень.mp3')
levb = pygame.mixer.Sound('game_songs/ур.mp3')
ungr = 0
degr = 0
flag = 0

running = True
while running:
    screen.fill((220, 220, 220))
    screen.blit(text.render(f'счёт: {score}', True, 'black'), (10, 10))

    if (b1 == arr[0] and b2 == arr[1] and b3 == arr[2] and b4 == arr[3] and b5 == arr[4] and b6 == arr[5]\
        and b7 == arr[6] and b8 == arr[7] and b9 == arr[8] and (degr == gr or (degr == 360 and gr == 0))):
        lev.play()
        arr = [randint(0, 1), randint(0, 1), randint(0, 1),
               randint(0, 1), randint(0, 1), randint(0, 1),
               randint(0, 1), randint(0, 1), randint(0, 1)]
        img = [b_w[arr[0]], b_w[arr[1]], b_w[arr[2]],
               b_w[arr[3]], b_w[arr[4]], b_w[arr[5]],
               b_w[arr[6]], b_w[arr[7]], b_w[arr[8]]]
        b1, b2, b3, b4, b5, b6, b7, b8, b9 = 0, 0, 0, 0, 0, 0, 0, 0, 0
        gr = [0, 45, 90, 135, 180, 225, 270, 315][randint(0, 7)]
        time = 1200
        angle = 0
        score += 1
    elif time == 0:
        levb.play()
        arr = [randint(0, 1), randint(0, 1), randint(0, 1),
               randint(0, 1), randint(0, 1), randint(0, 1),
               randint(0, 1), randint(0, 1), randint(0, 1)]
        img = [b_w[arr[0]], b_w[arr[1]], b_w[arr[2]],
               b_w[arr[3]], b_w[arr[4]], b_w[arr[5]],
               b_w[arr[6]], b_w[arr[7]], b_w[arr[8]]]
        b1, b2, b3, b4, b5, b6, b7, b8, b9 = 0, 0, 0, 0, 0, 0, 0, 0, 0
        gr = [0, 45, 90, 135, 180, 225, 270, 315][randint(0, 7)]
        time = 1200
        angle = 0

    bar = pygame.Surface((time, 30))

    screen.blit(img[0], (x_, y_))
    screen.blit(img[1], (x_ + 50, y_))
    screen.blit(img[2], (x_ + 100, y_))
    screen.blit(img[3], (x_, y_ + 50))
    screen.blit(img[4], (x_ + 50, y_ + 50))
    screen.blit(img[5], (x_ + 100, y_ + 50))
    screen.blit(img[6], (x_, y_ + 100))
    screen.blit(img[7], (x_ + 50, y_ + 100))
    screen.blit(img[8], (x_ + 100, y_ + 100))

    screen.blit(pygame.font.Font('game_fonts/font.ttf', 180).render(f'{gr}', True, 'black'), (600, 25))

    screen.blit(bar, (0, 200))

    if pygame.transform.scale(cr, (450, 450)).get_rect(topleft=(x__ - 225,
        y__ - 225)).collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
        angle = round(degrees(atan2(-(pygame.mouse.get_pos()[1] - y__), pygame.mouse.get_pos()[0] - x__)) - 90, 2)
        cr1 = 1
        mu10 = True
    elif mu10 and pygame.mouse.get_pressed()[0]:
        angle = round(degrees(atan2(-(pygame.mouse.get_pos()[1] - y__), pygame.mouse.get_pos()[0] - x__)) - 90, 2)
        cr1 = 1
    else:
        mu10 = False
        cr1 = 0

    if angle < 0:
        degr = -angle
    else:
        degr = 360 - angle

    if 336.5 < degr or degr < 22.5:
        angle = 0
    elif 22.5 <= degr <= 67.5:
        angle = -45
    elif 67.5 <= degr <= 112.5:
        angle = -90
    elif 112.5 <= degr <= 157.5:
        angle = -135
    elif 157.5 <= degr <= 202.5:
        angle = -180
    elif 202.5 <= degr <= 247.5:
        angle = -225
    elif 247.5 <= degr <= 292.5:
        angle = -270
    elif 292.5 <= degr <= 337.5:
        angle = 45

    circl = pygame.transform.rotate(pygame.transform.scale(cr, (450, 450)), angle)
    if ungr != angle:
        ungr = angle
        crut.play()
    screen.blit(pygame.transform.scale(br, (450, 450)), (x__ - 225, y__ - 225))
    screen.blit(circl, circl.get_rect(center=(x__, y__)))

    time -= 0.5

    if br1.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
        if mu1:
            if b1 == 0:
                b1 = 1
                but.play()
            elif b1 == 1:
                b1 = 0
        mu1 = False
    else:
        mu1 = True

    if br2.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
        if mu2:
            if b2 == 0:
                b2 = 1
                but.play()
            elif b2 == 1:
                b2 = 0
        mu2 = False
    else:
        mu2 = True

    if br3.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
        if mu3:
            if b3 == 0:
                b3 = 1
                but.play()
            elif b3 == 1:
                b3 = 0
        mu3 = False
    else:
        mu3 = True

    if br4.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
        if mu4:
            if b4 == 0:
                b4 = 1
                but.play()
            elif b4 == 1:
                b4 = 0
        mu4 = False
    else:
        mu4 = True

    if br5.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
        if mu5:
            if b5 == 0:
                b5 = 1
                but.play()
            elif b5 == 1:
                b5 = 0
        mu5 = False
    else:
        mu5 = True

    if br6.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
        if mu6:
            if b6 == 0:
                b6 = 1
                but.play()
            elif b6 == 1:
                b6 = 0
        mu6 = False
    else:
        mu6 = True

    if br7.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
        if mu7:
            if b7 == 0:
                b7 = 1
                but.play()
            elif b7 == 1:
                b7 = 0
        mu7 = False
    else:
        mu7 = True

    if br8.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
        if mu8:
            if b8 == 0:
                b8 = 1
                but.play()
            elif b8 == 1:
                b8 = 0
        mu8 = False
    else:
        mu8 = True

    if br9.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
        if mu9:
            if b9 == 0:
                b9 = 1
                but.play()
            elif b9 == 1:
                b9 = 0
        mu9 = False
    else:
        mu9 = True

    if b1 == 0:
        screen.blit(button[0], (x, y))
    elif b1 == 1:
        screen.blit(button[1], (x, y))

    if b2 == 0:
        screen.blit(button[0], (x + 150, y))
    elif b2 == 1:
        screen.blit(button[1], (x + 150, y))

    if b3 == 0:
        screen.blit(button[0], (x + 300, y))
    elif b3 == 1:
        screen.blit(button[1], (x + 300, y))

    if b4 == 0:
        screen.blit(button[0], (x, y + 150))
    elif b4 == 1:
        screen.blit(button[1], (x, y + 150))

    if b5 == 0:
        screen.blit(button[0], (x + 150, y + 150))
    elif b5 == 1:
        screen.blit(button[1], (x + 150, y + 150))

    if b6 == 0:
        screen.blit(button[0], (x + 300, y + 150))
    elif b6 == 1:
        screen.blit(button[1], (x + 300, y + 150))

    if b7 == 0:
        screen.blit(button[0], (x, y + 300))
    elif b7 == 1:
        screen.blit(button[1], (x, y + 300))

    if b8 == 0:
        screen.blit(button[0], (x + 150, y + 300))
    elif b8 == 1:
        screen.blit(button[1], (x + 150, y + 300))

    if b9 == 0:
        screen.blit(button[0], (x + 300, y + 300))
    elif b9 == 1:
        screen.blit(button[1], (x + 300, y + 300))

    pygame.display.update()
    flag += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
