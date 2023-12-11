import customtkinter as ct

# Setear apariencia y colores
ct.set_appearance_mode("dark")  # Modos: system (default), light, dark
ct.set_default_color_theme("green")  # Temas: blue (default), dark-blue, green

class AppWindow(ct.CTk): # hereda de Ctk, AppWindow es una customtkinter window
    def __init__(self):
        super().__init__()

        # config grid layout: splits the window into columns and rows
        self.grid_columnconfigure(0, weight=1)

        self.title('App Criptografia: ASCON')
        self.geometry("800x480")

        #Widgets
        self.entry_var = ct.StringVar()
        self.entry = ct.CTkEntry(master=self, placeholder_text="Ingrese un numero",textvariable=self.entry_var)
        self.entry.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        self.button=ct.CTkButton(master=self, text="Cifrar", command=self.button_function)
        self.button.grid(row=0, column=1, padx=20, pady=20, sticky="ew")

        self.check_var = ct.StringVar(value="on")
        self.checkbox = ct.CTkCheckBox(master=self, text="Mostrar resultado", command=self.checkbox_event,
                                     variable=self.check_var, onvalue="on", offvalue="off")
        self.checkbox.grid(row=0, column=2, padx=20, pady=20, sticky="ew")

        self.button2=ct.CTkButton(master=self, text="Descifrar", command=self.button_function)
        self.button2.grid(row=1, column=1, padx=20, pady=20, sticky="ew")

        self.textbox = ct.CTkTextbox(self,border_width=2)
        self.textbox.grid(row=2, column=0, padx=(20, 0), pady=(20, 0),sticky="nsew")
        self.textbox.insert("0.0", "Resultados\n")

    # Methods
    def encrypt(self):
        try:
            a = int(self.entry_var.get())
            b = 2
            c = a ^ b # apply XOR
            if self.check_var.get() == 'on':
                self.textbox.insert("0.0","Resultado de aplicar " +str(a)+" XOR "+str(b)+" es: "+str(c)+"\n")
        except ValueError: # XOR solo opera con int o bool
            self.textbox.insert("0.0","Error ingrese un INT \n")
            return None

    def button_function(self):
        print("button pressed") #debug
        self.encrypt()   
    
    def checkbox_event(self):
        print("checkbox toggled, current value:", self.check_var.get()) #debug
            
app = AppWindow()
app.mainloop()
