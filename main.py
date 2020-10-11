from tkinter import *
from tkinter import filedialog
import tkinter.messagebox as box
from pygame import mixer

filename = ''
root = Tk()
menubar = Menu(root)
root.config(menu=menubar)

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

text = Label(root, text="Let's make something nice").pack()


def playMusic():
    if filename=='':
        box.showerror(title="Choose a File!!", message="No File choosen. please choose a file.")
    elif filename.endswith('.mp3'):
        mixer.music.load(filename)
        mixer.music.play()
    else:
        box.showerror(title="Invalid!!", message="Filetype is Invalid.\nPlease check the choosen file or supported codec")
        mixer.music.stop()


def stopMusic():
    mixer.music.stop()

def setVolume(val):
    mixer.music.set_volume(int(val)/100)

play_photo = PhotoImage(file="./assets/play.png")
play_btn = Button(root, image=play_photo, command=playMusic).pack()

stop_photo = PhotoImage(file="./assets/stop.png")
stop_btn = Button(root, image=stop_photo, command=stopMusic).pack()

volume = Scale(root, from_=0, to=100, orient=HORIZONTAL, command=setVolume)
volume.set(50)
mixer.music.set_volume(0.5)
volume.pack()

root.mainloop()