from customtkinter import CTkFrame, CTkLabel, CTkButton, CTkFont


class SidebarFrame(CTkFrame):
    def __init__(self, master, on_demo_click, on_aead_click, **kwargs):
        super().__init__(master, **kwargs)

        # Store callback functions
        self.on_demo_click = on_demo_click
        self.on_aead_click = on_aead_click

        self.logo_label = CTkLabel(
            self, text="ASCON", font=CTkFont(size=30, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.demo_button = CTkButton(
            self, text="Demo", command=self.on_demo_click).grid(row=1, column=0, padx=20, pady=10)

        self.aead_button = CTkButton(
            self, text="AEAD", command=self.on_aead_click).grid(row=2, column=0, padx=20, pady=10)
