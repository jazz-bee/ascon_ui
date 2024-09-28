from view.main_section import MainSectionFrame
from customtkinter import CTkLabel


class DecryptionSectionFrame(MainSectionFrame):
    def __init__(self, master):
        super().__init__(master)

        self.add_inputs_widgets()

    def add_inputs_widgets(self):

        # Title
        self.label_key = CTkLabel(
            self, text="Decryption parameters", font=("Arial", 18, "bold"))
        self.label_key.grid(row=0, column=0, columnspan=3,
                            padx=10, pady=(10, 0), sticky="w")

    # def _gather_decryption_parameters(self):
    #     return {
    #         "key": self.key,
    #         "nonce": self.nonce,
    #         "associated_data": self.entry_ad.get().encode(),
    #         "ciphertext": self.ciphertext,
    #         "variant": self.optionmenu_variant.get()
    #     }
