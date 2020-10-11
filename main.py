from tkinter import *
from tkinter import filedialog
import os
import tkinter.messagebox as box
from pygame import mixer

filename = ''
paused = False
root = Tk()
menubar = Menu(root)
root.config(menu=menubar)
root['background']='#856ff8'

def browseFile():
    global filename
    filename = filedialog.askopenfilename()
    

submenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=submenu)
submenu.add_command(label="Openfile", command=browseFile)
submenu.add_command(label="Exit", command=root.destroy)

def aboutUs():
    box.showinfo(title="Melody Music Player", message="Simple music player using Tkinter-Python\nGithub:"+"ShriramShagri/Melody")

submenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=submenu)
submenu.add_command(label="About Us", command=aboutUs)
submenu.add_command(label="Info")

mixer.init()

root.geometry(f'600x300+{(root.winfo_screenwidth()-600)//2}+{(root.winfo_screenheight()-300)//2}')
root.title("Melody")
root.iconbitmap(r'./assets/favicon.ico')

heading = Label(root, text="Play Music")
heading.pack(pady=10)


def playMusic():
    if paused:
        mixer.music.unpause()
    else:
        if filename=='':
            box.showerror(title="Choose a File!!", message="No File choosen. please choose a file.")
        elif filename.endswith('.mp3'):
            mixer.music.load(filename)
            mixer.music.play()
            statusbar['text'] = "Now Playing: "+os.path.basename(filename)
        else:
            box.showerror(title="Invalid!!", message="Filetype is Invalid.\nPlease check the choosen file or supported codec")
            mixer.music.stop()


def stopMusic():
    mixer.music.stop()
    statusbar['text'] = "Stopped: "+os.path.basename(filename)

def pauseMusic():
    global paused
    paused = True
    mixer.music.pause()
    statusbar['text'] = "Paused: "+os.path.basename(filename)

def setVolume(val):
    mixer.music.set_volume(int(val)/100)


middleFrame = Frame(root, bg="#856ff8")
middleFrame.pack(padx = 10, pady=10)

play_photo = PhotoImage(file="./assets/play.png")
play_btn = Button(middleFrame, bg="#856ff8", image=play_photo, command=playMusic)
play_btn.pack(side=LEFT, padx = 10)

pause_photo = PhotoImage(file="./assets/pause.png")
pause_btn = Button(middleFrame, bg="#856ff8", image=pause_photo, command=pauseMusic)
pause_btn.pack(side=LEFT, padx = 10)

stop_photo = PhotoImage(file="./assets/stop.png")
stop_btn = Button(middleFrame, bg="#856ff8", image=stop_photo, command=stopMusic)
stop_btn.pack(side=LEFT, padx = 10)

volume = Scale(root, from_=0, to=100, orient=HORIZONTAL, command=setVolume)
volume.set(50)
mixer.music.set_volume(0.5)
volume.pack()

statusbar = Label(root, text="Welcome To melody", relief=SUNKEN)
statusbar.pack(side=BOTTOM, fill=X)

root.mainloop()