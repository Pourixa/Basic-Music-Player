from tkinter import *
from tkinter import filedialog
import pygame 
from pygame import mixer
music=[]
allm=[]
pygame.init()
def browseFiles():
        filetypes = (
        ('audio files', ["*.mp3","*.wav"]),
        ('All files', '*.*')
    )
        
        filename = filedialog.askopenfilenames(
        title='Select Music',
        initialdir='C:\',
        filetypes=filetypes)
        global music
        for i in range(len(filename)):
            nusic=filename[i]
            allm.append(nusic)
            index=nusic.rfind("/")
            filename1=nusic[index+1:]
            filename1=filename1.replace(".mp3","")
            music.append(filename1)
            musics_var = StringVar(value=music)
            list1.configure(listvariable=musics_var)

def play():
    global i
    i=allm[0]
    mixer.music.load(i)
    i=allm.index(i)
    musiclbl.configure(text="Music: "+music[i])
    mixer.music.play()
def pause():
    mixer.music.pause()
def unpause():
    mixer.music.unpause()
def next():
    try:
        global i
        i=allm[i+1]
        mixer.music.load(i)
        i=allm.index(i)
        mixer.music.play()
        musiclbl.configure(text="Music: "+music[i])
    except IndexError:
        i=allm[0]
        mixer.music.load(i)
        i=allm.index(i)
        mixer.music.play()
        musiclbl.configure(text="Music: "+music[i])
def previous():
    try:
        global i
        i=allm[i-1]
        mixer.music.load(i)
        i=allm.index(i)
        mixer.music.play()
        musiclbl.configure(text="Music: "+music[i])
    except IndexError:
        i=allm[-1]
        mixer.music.load(i)
        i=allm.index(i)
        mixer.music.play()
        musiclbl.configure(text="Music: "+music[i])
def volumeup():
    global volumeint
    mixer.music.set_volume(volumeint+0.1)
    volumeint=round(mixer.music.get_volume(),1)
    volumelbl.configure(text="Volume: "+ str(volumeint))
def volumedown():
    global volumeint
    mixer.music.set_volume(volumeint-0.1)
    volumeint=round(mixer.music.get_volume(),1)
    volumelbl.configure(text="Volume: "+ str(volumeint))
main = Tk()
main.title("N3M3515 Music Player")
main.config(background = "white")
main.geometry("500x500+380+84")
Label(main,text="Basic Music Player",justify="center",font=("segoe print",20),bg="white").pack()
Label(main,text="")
Button(main,text="Select Music",command=browseFiles).pack()
Label(main,text="")
musics_var = ''
list1=Listbox(main, listvariable=musics_var,width=70)
list1.pack()
Button(main,text="Play",command=play).pack()
Button(main,text="Pause",command=pause).pack()
Button(main,text="UnPause",command=unpause).pack()
Button(main,text="Next",command=next).pack()
Button(main,text="Previous",command=previous).pack()
volumeint=round(mixer.music.get_volume(),1)
volumelbl=Label(main,text="Volume: "+ str(volumeint),bg="white")
volumelbl.pack()
Button(main,text="Increase Volume",command=volumeup).pack()
Button(main,text="Decrease Volume",command=volumedown).pack()
musiclbl=Label(main,text="",bg="white")
musiclbl.pack()
main.mainloop()
