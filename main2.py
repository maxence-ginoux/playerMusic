from tkinter import *
from pygame import mixer
import os
import pygame

# Initialisation
mixer.init()
pygame.init()

root = Tk()
root.title("playerMusic")


def play_musique():
    currentsong = playlist.get(ACTIVE)
    mixer.music.load(currentsong)
    mixer.music.play()

def pause_musique():
    mixer.music.pause()

def stop_musique():
    mixer.music.stop()

def resume_musique():
    mixer.music.unpause()

def suivant_musique():
    current_index = playlist.curselection()
    next_index = current_index[0] + 1 if current_index else 0
    if next_index < playlist.size():
        playlist.selection_clear(0, END)
        playlist.selection_set(next_index)

def precedent_musique():
    current_index = playlist.curselection()
    prev_index = current_index[0] - 1 if current_index else 0
    if prev_index >= 0:
        playlist.selection_clear(0, END)
        playlist.selection_set(prev_index)

# Liste des chansons
playlist = Listbox(root, selectmode=SINGLE, bg="black", fg="white", font=('arial', 15), width=40)
playlist.grid(columnspan=5)

# Chargement des chansons du répertoire courant
os.chdir("C:/Users/ginma/Documents/La Plateforme/playerMusic/playerMusic/musique/")
songs = os.listdir()

for s in songs:
    playlist.insert(END, s)

# Boutons interactifs
precedent_bouton = Button(root, text="précédent", command=precedent_musique)
precedent_bouton.grid(row=1, column=0)

play_bouton = Button(root, text="Play", command=play_musique)
play_bouton.grid(row=1, column=1)

pause_bouton = Button(root, text="Pause", command=pause_musique)
pause_bouton.grid(row=1, column=2)

Resume_bouton = Button(root, text="Resume", command=resume_musique)
Resume_bouton.grid(row=1, column=3)

stop_bouton = Button(root, text="Stop", command=stop_musique)
stop_bouton.grid(row=1, column=4)

suivant_bouton = Button(root, text="suivant", command=suivant_musique)
suivant_bouton.grid(row=1, column=5)


mainloop()
