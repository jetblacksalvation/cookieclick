import pygame 
import math #needed for square root function


pygame.init()

screen = pygame.display.set_mode((800,800))
mousePos = (0,0) #variable mousePos stores TWO numbers
numClicks = 0
event = pygame.event.Event

cookie =pygame.draw.circle(screen, (200, 0, 200), (400,400), 100)
while 'main':
    for event in pygame.event.get():
        

        if event.type == pygame.QUIT: #close game window
            pygame.quit()
            break

        if event.type == pygame.MOUSEBUTTONDOWN: #check if clicked
            mousePos = event.pos #refreshes mouse position
            if cookie.collidepoint(mousePos):
                numClicks +=1
            print("CLICK")

        if event.type == pygame.MOUSEMOTION: #check if mouse moved
            
            print("mouse position: (",mousePos[0]," , ",mousePos[1])
        #draw stuff here ------ 
    

        print(" you have {} cookies".format(numClicks))
        
        
        pygame.display.flip()
        
    
    pass