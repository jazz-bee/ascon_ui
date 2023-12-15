import customtkinter as ct

# Setear apariencia y colores
ct.set_appearance_mode("dark")  # Modos: system (default), light, dark
ct.set_default_color_theme("dark-blue")  # Temas: blue, dark-blue, green


class AppWindow(ct.CTk):  # hereda de Ctk, AppWindow es una customtkinter window
    def __init__(self):
        super().__init__()

        # Config
        self.title("Criptografia - ASCON App")
        self.geometry(f"{1100}x{580}")
        self.minsize(1100, 580)  # minimo para achicar ventana
        self.grid_columnconfigure(1, weight=1)
        # self.grid_rowconfigure((0, 1, 2), weight=1)

        # Sidebar Frame
        self.sidebar_frame = ct.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=5, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(3, weight=1)
        self.logo_label = ct.CTkLabel(
            self.sidebar_frame, text="ASCON", font=ct.CTkFont(size=30, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        # botones del sidebar
        self.sidebar_button_1 = ct.CTkButton(
            self.sidebar_frame, text="Demo", command=self.sidebar_button_event)
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = ct.CTkButton(
            self.sidebar_frame, text="AEAD", command=self.sidebar_button_event)
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)

        # Textbox
        self.textbox = ct.CTkTextbox(self, border_width=2)
        self.textbox.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")
        self.textbox.insert(
            "0.0", "Implementación de Ascon v1.2 - http://ascon.iaik.tugraz.at/\n")

        # Entry texto plano
        self.entry_var = ct.StringVar()
        self.entry = ct.CTkEntry(master=self, placeholder_text="Texto plano",
                                 textvariable=self.entry_var)
        self.entry.grid(row=2, column=1, padx=20, pady=20, sticky="nsew")

        # Entry asociated data
        self.entry_var2 = ct.StringVar()
        self.entry2 = ct.CTkEntry(master=self, placeholder_text="Data asociada",
                                  textvariable=self.entry_var2)
        self.entry2.grid(row=3, column=1, padx=20, pady=20, sticky="nsew")

#
        self.check_var = ct.StringVar(value="on")
        self.checkbox = ct.CTkCheckBox(master=self, text="Mostrar resultado", command=self.checkbox_event,
                                       variable=self.check_var, onvalue="on", offvalue="off")
        self.checkbox.grid(row=3, column=0, padx=20, pady=20, sticky="ew")

        self.button = ct.CTkButton(
            master=self, text="Cifrar", command=self.button_function)
        self.button.grid(row=2, column=2, padx=20, pady=20, sticky="ew")

        self.button2 = ct.CTkButton(
            master=self, text="Descifrar", command=self.button_function)
        self.button2.grid(row=3, column=2, padx=20, pady=20, sticky="ew")

    # Methods

    def encrypt(self):
        try:
            a = int(self.entry_var.get())
            b = 2
            c = a ^ b  # apply XOR
            if self.check_var.get() == 'on':
                self.textbox.insert(
                    "0.0", "Resultado de aplicar " + str(a)+" XOR "+str(b)+" es: "+str(c)+"\n")
        except ValueError:  # XOR solo opera con int o bool
            self.textbox.insert("0.0", "Error ingrese un INT \n")
            return None

    def button_function(self):
        print("button pressed")  # debug
        self.encrypt()

    def checkbox_event(self):
        print("checkbox toggled, current value:",
              self.check_var.get())  # debug

    def sidebar_button_event(self):
        print("sidebar_button click")  # debug


app = AppWindow()
app.mainloop()
