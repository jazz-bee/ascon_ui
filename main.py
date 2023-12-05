import customtkinter
# Setear apariencia y colores
customtkinter.set_appearance_mode("System")  # Modos: system (default), light, dark
customtkinter.set_default_color_theme("green")  # Temas: blue (default), dark-blue, green

class AppWindow(customtkinter.CTk): # hereda de Ctk, AppWindow es una customtkinter window
    def __init__(self):
        super().__init__()

        self.title('App Criptografia: ASCON')
        self.geometry("800x480")

        #Widgets
        self.button=customtkinter.CTkButton(master=self, text="CTkButton", command=self.button_function)
        self.button.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

    #methods
    def button_function(self):
        print("button pressed") #debug    
            
app = AppWindow()
app.mainloop()