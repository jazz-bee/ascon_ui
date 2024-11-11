import customtkinter as ct
from tkinter import PhotoImage
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
        self._window_config()
        self._set_icon()

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

    def _window_config(self):
        self.geometry(f"{1100}x{580}")
        self.minsize(1100, 580)
        self._setup_grid()
        ct.set_appearance_mode("light")
        ct.set_default_color_theme("dark-blue")
        self.iconbitmap("assets/icon-mac.icns")

    def _setup_grid(self):
        self.grid_columnconfigure(0, weight=0, minsize=170)  # Sidebar
        self.grid_columnconfigure(1, weight=1)  # Main Section
        self.grid_rowconfigure(0, weight=1)  # Expands

    def _set_icon(self):
        icon = PhotoImage(file="assets/icon.png")
        self.iconphoto(False, icon)

    def handle_encrypt(self, params):
        try:
            self._prepare_debug_mode()
            self.ciphertext, execution_time = self.ascon_controller.encrypt_and_measure_time(
                params)
            self._store_and_display_encryption_results(
                params, self.ciphertext, execution_time)
            self._handle_debug_output()
        except Exception as e:
            self._handle_encryption_error(e)

    def _handle_encryption_error(self, e):
        self.results_textbox.insert_line(
            f"\n- ERROR DURING ENCRYPTION - {e}")

    def _prepare_debug_mode(self):
        debug_mode = self._debug_mode_enabled()
        self.ascon_controller.set_debug_mode(debug_mode)

    def _perform_encryption(self, params):
        self.ciphertext, execution_time = self.ascon_controller.encrypt_and_measure_time(
            params)
        self._display_encryption_results(
            params, self.ciphertext, execution_time)

    def _store_and_display_encryption_results(self, params, ciphertext, execution_time):
        self._display_encryption_results(params, ciphertext, execution_time)
        self.encryption_result = {
            "params": params,
            "ciphertext": ciphertext[:-16],
            "tag": ciphertext[-16:]
        }

    def _handle_debug_output(self):
        if self._debug_mode_enabled():
            debug_result = self.ascon_controller.get_debug_output()
            self.results_textbox.add_title(
                "DEBUG MODE: Ascon state (S)")
            self.results_textbox.insert_line(debug_result)

    def _debug_mode_enabled(self):
        return self.encryption_section_frame.get_debug_switch_value()

    def handle_decrypt(self, params):
        try:
            self.received_plaintext, execution_time = self.ascon_controller.decrypt_and_measure_time(
                params)
            self._display_decryption_results(
                params, self.received_plaintext, execution_time)
        except Exception as e:
            self.results_textbox.insert_line(
                f"\n- ERROR DURING DECRYPTION -  {e}")

    def _display_encryption_results(self, params, ciphertext, execution_time):
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

    def _display_decryption_results(self, params, received_plaintext, execution_time):
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
