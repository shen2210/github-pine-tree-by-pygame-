import pygame
from random import randint

# Initialize values for color (RGB format)
BLACK = (0,0,0)
GREEN = (3,160,98)
RED = (255,0,0)
BROWN = (165,42,42)
WHITE = (230,255,255)
STARRY = (230,255,80 )
(width,height) = (600,500)

running = True

def draw_tree(screen):
    pygame.draw.rect(screen,BROWN,[260,400,30,50])
    pygame.draw.polygon(screen,GREEN, [[350, 400], [275, 250], [200, 400]])
    pygame.draw.polygon(screen,GREEN, [[340, 350], [275, 230], [210, 350]])
    pygame.draw.polygon(screen,GREEN, [[330, 300], [275, 210], [220, 300]])

def draw_circle(screen):
    random_color = (randint(0,255),randint(0,255),randint(0,255))
     
    pygame.draw.circle(screen,random_color,(310, 300),10)
    pygame.draw.circle(screen,random_color,(230, 350),10)
    pygame.draw.circle(screen,random_color,(240, 300),10)
    pygame.draw.circle(screen,random_color,(320, 350),10)
    pygame.draw.circle(screen,random_color,(210, 393),10)
    pygame.draw.circle(screen,random_color,(340, 393),10)

def main():
    global running
    random_pos = (80,80)

    pygame.init()

    screen = pygame.display.set_mode((width,height))
    pygame.display.set_caption("Pine Tree")
   
    clock = pygame.time.Clock()
    background = BLACK

    font = pygame.font.SysFont('sans',30)
    text = font.render("Merry Christmas",True,RED)
    text_box = text.get_rect()

    while running:
        clock.tick(60)
        screen.fill(background)
        
        draw_tree(screen)
        draw_circle(screen)
        
        screen.blit(text,(random_pos))
        pygame.draw.rect(screen,WHITE,(random_pos[0],random_pos[1],text_box[2],text_box[3]))
        screen.blit(text,random_pos)
        
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()

    pygame.quit()

main()
