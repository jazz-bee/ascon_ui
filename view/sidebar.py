from customtkinter import CTkFrame, CTkLabel, CTkButton, CTkFont


class SidebarFrame(CTkFrame):
    def __init__(self, master, on_encrypt_click, on_decrypt_click, on_results_click, **kwargs):
        super().__init__(master, **kwargs)

        # Set up the grid
        # Span the sidebar across all rows (rowspan needs a large number e.g. 10)
        self.grid(row=0, column=0, rowspan=10, sticky="nsew")

        self.logo_label = CTkLabel(
            self, text="ASCON", font=CTkFont(size=30, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.grid_rowconfigure(1, minsize=20)   # Second row is for space
        self.grid_rowconfigure(5, weight=1)

        self.demo_button = CTkButton(
            self, text="Encrypt", font=CTkFont(weight="bold"), command=on_encrypt_click).grid(row=2, column=0, padx=20, pady=10)

        self.aead_button = CTkButton(
            self, text="Decrypt", font=CTkFont(weight="bold"), command=on_decrypt_click).grid(row=3, column=0, padx=20, pady=10)

        self.result_button = CTkButton(
            self, text="Results", font=CTkFont(weight="bold"), command=on_results_click).grid(row=4, column=0, padx=20, pady=10)
        self.info_button = CTkButton(
            self, text="About", font=CTkFont(weight="bold")).grid(row=9, column=0, padx=20, pady=10)
