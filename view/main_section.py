from customtkinter import CTkFrame, CTkTabview, CTkEntry, CTkLabel, CTkTextbox, CTkOptionMenu, CTkButton, CTk
from view.textbox import Textbox


class MainSectionFrame(CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self._setup_grid()

        # TabControl
        self.tab_control = CTkTabview(self)
        self.tab_control.grid(row=0, column=0, columnspan=4, sticky="nsew")

        # Inputs tab
        self.inputs_tab = self.tab_control.add("Inputs")
        self._setup_inputs_tab()
        self._add_inputs()

        # Results tab
        self.results_tab = self.tab_control.add("Results")
        self._setup_results_tab()

    def _setup_grid(self):

        # Config 4 columns
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)  # Expands (inputs)
        self.grid_columnconfigure(2, weight=0)
        self.grid_columnconfigure(3, weight=0, minsize=250)

        self.grid_rowconfigure(0, weight=1)     # Row 0 expands vertically

    def _setup_inputs_tab(self):
        # Config grid para Inputs tab
        self.inputs_tab.grid_columnconfigure(
            0, weight=0)
        self.inputs_tab.grid_columnconfigure(
            1, weight=1)  # Second column expands
        self.inputs_tab.grid_columnconfigure(
            2, weight=0)
        self.inputs_tab.grid_columnconfigure(
            3, weight=0, minsize=250)

        # Config del grid para filas
        self.inputs_tab.grid_rowconfigure(11, weight=1)  # Row expands
        self.inputs_tab.grid_rowconfigure(
            13, weight=0, minsize=40)  # Min space at the end of the window

    def _setup_results_tab(self):
        # Configuring the grid in the Results tab
        self.results_tab.grid_columnconfigure(0, weight=1)  # Column 0 expands
        self.results_tab.grid_columnconfigure(1, weight=1)  # Column 1 expands
        self.results_tab.grid_columnconfigure(2, weight=1)  # Column 2 expands
        self.results_tab.grid_columnconfigure(3, weight=1)  # Column 3 expands

        self.results_tab.grid_rowconfigure(0, weight=1)  # Row 0 expands

        # Textbox expands to fit all the space
        self.results_textbox = CTkTextbox(self.results_tab)
        self.results_textbox.grid(
            row=0, column=0, columnspan=4, rowspan=1, padx=10, pady=10, sticky="nsew")

    def _add_inputs(self):

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
