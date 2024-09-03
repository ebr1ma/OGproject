import os
import pygame
WIDTH, HEIGHT = 1000,750
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("im a munch")
KONG_HEIGHT, KONG_WIDTH = 100,100
BANANA_HEIGHT, BANANA_WIDTH = 150,150

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)

BORDER = pygame.Rect(WIDTH//2 - 5, 0, 10, HEIGHT)



FPS = 60
VEL = 5
BULLET_VEL = 7
MAX_BULLETS = 6

KONG_HEALTH = 10
BANANA_HEALTH = 10


BANANA_HIT = pygame.USEREVENT + 1
KONG_HIT = pygame.USEREVENT + 2



KONG_IMAGE = pygame.image.load(os.path.join('Assets', 'kong.png'))
BANANA_IMAGE = pygame.image.load(os.path.join('Assets', 'bananaman.png'))
KONG_= pygame.transform.scale(KONG_IMAGE, (KONG_HEIGHT, KONG_WIDTH))
BANANA_= pygame.transform.scale(BANANA_IMAGE, (BANANA_HEIGHT, BANANA_WIDTH))
kong = pygame.Rect(800,350, KONG_HEIGHT, KONG_WIDTH)
banana = pygame.Rect(75,350, BANANA_HEIGHT, BANANA_WIDTH)

CHICKEN = pygame.transform.scale(pygame.image.load(
     os.path.join('Assets', 'space.png')), (WIDTH,HEIGHT))

def draw_window(kong, banana, kong_bullets, banana_bullets):
    WIN.blit(CHICKEN, (0,0))
    pygame.draw.rect(WIN, BLACK, BORDER)
    WIN.blit(KONG_,(kong.x,kong.y))
    WIN.blit(BANANA_,(banana.x,banana.y))
    for bullets in kong_bullets:
         pygame.draw.rect(WIN, RED, bullets)
         
    for bullets in banana_bullets:
         pygame.draw.rect(WIN, YELLOW, bullets)
         
    pygame.display.update()
def kong_handle_movement(keys_pressed,kong):
        if keys_pressed[pygame.K_a] and kong.x-VEL > BORDER.x + BORDER.width: #LEFT
            kong.x -= VEL
        if keys_pressed[pygame.K_d] and kong.x+VEL+kong.width <WIDTH: #RIGHT
            kong.x += VEL
        if keys_pressed[pygame.K_w] and kong.y-VEL >0: #UP
            kong.y -= VEL
        if keys_pressed[pygame.K_s]and kong.y + VEL+ kong.height <HEIGHT-5: #DOWN
            kong.y += VEL
def banana_handle_movement(keys_pressed,banana):
        if keys_pressed[pygame.K_LEFT] and banana.x-VEL >0: #LEFT
            banana.x -= VEL
        if keys_pressed[pygame.K_RIGHT] and banana.x+VEL+banana.width <BORDER.x  : #RIGHT
            banana.x += VEL
        if keys_pressed[pygame.K_UP] and banana.y-VEL >0: #UP
            banana.y -= VEL
        if keys_pressed[pygame.K_DOWN]and banana.y + VEL+ banana.height <HEIGHT-5: #DOWN
            banana.y += VEL

def handle_bullets(banana_bullets, kong_bullets, banana, kong):
     for bullets in banana_bullets:
          bullets.x += BULLET_VEL
          if kong.colliderect(bullets):
               pygame.event.post(pygame.event.Event(KONG_HIT))
               banana_bullets.remove(bullets)
          elif bullets.x > WIDTH:
               banana_bullets.remove(bullets)     
     for bullets in kong_bullets:
          bullets.x -= BULLET_VEL
          if banana.colliderect(bullets):
               pygame.event.post(pygame.event.Event(BANANA_HIT))
               kong_bullets.remove(bullets)
          elif bullets.x < 0:
               kong_bullets.remove(bullets)
def main():
    banana_bullets = []
    kong_bullets = []
    clock = pygame.time.Clock()
    
    
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run= False
            if event.type==pygame.KEYDOWN:
                 if event.key==pygame.K_RSHIFT and len(banana_bullets) < MAX_BULLETS :
                      bullet = pygame.Rect(banana.x+banana.width, banana.y+ banana.height//2 -2, 10,5) 
                      banana_bullets.append(bullet)
                
                 if event.key==pygame.K_e and len(kong_bullets) < MAX_BULLETS:
                      bullet = pygame.Rect(kong.x, kong.y+ kong.height//2 -2, 10,5) 
                      kong_bullets.append(bullet)
       
                       
        keys_pressed = pygame.key.get_pressed()
        kong_handle_movement(keys_pressed,kong)
        banana_handle_movement(keys_pressed,banana)
        draw_window(kong, banana, kong_bullets, banana_bullets)

        handle_bullets(banana_bullets, kong_bullets, banana, kong)
    pygame.quit()
if __name__ == '__main__': 
    main()
        