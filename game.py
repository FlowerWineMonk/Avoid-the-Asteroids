import pygame
import random
import sys

WIDTH = 800
HEIGHT = 600

# initialization
pygame.init()

screen = pygame.display.set_mode((WIDTH,HEIGHT))

player = pygame.Rect(WIDTH / 2, HEIGHT / 2, 20, 20)

asteroids = []
for i in range(10):
    x = random.randint(0, WIDTH)
    y = random.randint(0, HEIGHT)
    asteroids.append(pygame.Rect(x, y, 50, 50))

bullets = []
for k in range(1):
    bullet_x = player.x + player.width //2
    bullet_y = player.y
    bullets.append(pygame.Rect(bullet_x, bullet_y, 5, 10)) 


font = pygame.font.Font(None, 30)

clock = pygame.time.Clock()

score = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        bullet_x = player.x + player.width // 2
        bullet_y = player.y
        bullets.append(pygame.Rect(bullet_x, bullet_y, 5, 10))
    if keys[pygame.K_LEFT]:
        player.x -= 10
    if keys[pygame.K_RIGHT]:
        player.x += 10
    if keys[pygame.K_UP]:
        player.y -= 10
    if keys[pygame.K_DOWN]:
        player.y += 10

    # update player position
    player.clamp_ip(pygame.Rect(0, 0, WIDTH, HEIGHT))
    # update asteroids
    for asteroid in asteroids:
        asteroid.y += 10
        if asteroid.y > HEIGHT:
            asteroid.y = 0
            asteroid.x = random.randint(0, WIDTH)
        # check for collsions
        for asteroid in asteroids:
            if player.colliderect(asteroid):
                score -= 1
                asteroid.x = random.randint(0, WIDTH)
                asteroid.y = 0

    for bullet in bullets:
        bullet.y -= 10
        if bullet.y < 0:
            bullets.remove(bullet)

    for bullet in bullets:
        for asteroid in asteroids:
            if bullet.colliderect(asteroid):
                bullets.remove(bullet)
                asteroid.x = random.randint(0, WIDTH)
                asteroid.y = 0
                score+=1

    # draw objects
    screen.fill((0, 255, 255))
    for asteroid in asteroids:
        pygame.draw.rect(screen, (255, 255, 0), asteroid)
    for bullet in bullets:
        pygame.draw.rect(screen, (0,0,255), bullet)
    pygame.draw.rect(screen, (255, 0, 0), player)
    # draw score
    text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(text, (10, 10))
    # update screen
    pygame.display.flip()
    # tick the clock
    clock.tick(60)
