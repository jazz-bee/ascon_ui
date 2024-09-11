import customtkinter as ct
from UI.textbox import Textbox
from UI.sidebar import SidebarFrame
from controllers.ascon_controller import AsconController


class AppWindow(ct.CTk):
    def __init__(self):
        super().__init__()

        self.ascon_controller = AsconController()

        # initialize parameters
        self.key = None
        self.nonce = None
        self.ciphertext = None
        self.received_plaintext = None

        # Config
        self.title("Criptografia - ASCON App")
        self.window_config()

        # Sidebar Frame
        self.sidebar_frame = SidebarFrame(master=self,
                                          on_demo_click=self.handle_demo,
                                          on_aead_click=self.handle_aead)

        # Textbox
        self.results_textbox = Textbox(self)

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
            self.tabview.tab("Entradas"), text="Key", command=self.handle_key_button
        )
        self.buttonkey.grid(row=1, column=0, padx=20, pady=20, sticky="ew")
        # Generar random nonce
        self.buttonnonce = ct.CTkButton(
            self.tabview.tab("Entradas"), text="Nonce", command=self.handle_nonce_button
        )
        self.buttonnonce.grid(row=2, column=0, padx=20, pady=20, sticky="ew")

    # Methods

    def window_config(self):
        self.geometry(f"{1100}x{580}")
        self.minsize(1100, 580)

        # Set grid
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Set appearance and theme color
        ct.set_appearance_mode("light")  # Modes: system (default), light, dark
        ct.set_default_color_theme("dark-blue")

    def handle_encrypt(self):
        # try:
        params = self._gather_encryption_parameters()
        self.ciphertext, execution_time = self.ascon_controller.encrypt_and_measure_time(
            params)
        self.display_encryption_results(
            params, self.ciphertext, execution_time)
        # except Exception as e:
        #     print(f"Error during encryption - {e}")
        #     # self.results_textbox.insert_line(f"Error during encryption - {e}")

    def handle_decrypt(self):
        try:
            decrypt_params = self._gather_decryption_parameters()

            self.received_plaintext, execution_time = self.ascon_controller.decrypt_and_measure_time(
                decrypt_params)

            self.display_decryption_results(
                decrypt_params, self.received_plaintext, execution_time)

        except Exception as e:
            self.results_textbox.insert_line(f"Error during decryption -  {e}")

    def _gather_encryption_parameters(self):
        # create a dict with the input parameters
        return {
            "key": self.key,
            "nonce": self.nonce,
            "plaintext": self.entry_pt.get().encode(),  # encode string to bytes object
            "associated_data": self.entry_ad.get().encode(),
            "variant": self.optionmenu_variant.get(),
        }

    def _gather_decryption_parameters(self):
        return {
            "key": self.key,
            "nonce": self.nonce,
            "associated_data": self.entry_ad.get().encode(),
            "ciphertext": self.ciphertext,
            "variant": self.optionmenu_variant.get()
        }

    def display_encryption_results(self, params, ciphertext, execution_time):
        # Title depending on variant
        self.results_textbox.add_title(f"ENCRYPTION: {params['variant']}")

        # Print the input params and ascon output
        self._result_print([
            ("Key", params['key']),
            ("Nonce", params['nonce']),
            ("Plaintext", params['plaintext']),
            ("Associated data", params['associated_data']),
            # Exclude the tag from ciphertext
            ("Ciphertext", ciphertext[:-16]),
            ("Tag", ciphertext[-16:])  # Last 16 bytes are the tag
        ])

        # Show the size of the output and the execution time
        self.results_textbox.insert_line(
            f"Output size (bytes): {len(ciphertext)}")
        self.results_textbox.insert_line(
            f"Execution time (s): {execution_time}")

    def display_decryption_results(self, params, received_plaintext, execution_time):
        self.results_textbox.add_title(
            f"DECRYPT: {params['variant']}")

        if received_plaintext is None:
            self.results_textbox.insert_line("It was not possible to decipher")
        else:
            self._result_print([("Received", self.received_plaintext),])
            self.results_textbox.insert_line(
                f"Received plaintext: {received_plaintext.decode()}")
            self.results_textbox.insert_line(
                f"Execution time(s): {execution_time:.6f} ")

    # Handlers for the sidebar button clicks
    def handle_demo(self):
        self.results_textbox.add_title("Demo")

    def handle_aead(self):
        self.results_textbox.add_title("AEAD")

    def _result_print(self, data):
        maxlen = max([len(text) for (text, val) in data])
        for text, val in data:
            self.results_textbox.insert_line("{text}:{align} 0x{val} ({length} bytes)".format(text=text, align=(
                (maxlen - len(text)) * " "), val=self.ascon_controller.bytes_to_hex(val), length=len(val)))

    def handle_key_button(self):
        self._generate_random_key()
        key_in_hex = self.ascon_controller.bytes_to_hex(self.key)
        self.results_textbox.insert_line(f"Key generado:  0x{key_in_hex}")

    def _generate_random_key(self):
        variant = self.optionmenu_variant.get()
        keysize = 20 if variant == "Ascon-80pq" else 16
        self.key = self.ascon_controller.get_random_key(
            keysize)  # TODO cambiar self.key

    def handle_nonce_button(self):
        self._generate_random_nonce()
        nonce_in_hex = self.ascon_controller.bytes_to_hex(self.nonce)
        self.results_textbox.insert_line(f"Nonce generado:  0x{nonce_in_hex}")

    def _generate_random_nonce(self):
        self.nonce = self.ascon_controller.get_random_nonce(
            16)  # zero_bytes(16)
