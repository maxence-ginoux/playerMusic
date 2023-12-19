from tkinter import *
from tkinter import filedialog
from pygame import mixer
import os

def play_musique():
    current_song = playlist.curselection()
    if current_song:
        index = current_song[0]
        song = playlist.get(index)
        mixer.music.load(os.path.join(music_folder, song))
        mixer.music.play()

def pause_musique():
    mixer.music.pause()

def stop_musique():
    mixer.music.stop()

def reprendre_musique():
    mixer.music.unpause()

def volume_musique(valeur):
    volume= float(valeur) / 100
    mixer.music.set_volume(volume)

def ajouter_musique():
    files= filedialog.askopenfilenames(filetypes=[("MP3 files","*.mp3")])
    for file in files:
        playlist.insert(END, file)

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

mixer.init()

root = Tk()
root.title('Lecteur de Media')


playlist = Listbox(root, selectmode=SINGLE, bg="black", fg="white", font=('Arial', 15), width=40)
playlist.grid(columnspan=5)

music_folder = "C:/Users/ginma/Documents/La Plateforme/playerMusic/playerMusic/musique/"  
music_files = [file for file in os.listdir(music_folder) if file.endswith('.mp3')]

for file in music_files:
    playlist.insert(END, file)

# Boutons
precedent_bouton = Button(root, text="précédent", command=precedent_musique)
precedent_bouton.grid(row=1, column=0)

play_bouton = Button(root, text="Play", command=play_musique)
play_bouton.grid(row=1, column=1)

pause_bouton = Button(root, text="Pause", command=pause_musique)
pause_bouton.grid(row=1, column=2)

reprendre_bouton = Button(root, text="Reprendre", command=reprendre_musique)
reprendre_bouton.grid(row=1, column=3)

stop_bouton = Button(root, text="Stop", command=stop_musique)
stop_bouton.grid(row=1, column=4)

suivant_bouton = Button(root, text="suivant", command=suivant_musique)
suivant_bouton.grid(row=1, column=5)

volume_bouton = Scale (root, from_=0,to=100, orient=HORIZONTAL, command=volume_musique)
volume_bouton.set(50)
volume_bouton.grid(row=2, column=3,rowspan=4)

ajouter_music_bouton = Button(root, text="ajouter piste", command= ajouter_musique)
ajouter_music_bouton.grid(row=2, columnspan=2,column=0)


root.mainloop()