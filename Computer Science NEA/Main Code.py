import pygame
import button

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

#buttons
start_img = pygame.image.load("Start_btn.png").convert_alpha()
exit_img = pygame.image.load("Exit_btn.png").convert_alpha()
    
start_button = button.Button(400, 50, start_img, 0.6)
exit_button = button.Button(465,300, exit_img, 0.6)


#game loop
run = True
while run:
    draw_bg()
    
    start_button.draw(screen)
    if exit_button.draw(screen):
        run = False 
            
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("
        if event.type == pygame.QUIT:
            run = False
        
        pygame.display.update()
    
   
            
pygame.quit()



