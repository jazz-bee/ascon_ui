import customtkinter as ct
from UI.textbox import Textbox
from cipher import AsconCipher


class AppWindow(ct.CTk):
    def __init__(self):
        super().__init__()

        self.ascon_cipher = AsconCipher()

        # Config
        self.title("Criptografia - ASCON App")
        self.window_config()

        # Sidebar Frame
        self.sidebar_frame = ct.CTkFrame(
            master=self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=5, sticky="nsew")
        self.logo_label = ct.CTkLabel(
            self.sidebar_frame, text="ASCON", font=ct.CTkFont(size=30, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.demo_button = ct.CTkButton(
            self.sidebar_frame, text="Demo", command=self.mostrar_demo).grid(row=1, column=0, padx=20, pady=10)

        self.aead_button = ct.CTkButton(
            self.sidebar_frame, text="AEAD", command=self.mostrar_aead).grid(row=2, column=0, padx=20, pady=10)

        self.restart_button = ct.CTkButton(
            self.sidebar_frame, text="Reiniciar", command=self.restart_textbox).grid(row=3, column=0, padx=20, pady=10)

        # Textbox
        self.results_textbox = Textbox(self)
        self.results_textbox.grid(row=0, column=1,  padx=20,
                                  pady=20, sticky="nsew")
        self.results_textbox.restart()

        # input frame
        self.input_frame = ct.CTkFrame(self, corner_radius=0)
        self.input_frame.grid(row=1, column=1, rowspan=5, sticky="nsew")
        self.input_frame.grid_rowconfigure(4, weight=1)
        self.input_frame.grid_columnconfigure(1, weight=1)

        # Entry plaintext
        self.entry_pt = ct.CTkEntry(
            self.input_frame, placeholder_text="Texto plano")
        self.entry_pt.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

        # Entry associated data
        self.entry_ad = ct.CTkEntry(
            self.input_frame, placeholder_text="Datos asociados")
        self.entry_ad.grid(row=3, column=1, padx=20, pady=20, sticky="nsew")

        # Botones Cifrar y Descifrar
        self.encrypt_button = ct.CTkButton(
            master=self, text="Cifrar", command=self.button_function_encrypt)
        self.encrypt_button.grid(
            row=2, column=2, padx=20, pady=20, sticky="ew")

        self.decrypt_button = ct.CTkButton(
            master=self, text="Descifrar", command=self.button_function_decrypt)
        self.decrypt_button.grid(
            row=3, column=2, padx=20, pady=20, sticky="ew")

        # Tab
        self.tabview = ct.CTkTabview(self, width=250)
        self.tabview.grid(row=0, column=2, rowspan=2, padx=(
            20, 0), pady=(20, 0), sticky="nsew")
        self.tabview.add("Entradas")
        self.tabview.tab("Entradas").grid_columnconfigure(
            0, weight=1)

        # Seleccionar variante
        self.optionmenu_variant = ct.CTkOptionMenu(self.tabview.tab("Entradas"),
                                                   values=["Ascon-128", "Ascon-128a", "Ascon-80pq"])
        self.optionmenu_variant.grid(row=0, column=0, padx=20, pady=(20, 10))
        # Generar random key
        self.buttonkey = ct.CTkButton(
            self.tabview.tab("Entradas"), text="Key", command=self.button_function_key
        )
        self.buttonkey.grid(row=1, column=0, padx=20, pady=20, sticky="ew")
        # Generar random nonce
        self.buttonnonce = ct.CTkButton(
            self.tabview.tab("Entradas"), text="Nonce", command=self.button_function_nonce
        )
        self.buttonnonce.grid(row=2, column=0, padx=20, pady=20, sticky="ew")

    # Methods

    def window_config(self):
        self.geometry(f"{1100}x{580}")
        self.minsize(1100, 580)

        # Set grid
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Set appearance and theme color
        ct.set_appearance_mode("light")  # Modes: system (default), light, dark
        ct.set_default_color_theme("dark-blue")

    def encrypt(self):
        try:

            variant = self.optionmenu_variant.get()

            key = self.key
            nonce = self.nonce
            plaintext = self.entry_pt.get().encode()  # encode string to bytes object
            associateddata = self.entry_ad.get().encode()

            self.ciphertext, execution_time = self.ascon_cipher.encrypt(
                key, nonce, associateddata, plaintext, variant)

            self.results_textbox.add_title(f"CIFRADO: {variant}")

            self.result_print([("key", key),
                               ("nonce", nonce),
                               ("plaintext", plaintext),
                               ("ad", associateddata),
                               ("ciphertext", self.ciphertext[:-16]),
                               ("tag", self.ciphertext[-16:]),
                               ])
            self.entry_pt.delete(0, 'end')
            self.results_textbox.insert_line(f"Tamaño en bytes de salida: {
                len(self.ciphertext)}")
            self.results_textbox.insert_line(f"Tiempo en segundos: {
                execution_time}")
        except AttributeError:
            self.results_textbox.insert_line(
                "Error: faltan variables: key / nonce")

    def decrypt(self):
        try:

            variant = self.optionmenu_variant.get()
            key = self.key
            nonce = self.nonce

            associateddata = self.entry_ad.get().encode()
            receivedplaintext, execution_time = self.ascon_cipher.decrypt(
                key, nonce, associateddata, self.ciphertext, variant)

            self.results_textbox.add_title(f"DESCIFRADO: {variant}")

            if receivedplaintext == None:
                self.results_textbox.insert_line(
                    "No se pudo descifrar el mensaje")
            else:
                self.result_print([("received", receivedplaintext),])
                self.results_textbox.insert_line(f"Tiempo en segundos: {
                    execution_time}")
        except AttributeError:
            self.results_textbox.insert_line(
                "Error: falta el texto cifrado")

    def button_function_encrypt(self):
        self.encrypt()

    def button_function_decrypt(self):
        self.decrypt()

    def mostrar_demo(self):

        variant = "Ascon-128"
        keysize = 20 if variant == "Ascon-80pq" else 16
        key = ascon.get_random_bytes(keysize)
        nonce = ascon.get_random_bytes(16)
        plaintext = b"ascon"
        associateddata = b"ASCON"

        ciphertext = ascon.ascon_encrypt(
            key, nonce, associateddata, plaintext,  variant)
        receivedplaintext = ascon.ascon_decrypt(
            key, nonce, associateddata, ciphertext, variant)

        self.results_textbox.add_title(f"DEMO con {variant}")

        if receivedplaintext == None:
            self.results_textbox.insert_line("verification failed!")
        self.results_textbox.insert_line(f"El resultado de cifrar el texto plano= {
            plaintext.decode()}, con AD= {associateddata.decode()} ")
        self.results_textbox.insert_line(
            "Mostrando los valores de las variables en hexadecimal y su tamaño en bytes")
        self.result_print([("key", key),
                           ("nonce", nonce),
                           ("plaintext", plaintext),
                           ("ad", associateddata),
                           ("ciphertext", ciphertext[:-16]),
                           ("tag", ciphertext[-16:]),
                           ("received", receivedplaintext),
                           ])

    def result_print(self, data):
        maxlen = max([len(text) for (text, val) in data])
        for text, val in data:
            self.results_textbox.insert_line("{text}:{align} 0x{val} ({length} bytes)".format(text=text, align=(
                (maxlen - len(text)) * " "), val=ascon.bytes_to_hex(val), length=len(val)))

    def mostrar_aead(self):
        self.results_textbox.add_title("AEAD")

    def restart_textbox(self):
        self.results_textbox.restart()
        # restart variables #TODO

    def button_function_key(self):
        self.generate_random_key()
        key_in_hex = ascon.bytes_to_hex(self.key)
        self.results_textbox.insert_line(f"Key generado:  0x{key_in_hex}")

    def generate_random_key(self):
        variant = self.optionmenu_variant.get()
        keysize = 20 if variant == "Ascon-80pq" else 16
        self.key = ascon.get_random_bytes(keysize)  # TODO cambiar self.key

    def button_function_nonce(self):
        self.generate_random_nonce()
        nonce_in_hex = ascon.bytes_to_hex(self.nonce)
        self.results_textbox.insert_line(f"Nonce generado:  0x{nonce_in_hex}")

    def generate_random_nonce(self):
        self.nonce = ascon.get_random_bytes(16)  # zero_bytes(16)

    def button_function(self):
        self.encrypt()
