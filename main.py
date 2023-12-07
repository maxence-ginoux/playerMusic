import pygame
from pygame import mixer
import tkinter


pygame.init()
mixer.init()

pygame.display.set_caption("playerMusic")
fenetre = pygame.display.set_mode((500, 400))

# LESMUSIQUES
piste1 = pygame.mixer.music.load("media/unesourisverte.mp3")
piste2 = pygame.mixer.music.load("media/lepetitbonhomme.mp3")
playlist = (piste1, piste2)

# LES IMAGES
fond = pygame.image.load("media/image2.webp")
fond = fond.convert()


# PARAMETRES DE DEPART
running = True
volume = 50

# CORPS DU PROGRAMME
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # pygame.QUIT pour fermer la fenêtre
            running = False
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN: # Si le clic de la souris est dans la zone du bouton
            if 100 <= event.pos[0] <= 300 and 100 <= event.pos[1] <= 150: # Augmentation du volume
                if volume < 100:  # Limite le volume à 100
                    volume += 10  # Augmentation de 10 unités
    fenetre.blit(fond, (0,0)) # OU fenetre.fill((125,235,110)) # POUR LA COULEUR DE FOND
    pygame.display.flip() # POUR AFFICHER LE FOND


# LES FONCTIONS
def bouton_play():
    mixer.music.load(playlist)
    mixer.music.play()


def bouton_stop():
    mixer.music.stop()

def bouton_pause():
    mixer.music.pause()
                    
def bouton_resume():
    mixer.music.unpause()

#def bouton_suivant():


#def bouton_precedent():


#def bouton_aleatoire():


#def bouton_repeat():


def bouton_volumeplus():
    font = pygame.font.Font(None, 36)
    texte = font.render("Augmenter le Volume", True)
    pygame.draw.rect(fenetre(100, 100, 200, 50))
    # fenetre.blit(texte, (110, 110))


#def bouton_volumemoins():
