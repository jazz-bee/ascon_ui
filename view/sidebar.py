from customtkinter import CTkFrame, CTkLabel, CTkButton, CTkFont, CTkToplevel


class SidebarFrame(CTkFrame):
    def __init__(self, master, switch_frame_callback, **kwargs):
        super().__init__(master, **kwargs)

        # Set up grid
        self.grid(row=0, column=0, sticky="nsew")

        self.logo_label = CTkLabel(
            self, text="ASCON", font=CTkFont(size=30, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 30))

        self.encrypt_button = CTkButton(
            self, text="🔐 Encrypt", font=CTkFont(weight="bold"), command=lambda: switch_frame_callback("encryption"))
        self.encrypt_button.grid(row=2, column=0, padx=20, pady=10)

        self.decrypt_button = CTkButton(
            self, text="🔓 Decrypt", font=CTkFont(weight="bold"), command=lambda: switch_frame_callback("decryption"))
        self.decrypt_button.grid(row=3, column=0, padx=20, pady=10)

        self.results_button = CTkButton(
            self, text="📺 Results", font=CTkFont(weight="bold"), command=lambda: switch_frame_callback("results"))
        self.results_button.grid(row=4, column=0, padx=20, pady=10)

        # Empty space
        self.grid_rowconfigure(5, weight=1)  # Expands

        self.about_button = CTkButton(
            self, text="ⓘ About", font=CTkFont(weight="bold"), command=self.show_info_popup)
        self.about_button.grid(row=6, column=0, padx=20, pady=10)
        self.grid_rowconfigure(
            99, weight=0, minsize=20)

    def show_info_popup(self):
        info_window = CTkToplevel(self)
        info_window.title("About")
        info_window.geometry("300x170")
        label = CTkLabel(
            info_window, text="\n Created by:\n Jazmin Bernal\n\nPontifical Catholic University (UCA)\n\n 🇦🇷 Argentina 🧉\n", font=("Arial", 14))
        label.pack(padx=20, pady=20)
