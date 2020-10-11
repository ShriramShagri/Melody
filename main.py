from tkinter import *
from pygame import mixer

root = Tk()

mixer.init()

root.geometry('600x300')
root.title("Melody")
root.iconbitmap(r'./assets/favicon.ico')

text = Label(root, text="Let's make something nice").pack()

photo = PhotoImage(file="./assets/play.png")
# labelphoto = Label(root,image=photo).pack()

def playMusic():
    mixer.music.load('./assets/Testmusic/AlanWalker.mp3')
    mixer.music.play()

play_btn = Button(root, image=photo, command=playMusic).pack()



root.mainloop()