import tkinter as tk
from tkinter import *
from tkinter import filedialog
import pygame
from time import strftime 
from tkinter.ttk import *
from tkinter import messagebox
from tkinter.messagebox import *
import sys
import time
from PIL import ImageTk,Image
import turtle
import speech_recognition as sr
root = tk.Tk()
root.title('Play World')
root.minsize(300 , 330)
root.maxsize(300,330)
root.geometry('300x330')
root.config(bg='black')
root.wm_iconbitmap('j1.ico')
r = sr.Recognizer()

#background= pygame.image.load('')

C = Canvas(height=250, width=300)
#C:\Users\UNEEB\Downloads\python\music
filename = PhotoImage(file = "C://Users//Saifullah//Downloads//music//oop.png")
background_label = Label(image=filename)
background_label.place(x=0, y=90, relwidth=960, relheight=1)

#img = PhotoImage(file="C:/Users/z tech/Downloads/Music-Player-main/dd.png")
#label = Label(
 #   root,
  #  image=img
#)
menubar = Menu(root)  
root.config(menu=menubar)  

file = Menu(menubar, tearoff=0)  
file.add_command(label="New", command=BROWSE)  
file.add_command(label="Open", command=BROWSE)  
file.add_command(label="Close", command=exit)  
  
file.add_separator()  
  
file.add_command(label="Exit", command=root.quit)  
  
menubar.add_cascade(label="File", menu=file)  
edit = Menu(menubar, tearoff=0)  
edit.add_command(label="Undo")  
menubar.add_cascade(label="Edit", menu=edit)  
help = Menu(menubar, tearoff=0)  
help.add_command(label="About")  
menubar.add_cascade(label="Help", command=lambda: showinfo(
        title='Help',
        message='This Software Made By SaifUllah \n Cont: Pak Austria University haripur\n\nBy Play World Music App')
)
def time():
	string = strftime('%H: %M: %S %p')
	label.config(text=string)
	label.after(1000, time)

label = Label(root,font=("ds-digital",30))
label.pack(anchor='center')
time()	

pygame.mixer.init()




song_list = tk.Listbox(root,width=60,fg='yellow',bg='black')
song_list.pack(pady=5)

def add_song():
		songs = filedialog.askopenfilenames(initialdir='C://Users//Saifullah//Downloads//',title='Add Music',filetypes=(('mp3 Files' , '*.mp3'),))
		for song in songs:
			songs = song.replace('C:/Users/Saifullah/Downloads/','')
			song_list.insert(END,songs)

def play_song():
	song = song_list.get(ACTIVE)
	song =  f'C:/Users/Saifullah/Downloads/{song}'
	pygame.mixer.music.load(song)
	pygame.mixer.music.play(loops=0)
def stop_song():
	pygame.mixer.music.stop()
	song_list.selection_clear(ACTIVE)

global paused
paused=False
def pause_song():
	global paused
	if paused:
		pygame.mixer.music.unpause()
		paused = False
	else:
		pygame.mixer.music.pause()
		paused = True

def play_next_song():
	next_song = song_list.curselection()
	next_song = next_song[0]+1
	song = song_list.get(next_song)
	song = f'C:/Users/Saifullah/Downloads/{song}'
	pygame.mixer.music.load(song)
	pygame.mixer.music.play(loops=0)
	song_list.selection_clear(0,END)
	song_list.selection_set(next_song,last=None) 

def play_previous_song():
	next_song = song_list.curselection()
	next_song = next_song[0]-1
	song = song_list.get(next_song)
	song = f'C:/Users/Saifullah/Downloads/{song}'
	pygame.mixer.music.load(song)
	pygame.mixer.music.play(loops=0)
	song_list.selection_clear(0,END)
	song_list.selection_set(next_song,last=None) 
def translator():
    audio = 'song.WAV'
    try:
        with sr.AudioFile(audio) as source:
            audio = r.record(source)
            print('Done!')

        text = r.recognize_google(audio)
        print(text)

    except Exception as e:
        print(e)	
frame = tk.Frame(root,bg='black')
frame.pack()
photo1 = PhotoImage(file = r"C:/Users/Saifullah/Downloads/music/po1.png")
photo2 = PhotoImage(file = r"C:/Users/Saifullah/Downloads/music/play1.png")
photo3 = PhotoImage(file = r"C:/Users/Saifullah/Downloads/music/pk.png")
photo4 = PhotoImage(file = r"C:/Users/Saifullah/Downloads/music/next.png")
#photo4 = PhotoImage(file = r"C:\Users\UNEEB\Downloads\Music-Player-main\next.png")
photo5 = PhotoImage(file = r"C:/Users/Saifullah/Downloads/music/bak1.png")
photo6 = PhotoImage(file = r"C:/Users/Saifullah/Downloads/music/add1.png")


  
photoimage1 = photo1.subsample(3, 3)
photoimage2 = photo2.subsample(3, 3)
photoimage3 = photo3.subsample(3, 3)
photoimage4 = photo4.subsample(5, 5)
photoimage5 = photo5.subsample(4, 4)
photoimage6 = photo6.subsample(3, 4)
play_button = tk.Button(frame,text='Play',padx=10,pady=10,command=play_song,bg='black', image = photoimage1)
pause_button = tk.Button(frame,text='Pause',padx=10,pady=10,command=pause_song,bg='black',image = photoimage2)
next_button = tk.Button(frame,text='Next',padx=10,pady=10,command=play_next_song,bg='black',image=photoimage4)
stop_button = tk.Button(frame,text='Stop',padx=10,pady=10,command=stop_song,bg='black', image= photoimage3)
previous_button = tk.Button(frame,text='Previous',padx=10,pady=10,command=play_previous_song,bg='black',image=photoimage5)

play_button.pack(side=LEFT,padx=2)
pause_button.pack(side=LEFT,padx=2)
next_button.pack(side=LEFT,padx=2)
stop_button.pack(side=LEFT,padx=2)
previous_button.pack(side=LEFT,padx=2)

add_song_btn = tk.Button(root,text='Add Songs',padx=1,pady=3,command=add_song,bg='black',image=photoimage6)
add_song_btn.pack(pady=1)

#add_translator_btn = tk.Button(root,text='Add Songs',padx=1,pady=3,command=translator,bg='black',image=photoimage6)
#add_song_btn.pack(pady=1)
#translator_btn = tk.Button(frame,text='Translator',padx=2,pady=4,command=translator,bg='White')
#translator_btn.pack(pady=1)


root.mainloop()