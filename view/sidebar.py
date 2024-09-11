from customtkinter import CTkFrame, CTkLabel, CTkButton, CTkFont


class SidebarFrame(CTkFrame):
    def __init__(self, master, on_demo_click, on_aead_click, width=140, corner_radius=0, **kwargs):
        super().__init__(master, **kwargs)

        # Set up the grid
        # Span the sidebar across all rows (rowspan needs a large number e.g. 10)
        self.grid(row=0, column=0, rowspan=10, sticky="nsew")

        # Store callback functions
        self.on_demo_click = on_demo_click
        self.on_aead_click = on_aead_click

        self.logo_label = CTkLabel(
            self, text="ASCON", font=CTkFont(size=30, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.grid_rowconfigure(1, minsize=20)   # Second row is for space

        self.demo_button = CTkButton(
            self, text="Demo", font=CTkFont(weight="bold"), command=self.on_demo_click).grid(row=2, column=0, padx=20, pady=10)

        self.aead_button = CTkButton(
            self, text="AEAD", font=CTkFont(weight="bold"), command=self.on_aead_click).grid(row=3, column=0, padx=20, pady=10)

        self.info_button = CTkButton(
            self, text="About", font=CTkFont(weight="bold")).grid(row=4, column=0, padx=20, pady=10)
