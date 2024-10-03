from view.main_section import MainSectionFrame
from customtkinter import CTkLabel, CTkEntry, CTkOptionMenu, CTkButton


class DecryptionSectionFrame(MainSectionFrame):
    def __init__(self, master):
        super().__init__(master)

        # self.add_inputs_widgets()
        self.after(50, self.add_inputs_widgets)

    def add_inputs_widgets(self):

        # Title
        self.label_key = CTkLabel(
            self, text="Decryption parameters", font=("Arial", 18, "bold"))
        self.label_key.grid(row=0, column=0, columnspan=3,
                            padx=10, pady=(10, 0), sticky="w")

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
            self, placeholder_text="Required")
        self.key_entry.grid(row=4, column=0, columnspan=2,
                            padx=10, pady=(0, 10), sticky="ew")

        # Nonce
        self.nonce_label = CTkLabel(
            self, text="Nonce:", font=("Arial", 12, "bold"))
        self.nonce_label.grid(row=5, column=0, columnspan=2,
                              padx=10, pady=(10, 0), sticky="w")
        self.nonce_entry = CTkEntry(
            self, placeholder_text="Required")
        self.nonce_entry.grid(row=6, column=0, columnspan=2,
                              padx=10, pady=(0, 10), sticky="ew")

        # Associated data
        self.ciphertext_label = CTkLabel(
            self, text="Associated data", font=("Arial", 12, "bold"))
        self.ciphertext_label.grid(row=7, column=0, columnspan=2,
                                   padx=10, pady=(10, 0), sticky="w")
        self.ciphertext_entry = CTkEntry(
            self, placeholder_text="Optional")
        self.ciphertext_entry.grid(row=8, column=0, columnspan=2,
                                   padx=10, pady=(0, 10), sticky="ew")

        # Ciphertext
        self.ciphertext_label = CTkLabel(
            self, text="Ciphertext", font=("Arial", 12, "bold"))
        self.ciphertext_label.grid(row=9, column=0, columnspan=2,
                                   padx=10, pady=(10, 0), sticky="w")
        self.ciphertext_entry = CTkEntry(
            self, placeholder_text="Optional")
        self.ciphertext_entry.grid(row=10, column=0, columnspan=2,
                                   padx=10, pady=(0, 10), sticky="ew")

        # Tag
        self.tag_label = CTkLabel(
            self, text="Tag", font=("Arial", 12, "bold"))
        self.tag_label.grid(row=11, column=0, columnspan=2,
                            padx=10, pady=(10, 0), sticky="w")
        self.ad_entry = CTkEntry(
            self, placeholder_text="Optional")
        self.ad_entry.grid(row=12, column=0, columnspan=2,
                           padx=10, pady=(0, 10), sticky="ew")

        self.grid_rowconfigure(13, weight=1)

        # Decrypt button
        self.decrypt_button = CTkButton(
            self, text="Decrypt", command=self._on_decrypt_click)
        self.decrypt_button.grid(
            row=14, column=0, padx=10, pady=10, sticky="nw")

    # def _gather_decryption_parameters(self):
    #     return {
    #         "key": self.key,
    #         "nonce": self.nonce,
    #         "associated_data": self.entry_ad.get().encode(),
    #         "ciphertext": self.ciphertext,
    #         "variant": self.optionmenu_variant.get()
    #     }

    def _on_decrypt_click(self):
        pass
