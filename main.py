from tkinter import *
from tkinter import messagebox
import base64
import os

def main_screen():
    # Variables Globales
    global screen
    global code
    global text

    screen = Tk()
    screen.geometry("375x398")

    image_icon = PhotoImage(file="./images/keys.png")
    screen.iconphoto(False, image_icon)
    screen.title("Secret Message App")

    # Funciones
    def reset():
        code.set("")
        text.delete(1.0, END)

    def encrypt():
        password = code.get()

        if password=="1234":
            screen_encrypt = Toplevel(screen)
            screen_encrypt.title("Encripcion Completada !")
            screen_encrypt.geometry("400x200")
            screen_encrypt.configure(bg="#ed3833")

            message = text.get(1.0, END)
            encode_message = message.encode("ascii")
            base64_bytes = base64.b64encode(encode_message)
            encrypt = base64_bytes.decode("ascii")

            Label(
                screen_encrypt, 
                text="ENCRIPTADO", 
                font="arial", 
                fg="#ed3833"
            ).place(x=10, y=0)

            text_encrypt = Text(
                font="Roboto 10",
                bg="white", 
                relief=GROOVE,
                wrap=WORD, 
                bd=0    
            )
            text_encrypt.place(x=10, y=40, width=380, height=150)
            text_encrypt.insert(END, encrypt)

    def decrypt():
        print("")

    # Texto
    Label(
        text="Ingrese el texto a encriptar/desencriptar:", 
        fg="black", 
        font=("calibri", 13)
    ).place(x=10, y=10)

    text = Text(font="Roboto 14", bg="white", relief=GROOVE, wrap=WORD, bd=0)
    text.place(x=10, y=50, width=355, height=100)

    Label(
        text="Ingrese la clave(key):", 
        fg="black", 
        font=("calibri", 13)
    ).place(x=10, y=170)

    code = StringVar()
    Entry(
        textvariable=code, 
        width=19, bd=0, 
        font=("arial", 13), 
        show="*"
    ).place(x=10, y=200)

    # Botones
    Button(
        text="ENCRIPTAR", 
        height="2", width=23, 
        bg="#ed3833", 
        fg="white", 
        bd=0,
        command=encrypt
    ).place(x=10, y=250)

    Button(
        text="DESENCRIPTAR", 
        height="2", width=23, 
        bg="#00bd56", 
        fg="white", 
        bd=0,
        command=decrypt
    ).place(x=200, y=250)

    Button(
        text="LIMPIAR", 
        height="2", width=50, 
        bg="#1089ff", 
        fg="white", 
        bd=0,
        command=reset
    ).place(x=10, y=300)

    screen.mainloop()

main_screen()