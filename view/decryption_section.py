from view.main_section import MainSectionFrame
from customtkinter import CTkLabel, CTkEntry, CTkOptionMenu, CTkButton


class DecryptionSectionFrame(MainSectionFrame):
    def __init__(self, master, decrypt_callback, autocomplete_callback):
        super().__init__(master)

        self.decrypt_callback = decrypt_callback
        self.autocomplete_callback = autocomplete_callback

        self.after(50, self.add_inputs_widgets)

    def add_inputs_widgets(self):
        # Title
        self.label_key = CTkLabel(
            self, text="Decryption parameters", font=("Arial", 18, "bold"))
        self.label_key.grid(row=0, column=0, columnspan=3,
                            padx=10, pady=(20, 0), sticky="w")

        # Variant
        self.variant_label = CTkLabel(
            self, text="Variant:", font=("Arial", 12, "bold"))
        self.variant_label.grid(row=1, column=0, columnspan=2,
                                padx=10, pady=(10, 0), sticky="w")
        self.optionmenu_variant = CTkOptionMenu(self,
                                                values=["Ascon-128", "Ascon-128a", "Ascon-80pq"])
        self.optionmenu_variant.grid(row=2, column=0,
                                     padx=10, pady=(0, 10), sticky="ew")

        # Key
        self.key_label = CTkLabel(
            self, text="Key:", font=("Arial", 12, "bold"))
        self.key_label.grid(row=3, column=0, columnspan=2,
                            padx=10, pady=(10, 0), sticky="w")

        self.key_entry = CTkEntry(
            self, placeholder_text="Required (hex)")
        self.key_entry.grid(row=4, column=0, columnspan=2,
                            padx=10, pady=(0, 10), sticky="ew")

        # Nonce
        self.nonce_label = CTkLabel(
            self, text="Nonce:", font=("Arial", 12, "bold"))
        self.nonce_label.grid(row=5, column=0, columnspan=2,
                              padx=10, pady=(10, 0), sticky="w")
        self.nonce_entry = CTkEntry(
            self, placeholder_text="Required (hex)")
        self.nonce_entry.grid(row=6, column=0, columnspan=2,
                              padx=10, pady=(0, 10), sticky="ew")

        # Associated data
        self.ad_label = CTkLabel(
            self, text="Associated data:", font=("Arial", 12, "bold"))
        self.ad_label.grid(row=7, column=0, columnspan=2,
                           padx=10, pady=(10, 0), sticky="w")
        self.ad_entry = CTkEntry(
            self, placeholder_text="Optional (hex)")
        self.ad_entry.grid(row=8, column=0, columnspan=2,
                           padx=10, pady=(0, 10), sticky="ew")

        # Ciphertext
        self.ciphertext_label = CTkLabel(
            self, text="Ciphertext:", font=("Arial", 12, "bold"))
        self.ciphertext_label.grid(row=9, column=0, columnspan=2,
                                   padx=10, pady=(10, 0), sticky="w")
        self.ciphertext_entry = CTkEntry(
            self, placeholder_text="Required (hex)")
        self.ciphertext_entry.grid(row=10, column=0, columnspan=2,
                                   padx=10, pady=(0, 10), sticky="ew")

        # Tag
        self.tag_label = CTkLabel(
            self, text="Tag:", font=("Arial", 12, "bold"))
        self.tag_label.grid(row=11, column=0, columnspan=2,
                            padx=10, pady=(10, 0), sticky="w")
        self.tag_entry = CTkEntry(
            self, placeholder_text="Required (hex)")
        self.tag_entry.grid(row=12, column=0, columnspan=2,
                            padx=10, pady=(0, 10), sticky="ew")

        self.grid_rowconfigure(13, weight=1)  # expands

        # Decrypt button
        self.decrypt_button = CTkButton(
            self, text="Decrypt", command=self._handle_decrypt_button)
        self.decrypt_button.grid(
            row=14, column=0, padx=10, pady=10, sticky="nw")

        self.error_label = CTkLabel(self, text="", text_color="red")
        self.error_label.grid(row=14, column=1, padx=10, pady=5, sticky="w")

        # Autocomplete button
        self.autocomplete_button = CTkButton(
            self, text="Autocomplete", fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), command=self._autocomplete_fields)
        self.autocomplete_button.grid(
            row=4, column=3, padx=10, pady=(0, 10))

    def _handle_decrypt_button(self):
        try:
            params = self._gather_decryption_parameters()
            self.error_label.configure(text="")
            self.decrypt_callback(params)
        except ValueError as e:
            self.error_label.configure(text=str(e))

    def _gather_decryption_parameters(self):
        # Create a dict with the parameters in bytes
        try:
            # Convert hexa to bytes
            key = bytes.fromhex(self.key_entry.get())
            nonce = bytes.fromhex(self.nonce_entry.get())
            ciphertext = bytes.fromhex(self.ciphertext_entry.get())
            tag = bytes.fromhex(self.tag_entry.get())
        except ValueError as e:
            # Handle error if user types a key that is not a valid hexa
            raise ValueError(
                "Invalid hexadecimal format") from e

        return {
            "key": key,
            "nonce": nonce,
            "ciphertext": ciphertext+tag,
            "associated_data": bytes.fromhex(self.ad_entry.get()),
            "variant": self.optionmenu_variant.get(),
        }

    def _autocomplete_fields(self):
        encryption_result = self.autocomplete_callback()

        if encryption_result:
            fields = {
                self.ciphertext_entry: encryption_result["ciphertext"].hex(),
                self.tag_entry: encryption_result["tag"].hex(),
                self.key_entry: encryption_result["params"]["key"].hex(),
                self.nonce_entry: encryption_result["params"]["nonce"].hex(),
                self.ad_entry: encryption_result["params"]["associated_data"].hex(),
            }
            for entry, value in fields.items():
                entry.delete(0, 'end')
                entry.insert(0, value)
        else:
            print("No encryption results available")  # TODO
