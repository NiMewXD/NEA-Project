
import pygame

pygame.init()



    
#main menu window
screen_height = 1300
screen_width = 600
screen = pygame.display.set_mode((screen_height, screen_width))


pygame.display.set_caption("GOTY")


    #game backgrounds
bg_image = pygame.image.load("Startscreen.png").convert_alpha()

def draw_bg():
    scaled_bg = pygame.transform.scale(bg_image,(screen_height, screen_width))
    screen.blit(scaled_bg, (0,0))

    #game loop
run = True
while run:
            
    draw_bg()
            
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
                    
        pygame.display.update()
                    
    pygame.quit()
