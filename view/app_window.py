import customtkinter as ct
from view.textbox import Textbox
from view.sidebar import SidebarFrame
from view.encryption_section import EncryptionSectionFrame
from view.decryption_section import DecryptionSectionFrame
from controllers.ascon_controller import AsconController


class AppWindow(ct.CTk):
    def __init__(self):
        super().__init__()

        # Config
        self.title("Lightweight Cryptography - ASCON UI")
        self.window_config()

        self.ascon_controller = AsconController()

        # Initialize parameters
        self.key = None
        self.nonce = None
        self.ciphertext = None
        self.received_plaintext = None
        self.encryption_result = {}

        # Initialize frames
        self.encryption_section_frame = EncryptionSectionFrame(
            self, self.handle_encrypt, self.handle_key_button, self.handle_nonce_button)
        self.decryption_section_frame = DecryptionSectionFrame(
            self, self.handle_decrypt, self.get_encryption_result)

        # Initialize components
        self.ascon_controller = AsconController()
        self.results_textbox = Textbox(self)
        self.about_window = None

        # Initially show the encryption frame
        self.current_frame = None
        self.switch_frame("encryption")

        # Sidebar Frame
        self.sidebar_frame = SidebarFrame(self, self.switch_frame)
        self.sidebar_frame.grid(row=0, column=0, sticky="nsew")

    def window_config(self):
        self.geometry(f"{1100}x{580}")
        self.minsize(1100, 580)
        self._setup_grid()
        ct.set_appearance_mode("light")
        ct.set_default_color_theme("dark-blue")

    def _setup_grid(self):
        self.grid_columnconfigure(0, weight=0, minsize=170)  # Sidebar
        self.grid_columnconfigure(1, weight=1)  # Main Section
        self.grid_rowconfigure(0, weight=1)  # Expands

    def handle_encrypt(self, params):
        try:
            self.ciphertext, execution_time = self.ascon_controller.encrypt_and_measure_time(
                params)
            self.display_encryption_results(
                params, self.ciphertext, execution_time)
            self.encryption_result = {
                "params": params,
                "ciphertext": self.ciphertext[:-16],
                "tag": self.ciphertext[-16:]
            }
        except Exception as e:
            self.results_textbox.insert_line(
                f"\nError during encryption - {e}")

    def handle_decrypt(self, params):
        try:
            self.received_plaintext, execution_time = self.ascon_controller.decrypt_and_measure_time(
                params)
            self.display_decryption_results(
                params, self.received_plaintext, execution_time)
        except Exception as e:
            self.results_textbox.insert_line(
                f"\nError during decryption -  {e}")

    def display_encryption_results(self, params, ciphertext, execution_time):
        # Title depending on variant
        self.results_textbox.add_title(f"ENCRYPTION: {params['variant']}")

        # Print the input params and ascon output
        self._result_print([
            ("Key", params['key']),
            ("Nonce", params['nonce']),
            ("Plaintext", params['plaintext']),
            ("Associated data", params['associated_data']),
            ("Ciphertext", ciphertext[:-16]),
            ("Tag", ciphertext[-16:])  # Last 16 bytes are the tag
        ])

        # Show the size of the output and the execution time
        self.results_textbox.insert_line(
            f"Output size (bytes): {len(ciphertext)}")
        self.results_textbox.insert_line(
            f"Execution time (s): {execution_time:.6f}")

    def display_decryption_results(self, params, received_plaintext, execution_time):
        self.results_textbox.add_title(f"DECRYPTION: {params['variant']}")

        # Print the decryption params and output
        self._result_print([
            ("Key", params['key']),
            ("Nonce", params['nonce']),
            ("Associated data", params['associated_data']),
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

    def _result_print(self, data):
        # Print aligned text
        maxlen = max([len(text) for (text, val) in data])
        for text, val in data:
            self.results_textbox.insert_line("{text}:{align} 0x{val} ({length} bytes)".format(text=text, align=(
                (maxlen - len(text)) * " "), val=self.ascon_controller.bytes_to_hex(val), length=len(val)))

    def handle_key_button(self, variant):
        self._generate_random_key(variant)
        key_in_hex = self.ascon_controller.bytes_to_hex(self.key)
        self.results_textbox.insert_line(f"Key generated:  0x{key_in_hex}")
        return self.key

    def _generate_random_key(self, variant):
        keysize = 20 if variant == "Ascon-80pq" else 16
        self.key = self.ascon_controller.get_random_key(
            keysize)

    def handle_nonce_button(self):
        self._generate_random_nonce()
        nonce_in_hex = self.ascon_controller.bytes_to_hex(self.nonce)
        self.results_textbox.insert_line(f"Nonce generated:  0x{nonce_in_hex}")
        return self.nonce

    def _generate_random_nonce(self):
        self.nonce = self.ascon_controller.get_random_nonce(
            16)  # zero_bytes(16)

    def switch_frame(self, frame_name):

        if self.current_frame:
            self.current_frame.grid_forget()  # Hides current frame

        selected_frame = {
            "encryption": self.encryption_section_frame,
            "decryption": self.decryption_section_frame,
            "results": self.results_textbox
        }.get(frame_name)

        # Show the selected frame

        if selected_frame:
            selected_frame.grid(row=0, column=1, sticky="nsew")
            self.current_frame = selected_frame
        else:
            print(f"No frame found for {frame_name}")

    def get_encryption_result(self):
        return self.encryption_result
