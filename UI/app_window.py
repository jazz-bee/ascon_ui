import customtkinter as ct
from UI.textbox import Textbox
from UI.sidebar import SidebarFrame
from cipher import AsconCipher


class AppWindow(ct.CTk):
    def __init__(self):
        super().__init__()

        self.ascon_cipher = AsconCipher()
        self.key = 0
        self.ciphertext = None
        self.received_plaintext = None

        # Config
        self.title("Criptografia - ASCON App")
        self.window_config()

        # Sidebar Frame
        self.sidebar_frame = SidebarFrame(master=self,
                                          on_demo_click=self.handle_demo,
                                          on_aead_click=self.handle_aead,
                                          width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=5, sticky="nsew")

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
            master=self, text="Cifrar", command=self.handle_encrypt)
        self.encrypt_button.grid(
            row=2, column=2, padx=20, pady=20, sticky="ew")

        self.decrypt_button = ct.CTkButton(
            master=self, text="Descifrar", command=self.handle_decrypt)
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

    def gather_encryption_parameters(self):
        # create a dict with the input parameters
        return {
            "key": self.key,
            "nonce": self.nonce,
            "plaintext": self.entry_pt.get().encode(),  # encode string to bytes object
            "associated_data": self.entry_ad.get().encode(),
            "variant": self.optionmenu_variant.get(),
        }

    def display_results(self, params, ciphertext, execution_time):
        # Title depending on variant
        self.results_textbox.add_title(f"ENCRYPTION: {params['variant']}")

        # Print the input params and ascon output
        self.result_print([
            ("key", params['key']),
            ("nonce", params['nonce']),
            ("plaintext", params['plaintext']),
            ("associated data", params['associated_data']),
            # Exclude the tag from ciphertext
            ("ciphertext", ciphertext[:-16]),
            ("tag", ciphertext[-16:])  # Last 16 bytes are the tag
        ])

        # Show the size of the output and the execution time
        self.results_textbox.insert_line(
            f"Output size (bytes): {len(ciphertext)}")
        self.results_textbox.insert_line(
            f"Execution time (seconds): {execution_time}")

    def handle_encrypt(self):
        if not self.key or not self.nonce:
            self.results_textbox.insert_line(
                "Error: Key or nonce not generated.")
            return

        try:
            params = self.gather_encryption_parameters()

            self.ciphertext, execution_time = self.ascon_cipher.encrypt_and_measure_time(
                params['key'], params['nonce'], params['associated_data'], params['plaintext'], params['variant'])

            self.display_results(params, self.ciphertext, execution_time)
        except Exception as e:
            self.results_textbox.insert_line(f"Error during encryption: {e}")

    def handle_decrypt(self):
        # Gather parameters in a dictionary
        try:
            decrypt_params = {
                "key": self.key,
                "nonce": self.nonce,
                "associated_data": self.entry_ad.get().encode(),
                "ciphertext": self.ciphertext,
                "variant": self.optionmenu_variant.get()
            }
            if not hasattr(self, 'ciphertext'):
                raise AttributeError(
                    "Ciphertext is not available for decryption.")

            self.received_plaintext, execution_time = self.ascon_cipher.decrypt_and_measure_time(
                decrypt_params["key"],
                decrypt_params["nonce"],
                decrypt_params["associated_data"],
                decrypt_params["ciphertext"],
                decrypt_params["variant"]
            )

            self.display_decryption_results(decrypt_params,
                                            self.received_plaintext, execution_time)

        except AttributeError:
            self.results_textbox.insert_line(
                "Error: falta el texto cifrado")

    def display_decryption_results(self, params, received_plaintext, execution_time):
        self.results_textbox.add_title(
            f"DECRYPT: {params['variant']}")

        if received_plaintext is None:
            self.results_textbox.insert_line("It was not possible to decipher")
        else:
            self.result_print([("Received", self.received_plaintext),])
            self.results_textbox.insert_line(
                f"Received plaintext: {received_plaintext.decode()}")
            self.results_textbox.insert_line(
                f"Time taken: {execution_time:.6f} seconds")

    # Handlers for the sidebar button clicks
    def handle_demo(self):
        self.results_textbox.add_title("Demo")

    def handle_aead(self):
        self.results_textbox.add_title("AEAD")

    def result_print(self, data):
        maxlen = max([len(text) for (text, val) in data])
        for text, val in data:
            self.results_textbox.insert_line("{text}:{align} 0x{val} ({length} bytes)".format(text=text, align=(
                (maxlen - len(text)) * " "), val=self.ascon_cipher.bytes_to_hex(val), length=len(val)))

    def restart_textbox(self):
        self.results_textbox.restart()
        # restart variables #TODO

    def button_function_key(self):
        self.generate_random_key()
        key_in_hex = self.ascon_cipher.bytes_to_hex(self.key)
        self.results_textbox.insert_line(f"Key generado:  0x{key_in_hex}")

    def generate_random_key(self):
        variant = self.optionmenu_variant.get()
        keysize = 20 if variant == "Ascon-80pq" else 16
        self.key = self.ascon_cipher.get_random_key(
            keysize)  # TODO cambiar self.key

    def button_function_nonce(self):
        self.generate_random_nonce()
        nonce_in_hex = self.ascon_cipher.bytes_to_hex(self.nonce)
        self.results_textbox.insert_line(f"Nonce generado:  0x{nonce_in_hex}")

    def generate_random_nonce(self):
        self.nonce = self.ascon_cipher.get_random_nonce(16)  # zero_bytes(16)

    def button_function(self):
        self.encrypt()
