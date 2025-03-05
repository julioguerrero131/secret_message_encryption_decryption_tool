from tkinter import *
from tkinter import messagebox
import base64
import os

def main_screen():
    screen = Tk()
    screen.geometry("375x398")

    image_icon = PhotoImage(file="./images/keys.png")
    screen.iconphoto(False, image_icon)
    screen.title("Secret Message App")

    Label(
        text="Ingrese el mensaje a encriptar/desencriptar:", 
        fg="black", 
        font=("calibri", 13)
    ).place(x=10, y=10)

    text = Text(font="Roboto 15", bg="white", relief=GROOVE, wrap=WORD, bd=0)
    text.place(x=10, y=50, width=355, height=100)

    screen.mainloop()

main_screen()