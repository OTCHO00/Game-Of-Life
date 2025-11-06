import pygame, sys, random
from grid import Grid
from config import LARGEUR, HAUTEUR, NB_COLONNES, NB_LIGNES, TAILLE_CELLULE, WHITE, FPS
from patterns import GOSPER_GLIDER_GUN, ACORN, PENTADECATHLON, PULSAR, LWSS, DIEHARD

pygame.init()
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Game Of Life")
grid = Grid()
clock = pygame.time.Clock()
running = True
simulation = False
patterns = [GOSPER_GLIDER_GUN, ACORN, PENTADECATHLON, PULSAR, LWSS, DIEHARD]

while running:
    for event in pygame.event.get():

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            grid.toggle_cel(y // TAILLE_CELLULE, x // TAILLE_CELLULE)

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_SPACE:
                grid.clear()
            if event.key == pygame.K_s:
                simulation = not simulation
    
            if event.key == pygame.K_1:
                x, y = pygame.mouse.get_pos()
                grid.insert_patterns(random.choice(patterns), y // TAILLE_CELLULE, x // TAILLE_CELLULE)
            
            if event.key == pygame.K_RIGHT:
                FPS += 2
            if event.key == pygame.K_LEFT:
                FPS -= 2
                if FPS < 1:
                    FPS = 1

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    fenetre.fill((0, 0, 0))
    
    for row in range(0, NB_LIGNES):
        for col in range(0, NB_COLONNES):
            if grid.get_cell(row, col):
                pixel_x, pixel_y = col * TAILLE_CELLULE, row * TAILLE_CELLULE
                rect = rect = pygame.Rect(pixel_x, pixel_y, TAILLE_CELLULE, TAILLE_CELLULE)
                pygame.draw.rect(fenetre, WHITE, rect)

    pygame.display.flip()

    if simulation:
        grid.update()

    clock.tick(FPS)