
from view.main_section import MainSectionFrame
from customtkinter import CTkFrame, CTkTabview, CTkEntry, CTkLabel, CTkTextbox, CTkOptionMenu, CTkButton, CTk
from view.textbox import Textbox


class EncryptionSectionFrame(MainSectionFrame):
    def __init__(self, master, encrypt_callback, generate_key_callback, generate_nonce_callback):
        super().__init__(master)

        # initialize parameters
        self.key = None
        self.nonce = None
        self.ciphertext = None
        self.received_plaintext = None

        self.encrypt_callback = encrypt_callback
        self.generate_key_callback = generate_key_callback
        self.generate_nonce_callback = generate_nonce_callback
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
            self.inputs_tab, placeholder_text="Required", state="disabled")
        self.entry_key.grid(row=4, column=0, columnspan=2,
                            padx=10, pady=(0, 10), sticky="ew")

        # Key random button
        self.key_button = CTkButton(
            self.inputs_tab, text="Key", command=self.handle_key_button
        )
        self.key_button.grid(row=4, column=3, padx=10, pady=(0, 10))

        # Nonce
        self.label_nonce = CTkLabel(
            self.inputs_tab, text="Nonce:", font=("Arial", 12, "bold"))
        self.label_nonce.grid(row=5, column=0, columnspan=2,
                              padx=10, pady=(10, 0), sticky="w")
        self.entry_nonce = CTkEntry(
            self.inputs_tab, placeholder_text="Required", state="disabled")
        self.entry_nonce.grid(row=6, column=0, columnspan=2,
                              padx=10, pady=(0, 10), sticky="ew")

        # Nonce random button
        self.nonce_button = CTkButton(
            self.inputs_tab, text="Nonce", command=self.handle_nonce_button
        )
        self.nonce_button.grid(row=6, column=3, padx=10, pady=(0, 10))

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
        self.label_ad = CTkLabel(
            self.inputs_tab, text="Associated data", font=("Arial", 12, "bold"))
        self.label_ad.grid(row=9, column=0, columnspan=2,
                           padx=10, pady=(10, 0), sticky="w")
        self.entry_ad = CTkEntry(
            self.inputs_tab, placeholder_text="Optional")
        self.entry_ad.grid(row=10, column=0, columnspan=2,
                           padx=10, pady=(0, 10), sticky="ew")

        # Encrypt button does not expand
        self.cipher_button = CTkButton(
            self.inputs_tab, text="Encrypt", command=self._on_encrypt_click)
        self.cipher_button.grid(
            row=12, column=0, padx=10, pady=10, sticky="nw")

    # def add_result_widgets(self):
    #     pass

    def _on_encrypt_click(self):
        params = self._gather_encryption_parameters()  # Collect parameters
        self.encrypt_callback(params)  # Pass the params to the callback

    # TODO metodos a reutilizar y borrar

    # def handle_encrypt(self):
    #     # try:
    #     params = self._gather_encryption_parameters()

    #     # self.ciphertext, execution_time = self.ascon_controller.encrypt_and_measure_time(
    #     #     params)
    #     self.app_window_callback(params)

    #     #     self.display_encryption_results(
    #     #         params, self.ciphertext, execution_time)
    #     # except Exception as e:
    #     #     self.results_textbox.insert_line(f"Error during encryption - {e}")

    def _gather_encryption_parameters(self):
        # create a dict with the input parameters
        key = b'1234567890123456'
        nonce = b'1234567890123456'

        return {
            "key": self.key,
            "nonce": self.nonce,
            "plaintext": self.entry_pt.get().encode(),  # encode string to bytes object
            "associated_data": self.entry_ad.get().encode(),
            "variant": self.optionmenu_variant.get(),
        }

    # def handle_decrypt(self):
    #     try:
    #         decrypt_params = self._gather_decryption_parameters()

    #         self.received_plaintext, execution_time = self.ascon_controller.decrypt_and_measure_time(
    #             decrypt_params)

    #         self.display_decryption_results(
    #             decrypt_params, self.received_plaintext, execution_time)
    #     except Exception as e:
    #         self.results_textbox.insert_line(f"Error during decryption -  {e}")

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
        self.results_textbox.add_title(f"DECRYPTION: {params['variant']}")

        # Print the decryption params and output
        self._result_print([
            ("Key", params['key']),
            ("Nonce", params['nonce']),
            ("Associated data", params['associated_data']),
            # Exclude the tag from ciphertext
            ("Ciphertext", params['ciphertext'][:-16]),
            ("Tag", params['ciphertext'][-16:])  # Last 16 bytes are the tag
        ])

        if received_plaintext is None:
            self.results_textbox.insert_line("It was not possible to decipher")
        else:
            self.results_textbox.insert_line(
                f"Received plaintext (str): {received_plaintext.decode()}")
            self.results_textbox.insert_line(
                f"Execution time (s): {execution_time:.6f} ")

    # Handlers for the sidebar button clicks
    def handle_demo(self):
        self.results_textbox.add_title("Demo")

    def handle_aead(self):
        self.results_textbox.add_title("AEAD")

    def _result_print(self, data):
        # Print aligned text
        maxlen = max([len(text) for (text, val) in data])
        for text, val in data:
            self.results_textbox.insert_line("{text}:{align} 0x{val} ({length} bytes)".format(text=text, align=(
                (maxlen - len(text)) * " "), val=self.ascon_controller.bytes_to_hex(val), length=len(val)))

    def handle_key_button(self):
        variant = self.optionmenu_variant.get()
        self.key = self.generate_key_callback(variant)

    def handle_nonce_button(self):
        self.nonce = self.generate_nonce_callback()
