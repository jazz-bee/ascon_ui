
from view.main_section import MainSectionFrame
from customtkinter import CTkFrame, CTkTabview, CTkEntry, CTkLabel, CTkTextbox, CTkOptionMenu, CTkButton, CTk


class EncryptionSectionFrame(MainSectionFrame):
    def __init__(self, master):
        super().__init__(master)
        self.add_inputs_widgets()

    def add_inputs_widgets(self):

        # Title
        self.label_key = CTkLabel(
            self.inputs_tab, text="Encryption parameters", font=("Arial", 18, "bold"))
        self.label_key.grid(row=0, column=0, columnspan=3,
                            padx=10, pady=(10, 0), sticky="w")

        # Variant
        self.label_pt = CTkLabel(
            self.inputs_tab, text="Variant:", font=("Arial", 12, "bold"))
        self.label_pt.grid(row=1, column=0, columnspan=2,
                           padx=10, pady=(10, 0), sticky="w")
        self.optionmenu_variant = CTkOptionMenu(self.inputs_tab,
                                                values=["Ascon-128", "Ascon-128a", "Ascon-80pq"])
        self.optionmenu_variant.grid(row=2, column=0,
                                     padx=10, pady=(0, 10), sticky="ew")

        # Key
        self.label_key = CTkLabel(
            self.inputs_tab, text="Key:", font=("Arial", 12, "bold"))
        self.label_key.grid(row=3, column=0, columnspan=2,
                            padx=10, pady=(10, 0), sticky="w")
        self.entry_key = CTkEntry(
            self.inputs_tab, placeholder_text="Required")
        self.entry_key.grid(row=4, column=0, columnspan=2,
                            padx=10, pady=(0, 10), sticky="ew")

        # Nonce
        self.label_nonce = CTkLabel(
            self.inputs_tab, text="Nonce:", font=("Arial", 12, "bold"))
        self.label_nonce.grid(row=5, column=0, columnspan=2,
                              padx=10, pady=(10, 0), sticky="w")
        self.entry_nonce = CTkEntry(
            self.inputs_tab, placeholder_text="Required")
        self.entry_nonce.grid(row=6, column=0, columnspan=2,
                              padx=10, pady=(0, 10), sticky="ew")

        # Plaintext
        self.label_pt = CTkLabel(
            self.inputs_tab, text="Plaintext:", font=("Arial", 12, "bold"))
        self.label_pt.grid(row=7, column=0, columnspan=2,
                           padx=10, pady=(10, 0), sticky="w")
        self.entry_pt = CTkEntry(
            self.inputs_tab, placeholder_text="Optional")
        self.entry_pt.grid(row=8, column=0, columnspan=2,
                           padx=10, pady=(0, 10), sticky="ew")

        # Associated data
        self.label_pt = CTkLabel(
            self.inputs_tab, text="Associated data", font=("Arial", 12, "bold"))
        self.label_pt.grid(row=9, column=0, columnspan=2,
                           padx=10, pady=(10, 0), sticky="w")
        self.entry_ad = CTkEntry(
            self.inputs_tab, placeholder_text="Optional")
        self.entry_ad.grid(row=10, column=0, columnspan=2,
                           padx=10, pady=(0, 10), sticky="ew")

        # Cipher button does not expand
        self.cipher_button = CTkButton(self.inputs_tab, text="Encrypt")
        self.cipher_button.grid(
            row=12, column=0, padx=10, pady=10, sticky="nw")
