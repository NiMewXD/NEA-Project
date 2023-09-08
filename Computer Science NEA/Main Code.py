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
start_img = pygame.image.load("Start_Button.png").convert_alpha()
exit_img = pygame.image.load("Exit_Button.png").convert_alpha()
    
start_button = button.Button(screen_width/2, 300, start_img, 1.5)
exit_button = button.Button(1150,460, exit_img, 0.6)

def start_game():
#game loop
    run = True
    while run:
        draw_bg()
    
        if start_button.draw(screen):
            main_game()
        if exit_button.draw(screen):
            run = False 
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
            pygame.display.update()
    
   
            
    pygame.quit()

def main_game():
    draw_bg()


start_game()




