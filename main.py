'''          => Welcome to the game of Space Invaders <=
    Instructions:
    Shoot the enemy using the space bar and move the player left and right with arrow keys. Try to get to Level 10! Good Luck!         '''

import math
import random
import pygame

# Initialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load('background.png')
background = pygame.transform.scale(background, (800, 600))

# Caption and Icon
pygame.display.set_caption("Space Invader")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('player.png')
playerImg = pygame.transform.scale(playerImg, (65, 80))
playerX = 370
playerY = 480
 # For moving the player later on
playerX_change = 0

# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 10

for i in range(num_of_enemies):
  enemyImg.append(pygame.image.load('enemy.png'))
  enemyX.append(random.randint(0, 736))
  enemyY.append(random.randint(50, 150))
  enemyX_change.append(4)
  enemyY_change.append(40)          


# Bullet

# Ready - You can't see the bullet on the screen
# Fire - The bullet is currently moving

bulletImg = pygame.image.load('bullet.png')
bulletImg = pygame.transform.scale(bulletImg, (30, 50))
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 50
bullet_state = "ready"

# Score

score_value = 0
font = pygame.font.Font('sansbold.ttf', 32)
level_value = 1

textX = 10
testY = 10
levelX = 10
levelY = 50

# Game Over
over_font = pygame.font.Font('sansbold.ttf', 64)


def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))
    

def show_level(x, y):
  level = font.render("Level : " + str(level_value), True, (255, 255, 255))
  screen.blit(level, (x, y))


def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))

def you_win_text():
    over_text = over_font.render("YOU WIN", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))

def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10)) #35 or 16


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False


# Game Loop
running = True
while running:

    screen.fill((0, 0, 0))
    # Background Image
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -10
            if event.key == pygame.K_RIGHT:
                playerX_change = 10
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                
                    # Get the current x cordinate of the spaceship
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
        # Control player and stops when not pressing/holding keys
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # 5 = 5 + -0.1 -> 5 = 5 - 0.1
    # 5 = 5 + 0.1

    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # Enemy Movement
    for i in range(num_of_enemies):

        # Game Over
        if enemyY[i] > 440:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break
        

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 4
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -4
            enemyY[i] += enemyY_change[i]

        # Collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
          
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, 736)
            enemyY[i] = random.randint(50, 150)

        enemy(enemyX[i], enemyY[i], i)

        # Levels
        if score_value == 20:
          playerImg = pygame.image.load('player.png')
          bulletImg = pygame.image.load('bullet.png')
          bulletImg = pygame.transform.scale(bulletImg, (30, 50))
          level_value = 2
          bulletY_change = 45
        if score_value == 30:
          playerImg = pygame.image.load('spaceship.png')
          playerImg = pygame.transform.scale(playerImg, (65, 80))
          
          level_value = 3
          bulletY_change = 40
        if score_value == 40:
          playerImg = pygame.image.load('player.png')
          bulletImg = pygame.image.load('bullet.png')
          bulletImg = pygame.transform.scale(bulletImg, (30, 50))
          level_value = 4
          bulletY_change = 35
        if score_value == 50:
          playerImg = pygame.image.load('spaceship.png')
          playerImg = pygame.transform.scale(playerImg, (65, 80))
          
          level_value = 5
          bulletY_change = 30
        if score_value == 60:
          playerImg = pygame.image.load('player.png')
          bulletImg = pygame.image.load('bullet.png')
          bulletImg = pygame.transform.scale(bulletImg, (30, 50))
          level_value = 6
          bulletY_change = 25
        if score_value == 70:
          playerImg = pygame.image.load('spaceship.png')
          playerImg = pygame.transform.scale(playerImg, (65, 80))
          
          level_value = 7
          bulletY_change = 20
        if score_value == 80:
          playerImg = pygame.image.load('player.png')
          bulletImg = pygame.image.load('bullet.png')
          bulletImg = pygame.transform.scale(bulletImg, (30, 50))
          level_value = 8
          bulletY_change = 15
        if score_value == 90:
          playerImg = pygame.image.load('spaceship.png')
          playerImg = pygame.transform.scale(playerImg, (65, 80))
          
          level_value = 9
          bulletY_change = 15
        if score_value == 100:
          playerImg = pygame.image.load('player.png')
          bulletImg = pygame.image.load('bullet.png')
          bulletImg = pygame.transform.scale(bulletImg, (30, 50))
          level_value = 10
          bulletY_change = 15
          you_win_text()
          break
        if score_value > 100:
          level_value = "INFINITE SECRET PASSAGE"
          bulletY_change = 50
    
    # Bullet Movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)
    show_score(textX, testY)
    show_level(levelX,levelY)
    pygame.display.update()