import customtkinter as ct
from algoritmos import ascon
import tkinter.font as TkFont

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
        self.grid_rowconfigure((0, 1), weight=1)

        # Sidebar Frame
        self.sidebar_frame = ct.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=5, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = ct.CTkLabel(
            self.sidebar_frame, text="ASCON", font=ct.CTkFont(size=30, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.sidebar_button_1 = ct.CTkButton(
            self.sidebar_frame, text="Demo", command=self.sidebar_button1_event)
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = ct.CTkButton(
            self.sidebar_frame, text="AEAD", command=self.sidebar_button2_event)
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.sidebar_button_3 = ct.CTkButton(
            self.sidebar_frame, text="Reiniciar", command=self.sidebar_button3_event)
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)

        # Textbox
        self.textbox = ct.CTkTextbox(
            self, border_width=2, font=ct.CTkFont(family="Courier New"))
        # use monospaced font (Courier New is available in  mac and windows)
        self.textbox.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")
        self.restart_textbox()

        # Entry texto plano
        self.entry_var = ct.StringVar()
        self.entry = ct.CTkEntry(master=self, placeholder_text="Texto plano",
                                 textvariable=self.entry_var)
        self.entry.grid(row=2, column=1, padx=20, pady=20, sticky="nsew")

        # Entry associated data
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

    def sidebar_button1_event(self):
        # Demo aead
        variant = "Ascon-128"
        keysize = 20 if variant == "Ascon-80pq" else 16
        key = ascon.get_random_bytes(keysize)  # zero_bytes(keysize)
        nonce = ascon.get_random_bytes(16)      # zero_bytes(16)

        associateddata = b"ASCON"
        plaintext = b"ascon"
        ciphertext = ascon.ascon_encrypt(
            key, nonce, associateddata, plaintext,  variant)
        receivedplaintext = ascon.ascon_decrypt(
            key, nonce, associateddata, ciphertext, variant)

        if receivedplaintext == None:
            print("verification failed!")

        print("=== demo con {variant} ===".format(
            variant=variant))  # debug
        self.demo_print([("key", key),
                         ("nonce", nonce),
                         ("plaintext", plaintext),
                         ("ad", associateddata),
                         ("ciphertext", ciphertext[:-16]),
                         ("tag", ciphertext[-16:]),
                         ("received", receivedplaintext),
                         ])

    def demo_print(self, data):
        maxlen = max([len(text) for (text, val) in data])
        self.update_textbox("=== Demo ===")
        for text, val in data:
            self.textbox.insert(
                "end", "{text}:{align} 0x{val} ({length} bytes)\n".format(text=text, align=(
                    (maxlen - len(text)) * " "), val=ascon.bytes_to_hex(val), length=len(val)))

    def sidebar_button2_event(self):
        print("sidebar_button click")  # debug

    def sidebar_button3_event(self):
        self.restart_textbox()

    def update_textbox(self, text):
        self.textbox.insert("end", "\n{text}\n".format(text=text))

    def restart_textbox(self):
        self.textbox.delete("0.0", "end")  # delete all text
        self.textbox.insert(
            "0.0", "Implementación de Ascon v1.2 - http://ascon.iaik.tugraz.at/ \n")


app = AppWindow()
app.mainloop()
