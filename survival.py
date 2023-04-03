import pygame, sys
from pygame.locals import *

pygame.init()

# määrittelee pelialueen koon
screen = pygame.display.set_mode((500, 300))
pygame.display.set_caption('Survival Game')

#Vihollinen
enemy = pygame.Rect(250, 150, 30,10)
enemy_speed = [3, 1] 
explosion = pygame.image.load('download.png')  

#tallennetaan hiiren sijainti
mouse= pygame.mouse.get_pos()

#piirretään pelaaja samaan paikkaan kuin hiiri
player= pygame.Rect(mouse[0], mouse[1], 30, 30)
#print (mouse)

FPS = 200
FramePerSec = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
          pygame.quit()
          sys.exit()
        if event.type == MOUSEMOTION:
          mouse = event.pos
          #print (mouse)
          player = pygame.Rect(mouse[0], mouse [1], 30,30)

    enemy.move_ip(enemy_speed)
    #Enemy movement
    if enemy.left < 0:
      enemy_speed[0] *= -1
    if enemy.right > 500:
      enemy_speed[0] *= -1
    if enemy.top < 0:
      enemy_speed[1] *= -1
    if enemy.bottom > 250:
      enemy_speed[1] *= -1
    #taustaväri
    screen.fill("#127f99")

    #piirretään player
    pygame.draw.rect(screen, (100,100,200), player)

    #piirretään talo
    pygame.draw.rect(screen, "brown",(300,210, 70,40))
    #piirretään katto
    pygame.draw.polygon(screen, "green", [(300, 210), (335, 190), (370, 210)])      
    #piirretään maa
    pygame.draw.rect(screen, "#b38600", (0, 250, 500, 50))

    #piirretään kiviä
    pygame.draw.ellipse(screen, "gray", (50, 235, 50, 20))
    pygame.draw.ellipse(screen, "gray", (380, 232, 40, 20))
    pygame.draw.ellipse(screen, "gray", (250, 220, 40, 35))
    pygame.draw.ellipse(screen, "gray", (170, 228, 40, 30))

    #piirretään vihollinen
    pygame.draw.rect(screen, "white", enemy)

    if  pygame.Rect.colliderect(player, enemy) == True:
      print("Hit Ocurred")
      explosion = pygame.transform.scale(explosion, (100, 100))
      player.move_ip(-50, -50)
    #shows the player avatar for the explosion image
      screen.blit(explosion, player)
      enemy_speed = [0,0]
    
      pygame.display.update()
      break
   
    pygame.display.update()
    FramePerSec.tick(FPS)