from customtkinter import CTkEntry, CTkLabel, CTkOptionMenu, CTkButton
from tkinter import Entry
from view.main_section import MainSectionFrame


class EncryptionSectionFrame(MainSectionFrame):
    def __init__(self, master, encrypt_callback, generate_key_callback, generate_nonce_callback):
        super().__init__(master)

        # Initialization
        self.key = None
        self.nonce = None
        self.ciphertext = None
        self.received_plaintext = None

        self.encrypt_callback = encrypt_callback
        self.generate_key_callback = generate_key_callback
        self.generate_nonce_callback = generate_nonce_callback

        # Delay widget creation to ensure main window has loaded fully,
        # Prevents rendering issues with CTkEntry
        self.after(50, self.add_inputs_widgets)

    def add_inputs_widgets(self):

        # Title
        self.label_key = CTkLabel(
            self, text="Encryption parameters", font=("Arial", 18, "bold"))
        self.label_key.grid(row=0, column=0, columnspan=3,
                            padx=10, pady=(10, 0), sticky="w")

        # Variant
        self.label_pt = CTkLabel(
            self, text="Variant:", font=("Arial", 12, "bold"))
        self.label_pt.grid(row=1, column=0, columnspan=2,
                           padx=10, pady=(10, 0), sticky="w")
        self.optionmenu_variant = CTkOptionMenu(self,
                                                values=["Ascon-128", "Ascon-128a", "Ascon-80pq"])
        self.optionmenu_variant.grid(row=2, column=0,
                                     padx=10, pady=(0, 10), sticky="ew")

        # Key
        self.label_key = CTkLabel(
            self, text="Key:", font=("Arial", 12, "bold"))
        self.label_key.grid(row=3, column=0, columnspan=2,
                            padx=10, pady=(10, 0), sticky="w")

        self.entry_key = CTkEntry(
            self, placeholder_text="Required")
        self.entry_key.grid(row=4, column=0, columnspan=2,
                            padx=10, pady=(0, 10), sticky="ew")

        # Key random button
        self.key_button = CTkButton(
            self, text="Key", command=self.handle_key_button
        )
        self.key_button.grid(row=4, column=3, padx=10, pady=(0, 10))

        # Nonce
        self.label_nonce = CTkLabel(
            self, text="Nonce:", font=("Arial", 12, "bold"))
        self.label_nonce.grid(row=5, column=0, columnspan=2,
                              padx=10, pady=(10, 0), sticky="w")
        self.entry_nonce = CTkEntry(
            self, placeholder_text="Required")
        self.entry_nonce.grid(row=6, column=0, columnspan=2,
                              padx=10, pady=(0, 10), sticky="ew")

        # Nonce random button
        self.nonce_button = CTkButton(
            self, text="Nonce", command=self.handle_nonce_button
        )
        self.nonce_button.grid(row=6, column=3, padx=10, pady=(0, 10))

        # Plaintext
        self.label_pt = CTkLabel(
            self, text="Plaintext:", font=("Arial", 12, "bold"))
        self.label_pt.grid(row=7, column=0, columnspan=2,
                           padx=10, pady=(10, 0), sticky="w")
        self.entry_pt = CTkEntry(
            self, placeholder_text="Optional")
        self.entry_pt.grid(row=8, column=0, columnspan=2,
                           padx=10, pady=(0, 10), sticky="ew")

        # Associated data
        self.label_ad = CTkLabel(
            self, text="Associated data", font=("Arial", 12, "bold"))
        self.label_ad.grid(row=9, column=0, columnspan=2,
                           padx=10, pady=(10, 0), sticky="w")
        self.entry_ad = CTkEntry(
            self, placeholder_text="Optional")
        self.entry_ad.grid(row=10, column=0, columnspan=2,
                           padx=10, pady=(0, 10), sticky="ew")

        # Encrypt button does not expand
        self.cipher_button = CTkButton(
            self, text="Encrypt", command=self._on_encrypt_click)
        self.cipher_button.grid(
            row=12, column=0, padx=10, pady=10, sticky="nw")

    def _on_encrypt_click(self):
        params = self._gather_encryption_parameters()
        self.encrypt_callback(params)

    def _gather_encryption_parameters(self):
        # Create a dict with the input parameters
        try:
            # Convert hexa to bytes
            key = bytes.fromhex(self.entry_key.get())
            nonce = bytes.fromhex(self.entry_nonce.get())
        except ValueError:
            # Handle error if user types a key that is not a valid hexa
            raise ValueError("Invalid hexadecimal key/nonce format")

        return {
            "key": key,
            "nonce": nonce,
            "plaintext": self.entry_pt.get().encode(),  # encode string to bytes object
            "associated_data": self.entry_ad.get().encode(),
            "variant": self.optionmenu_variant.get(),
        }

    def handle_key_button(self):
        variant = self.optionmenu_variant.get()
        random_key = self.generate_key_callback(variant)
        self.entry_key.delete(0, 'end')
        self.entry_key.insert(0, random_key.hex())

    def handle_nonce_button(self):
        random_nonce = self.generate_nonce_callback()
        self.entry_nonce.delete(0, 'end')
        self.entry_nonce.insert(0, random_nonce.hex())
