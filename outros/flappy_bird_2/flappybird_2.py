import pygame
import random
import os

dir = os.path.realpath(os.path.dirname(__file__))

bird = pygame.transform.scale(pygame.image.load(os.path.join(dir,'pasro.png')),(40,40))
post_0 = pygame.transform.scale(pygame.image.load(os.path.join(dir,'poste.png')),(60,320))
post_1 = pygame.transform.rotate(post_0,180)
sky  = pygame.transform.scale(pygame.image.load(os.path.join(dir,'ceu.png'))  ,(600,400))

running = True
dt = 0

clock = pygame.Clock()
screen = pygame.display.set_mode((600,400))
pygame.init()

font = pygame.font.Font(pygame.font.match_font('consolas'),20)

PAUSED = True
SCORE = 0
GAP = 120

player = pygame.rect.Rect(100,200,40,40)
y_speed = 0

sky_rect = [
    pygame.rect.Rect(0  ,0,600,400),
    pygame.rect.Rect(600,0,600,400)
    ]

pipes = [
    [pygame.rect.Rect(600,0,60,400),pygame.rect.Rect(600,0,60,400)],
    [pygame.rect.Rect(900,0,60,400),pygame.rect.Rect(900,0,60,400)]
]
passed = [False,False]


pipes[0][0].bottom = random.randint(0,400-(GAP+10))
pipes[1][0].bottom = random.randint(0,400-(GAP+10))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == 32:
                y_speed = -200
                if PAUSED:
                    SCORE = 0
                    pipes[0][0].bottom = random.randint(0,400-(GAP+10))
                    pipes[1][0].bottom = random.randint(0,400-(GAP+10))
                    pipes[0][0].left = 600
                    pipes[1][0].left = 900
                    player.topleft = 100, 200
                    PAUSED = False
    screen.fill('black')


    if not PAUSED:
        y_speed += 5
        player.top += y_speed*dt

        sky_rect[0].left -= 1
        sky_rect[1].left -= 1
        if sky_rect[0].right < 0:
            sky_rect[0].left = 600
        if sky_rect[1].right < 0:
            sky_rect[1].left = 600

        for i, pair in enumerate(pipes):
            if pair[0].right < 0:
                passed[i] = False
                pair[0].bottom = random.randint(0,400-(GAP+10))
                pair[0].left = 601

            pair[0].left -= 100*dt
            pair[1].topleft = (pair[0].left,pair[0].bottom+GAP)

            if player.colliderect(pair[0]) or player.colliderect(pair[1]):
                PAUSED = True
            elif player.left > pair[0].right and not passed[i]:
                SCORE += 1
                passed[i] = True

    screen.blit(sky,sky_rect[0])
    screen.blit(sky,sky_rect[1])

    screen.blit(post_1,(pipes[0][0].left,pipes[0][0].bottom-320))
    screen.blit(post_1,(pipes[1][0].left,pipes[1][0].bottom-320))

    screen.blit(post_0,pipes[0][1])
    screen.blit(post_0,pipes[1][1])

    screen.blit(bird,player)
    screen.blit(font.render(f'SCORE: {SCORE}',False,'white'),(20,20))
    
    pygame.display.flip()
    dt = clock.tick(60)/1000