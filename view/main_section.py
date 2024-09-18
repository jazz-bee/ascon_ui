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

        # Configuración del grid para filas
        self.inputs_tab.grid_rowconfigure(0, weight=0)
        self.inputs_tab.grid_rowconfigure(1, weight=0)
        self.inputs_tab.grid_rowconfigure(2, weight=0)
        self.inputs_tab.grid_rowconfigure(3, weight=0)
        self.inputs_tab.grid_rowconfigure(4, weight=0)
        self.inputs_tab.grid_rowconfigure(5, weight=1)  # Row 5 expands

        # Inputs
        self.entry_key = CTkEntry(
            self.inputs_tab, placeholder_text="Enter Key")
        self.entry_key.grid(row=0, column=0, columnspan=2,
                            padx=10, pady=10, sticky="ew")

        self.entry_nonce = CTkEntry(
            self.inputs_tab, placeholder_text="Enter Nonce")
        self.entry_nonce.grid(row=1, column=0, columnspan=2,
                              padx=10, pady=10, sticky="ew")

        # Cipher button does not expand
        self.cipher_button = CTkButton(self.inputs_tab, text="Encrypt")
        self.cipher_button.grid(row=6, column=0, padx=10, pady=10, sticky="w")

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
