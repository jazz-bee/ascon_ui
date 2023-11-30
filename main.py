from tkinter import *
# from customtkinter import CTk,CTkButton
import customtkinter

#Setear apariencia y colores
customtkinter.set_appearance_mode("System")  # Modos: system (default), light, dark
customtkinter.set_default_color_theme("green")  # Temas: blue (default), dark-blue, green


app = customtkinter.CTk()  # create CTk window like you do with the Tk window

app.title('App Criptografia')
app.geometry("400x240")

#debug
def button_function(): 
    print("button pressed")

# Boton
button = customtkinter.CTkButton(master=app, text="CTkButton", command=button_function)
button.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

app.mainloop()