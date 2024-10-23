import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Test Pygame")

background_color = (0, 0, 0)  # Czarny

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    screen.fill(background_color)
    
    pygame.draw.rect(screen, (255, 0, 0), (100, 100, 200, 150))

    pygame.display.flip() 