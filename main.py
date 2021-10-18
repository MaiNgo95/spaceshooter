import pygame
import random
import math
pygame.init()

screen = pygame.display.set_mode((800,800))
title = pygame.display.set_caption("Space Shooter")
#set icon for title
spaceship = pygame.image.load('spaceship.png')
pygame.display.set_icon(spaceship)
background = pygame.image.load('space.jpg')

#player info
player = pygame.image.load('rocket.png')
playerX = 370
playerY = 400
playerX_change= 0

def playerInfo(x,y):
  screen.blit(player, (playerX, playerY))

enemy = []
enemyX = []
enemyY = []
enemy_change = []
enemyY_change = []
numberofe = 6
for i in range(numberofe):

  enemy.append(pygame.image.load('alien.png'))
  enemyX.append(random.randint(0,700))
  enemyY.append(random.randint(50, 200))
  enemy_change.append(0.3)
  enemyY_change.append(0)

def enemyinfo(x,y,i):
  screen.blit(enemy[i],(x, y))

bullet = pygame.image.load('bullet.png')
bulletX = 0
bulletY  = 480
bullet_change = 0
bulletY_change = 3
bullet_state = "ready" #set the bullet to shoot

def shoot_bullet(x,y):
  global bullet_state #get the bullet_stae into func
  bullet_state= "fire"
  screen.blit(bullet, (x+20, y+40))

def collision(enemyX, enemyY, bulletX, bulletY):
  distance = math.sqrt(math.pow(enemyX-enemyY,2)+ math.pow(bulletX-bulletY,2))
  if distance <27:
    return True
score = 0
running = True #get the game running
while running:
  screen.fill((0, 0, 0))
  screen.blit(background,(0,0))
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:
        playerX_change = -1 #check event key for which key is using
      if event.key == pygame.K_RIGHT:
        playerX_change = 1
      if event.key == pygame.K_SPACE: #get the bullet 
       if bullet_state == "ready":
          bulletX = playerX  #buller will not follow the spaceship
          shoot_bullet(bulletX, bulletY)
       
    if event.type == pygame.KEYUP:
      if event.key == pygame.K_LEFT or event.key ==pygame.K_RIGHT:
          playerX_change = 0
 
  playerX += playerX_change
  if playerX <= 0:
    playerX  = 0
  elif playerX >= 700:
    playerX = 700


  for i in range(numberofe):
    enemyX[i] += enemy_change[i]
    if enemyX[i] <= 0:
      enemy_change[i]  = 1
    elif enemyX[i] >= 710:
      enemy_change[i] = -1

    touch = collision(enemyX[i], enemyY[i], bulletX, bulletY)
    if touch:
      bulletY = 480
      bullet_state = "ready"
      score+= 1
      enemyX[i] = random.randint(0,700)
      enemyY[i] = random.randint(50, 200)
    enemyinfo(enemyX[i],enemyY[i],i)
    
  #keep looping the bullet
  if bulletY <= 0:
    bulletY=480
    bullet_state = "ready"

  if bullet_state == "fire":
    shoot_bullet(bulletX, bulletY)
    bulletY -= bulletY_change
  
  
  

  playerInfo(playerX,playerY)
#movement of aliens

  
  #get the new movement
  pygame.display.update()
