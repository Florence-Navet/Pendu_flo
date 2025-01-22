import pygame

    
pygame.init()

res = (640,480)

#paramètre de la fenêtre // retourne aussi un objet surface

screen = pygame.display.set_mode((res))


#un booleen pour maintenir la fenetre de jeu ouverte
launched = True
image = pygame.image.load('logo.png')


while launched:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
             launched = False

     

    pygame.display.flip()

pygame.quit()