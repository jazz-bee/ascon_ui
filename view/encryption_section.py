from customtkinter import CTkEntry, CTkLabel, CTkOptionMenu, CTkButton, CTkSwitch, CTkFont, CTkComboBox
from view.main_section import MainSectionFrame


class EncryptionSectionFrame(MainSectionFrame):
    def __init__(self, master, encrypt_callback, generate_key_callback, generate_nonce_callback):
        super().__init__(master)

        self.encrypt_callback = encrypt_callback
        self.generate_key_callback = generate_key_callback
        self.generate_nonce_callback = generate_nonce_callback

        # Delay widget creation to ensure main window has loaded fully,
        # Prevents rendering issues with CTkEntry
        self.after(50, self.add_inputs_widgets)

    def add_inputs_widgets(self):
        # Title
        self.title_label = CTkLabel(
            self, text="Encryption parameters",  font=("Arial", 18, "bold"))
        self.title_label.grid(row=0, column=0, columnspan=3,
                              padx=10, pady=(20, 0), sticky="w")

        # Variant
        self.variant_label = CTkLabel(
            self, text="Variant:", font=("Arial", 12, "bold"))
        self.variant_label.grid(row=1, column=0, columnspan=2,
                                padx=10, pady=(10, 0), sticky="w")

        # self.optionmenu_variant = CTkComboBox(self,
        #                                       values=["Ascon-128", "Ascon-128a", "Ascon-80pq"])
        self.optionmenu_variant = CTkOptionMenu(self,
                                                values=["Ascon-128", "Ascon-128a", "Ascon-80pq"])
        self.optionmenu_variant.grid(row=2, column=0,
                                     padx=10, pady=(0, 10), sticky="ew")

        # Debug switch
        self.debug_switch = CTkSwitch(
            self, text="Debug Mode")
        self.debug_switch.grid(row=2, column=3,
                               padx=10, pady=(0, 10))

        # Key
        self.key_label = CTkLabel(
            self, text="Key:", font=("Arial", 12, "bold"))
        self.key_label.grid(row=3, column=0, columnspan=2,
                            padx=10, pady=(10, 0), sticky="w")

        self.key_entry = CTkEntry(
            self, placeholder_text="Required (hex)")
        self.key_entry.grid(row=4, column=0, columnspan=2,
                            padx=10, pady=(0, 10), sticky="ew")

        # Key random button
        self.key_button = CTkButton(
            self, text="Generate Key", command=self._handle_key_button,
            fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE")
        )
        self.key_button.grid(row=4, column=3, padx=10, pady=(0, 10))

        # Nonce
        self.nonce_label = CTkLabel(
            self, text="Nonce:", font=("Arial", 12, "bold"))
        self.nonce_label.grid(row=5, column=0, columnspan=2,
                              padx=10, pady=(10, 0), sticky="w")
        self.nonce_entry = CTkEntry(
            self, placeholder_text="Required (hex)")
        self.nonce_entry.grid(row=6, column=0, columnspan=2,
                              padx=10, pady=(0, 10), sticky="ew")

        # Nonce random button
        self.nonce_button = CTkButton(
            self, text="Generate Nonce", command=self._handle_nonce_button, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE")
        )
        self.nonce_button.grid(row=6, column=3, padx=10, pady=(0, 10))

        # Plaintext
        self.plaintext_label = CTkLabel(
            self, text="Plaintext:", font=("Arial", 12, "bold"))
        self.plaintext_label.grid(row=7, column=0, columnspan=2,
                                  padx=10, pady=(10, 0), sticky="w")
        self.plaintext_entry = CTkEntry(
            self, placeholder_text="Required (text)")
        self.plaintext_entry.grid(row=8, column=0, columnspan=2,
                                  padx=10, pady=(0, 10), sticky="ew")

        # Associated data
        self.ad_label = CTkLabel(
            self, text="Associated data:", font=("Arial", 12, "bold"))
        self.ad_label.grid(row=9, column=0, columnspan=2,
                           padx=10, pady=(10, 0), sticky="w")
        self.ad_entry = CTkEntry(
            self, placeholder_text="Optional (text)")
        self.ad_entry.grid(row=10, column=0, columnspan=2,
                           padx=10, pady=(0, 10), sticky="ew")

        self.grid_rowconfigure(11, weight=1)  # expands

        # Encrypt button
        self.encrypt_button = CTkButton(
            self, text="Encrypt",   command=self._handle_encrypt_button
        )

        self.encrypt_button.grid(
            row=12, column=0, padx=10, pady=10, sticky="nw")

        self.error_label = CTkLabel(self, text="", text_color="red")
        self.error_label.grid(row=12, column=1, padx=10, pady=5, sticky="w")

    def _handle_encrypt_button(self):
        try:
            params = self._gather_encryption_parameters()
            self.error_label.configure(text="")
            self.encrypt_callback(params)
        except ValueError as e:
            self.error_label.configure(text=str(e))

    def _gather_encryption_parameters(self):
        # Create a dict with the input parameters
        try:
            # Convert hexa to bytes
            key = bytes.fromhex(self.key_entry.get())
            nonce = bytes.fromhex(self.nonce_entry.get())
        except ValueError as e:
            # Handle error if user types a key that is not a valid hexa
            raise ValueError("Invalid hexadecimal key/nonce format") from e

        return {
            "key": key,
            "nonce": nonce,
            "plaintext": self.plaintext_entry.get().encode(),  # encode string to bytes object
            "associated_data": self.ad_entry.get().encode(),
            "variant": self.optionmenu_variant.get(),
        }

    def _handle_key_button(self):
        variant = self.optionmenu_variant.get()
        random_key = self.generate_key_callback(variant)
        self.key_entry.delete(0, 'end')
        self.key_entry.insert(0, random_key.hex())

    def _handle_nonce_button(self):
        random_nonce = self.generate_nonce_callback()
        self.nonce_entry.delete(0, 'end')
        self.nonce_entry.insert(0, random_nonce.hex())

    def get_debug_switch_value(self):
        return self.debug_switch.get()
