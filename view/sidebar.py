from customtkinter import CTkFrame, CTkLabel, CTkButton, CTkFont, CTkToplevel


class SidebarFrame(CTkFrame):
    def __init__(self, master, switch_frame_callback, **kwargs):
        super().__init__(master, **kwargs)

        # Set up grid
        # Span the sidebar across all rows (rowspan needs a large number e.g. 10)
        self.grid(row=0, column=0, rowspan=10, sticky="nsew")
        self.grid_rowconfigure(1, minsize=20)  # Row after title: empty space
        self.grid_rowconfigure(5, weight=1)  # Expands

        self.logo_label = CTkLabel(
            self, text="ASCON", font=CTkFont(size=30, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.encrypt_button = CTkButton(
            self, text="🔐 Encrypt", font=CTkFont(weight="bold"), command=lambda: switch_frame_callback("encryption"))
        self.encrypt_button.grid(row=2, column=0, padx=20, pady=10)

        self.decrypt_button = CTkButton(
            self, text="🔓 Decrypt", font=CTkFont(weight="bold"), command=lambda: switch_frame_callback("decryption"))
        self.decrypt_button.grid(row=3, column=0, padx=20, pady=10)

        self.results_button = CTkButton(
            self, text="📺 Results", font=CTkFont(weight="bold"), command=lambda: switch_frame_callback("results"))
        self.results_button.grid(row=4, column=0, padx=20, pady=10)

        self.about_button = CTkButton(
            self, text="ⓘ About", font=CTkFont(weight="bold"), command=self.show_info_popup)
        self.about_button.grid(row=9, column=0, padx=20, pady=10)

    def show_info_popup(self):
        info_window = CTkToplevel(self)
        info_window.title("About")
        info_window.geometry("300x170")
        label = CTkLabel(
            info_window, text="Created by:\n Jazmin Bernal\n\n Software Engineer ?\n Pontifical Catholic University (UCA)\n\n 🇦🇷 Argentina 🧉\n", font=("Arial", 14))
        label.pack(padx=20, pady=20)
