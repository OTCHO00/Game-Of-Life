# Game of Life

Simulation du Jeu de la Vie de Conway en Python avec Pygame.

## Screenshot
![Game of Life](img.png)

## Règles du Jeu
- Cellule vivante < 2 voisins → meurt (solitude)
- Cellule vivante 2-3 voisins → survit
- Cellule vivante > 3 voisins → meurt (surpopulation)
- Cellule morte 3 voisins → naît (reproduction)

## Contrôles
- **Clic souris** : Dessiner/effacer cellules
- **S** : Démarrer/Arrêter simulation
- **ESPACE** : Effacer grille
- **1** : Insérer pattern aléatoire à la souris
- **←/→** : Ralentir/Accélérer

## Patterns inclus
- Gosper Glider Gun (génère des gliders)
- Pulsar (oscillateur magnifique)
- LWSS (vaisseau horizontal)
- Pentadecathlon (longue période)
- Acorn (chaos pendant 5206 générations)
- Diehard (meurt après 130 générations)