import pygame
import sys
import random

# Initialize pygame
pygame.init()

screen_width, screen_height = 1800, 900
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Moving Dinosaur Game")

black = (0, 0, 0)
blue = (0, 0, 255)
white = (255, 255, 255)

dino_image = pygame.image.load("immage.png")
dino_image = pygame.transform.scale(dino_image, (100, 100))
dino_rect = dino_image.get_rect()
dino_rect.topleft = (screen_width // 8, screen_height - dino_rect.height - 50)
dino_speed = 5

falling_objects = []
falling_speed = 5
spawn_event = pygame.USEREVENT + 1
pygame.time.set_timer(spawn_event, 1000)


score = 0
font = pygame.font.Font(None, 74)


running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == spawn_event:
            obj_x = random.randint(0, screen_width - 50)
            obj_rect = pygame.Rect(obj_x, 0, 50, 50)
            falling_objects.append(obj_rect)


    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and dino_rect.left > 0:
        dino_rect.x -= dino_speed
    if keys[pygame.K_RIGHT] and dino_rect.right < screen_width:
        dino_rect.x += dino_speed

    dino_rect.y = screen_height - dino_rect.height - 50


    for obj in falling_objects[:]:
        obj.y += falling_speed
        if obj.colliderect(dino_rect):
            falling_objects.remove(obj)
            score += 1
            dino_speed+=1

    if score == 10:
        falling_speed+=1
        score-=10

    screen.fill(blue)

    ground_height = 50
    pygame.draw.rect(screen, white, (0, screen_height - ground_height, screen_width, ground_height))

    screen.blit(dino_image, dino_rect.topleft)

    for obj in falling_objects:
        pygame.draw.rect(screen, white, obj)

    score_text = font.render(f"Score: {score}", True, white)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
sys.exit()
