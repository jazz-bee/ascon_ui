from customtkinter import CTkFrame, CTkLabel, CTkButton, CTkFont, CTkToplevel, CTkImage
from PIL import Image, ImageTk


class SidebarFrame(CTkFrame):
    def __init__(self, master, switch_frame_callback, **kwargs):
        super().__init__(master, **kwargs)

        encrypt_icon = CTkImage(Image.open(
            "assets/encrypt.png"), size=(20, 20))
        decrypt_icon = CTkImage(Image.open(
            "assets/decrypt.png"), size=(20, 20))
        results_icon = CTkImage(Image.open(
            "assets/results.png"), size=(20, 20))
        about_icon = CTkImage(Image.open("assets/about.png"), size=(15, 15))
        docs_icon = CTkImage(Image.open("assets/docs.png"), size=(20, 20))

        # Set up grid
        self.grid(row=0, column=0, sticky="nsew")

        self.logo_label = CTkLabel(
            self, text="ASCON", font=CTkFont(size=30, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 30))

        self.encrypt_button = CTkButton(
            self, text="Encrypt", image=encrypt_icon, compound="left", font=CTkFont(family="Arial", weight="bold"), command=lambda: switch_frame_callback("encryption"))
        self.encrypt_button.grid(row=2, column=0, padx=20, pady=10)

        self.decrypt_button = CTkButton(
            self, text="Decrypt", image=decrypt_icon, compound="left", font=CTkFont(weight="bold"), command=lambda: switch_frame_callback("decryption"))
        self.decrypt_button.grid(row=3, column=0, padx=20, pady=10)

        self.results_button = CTkButton(
            self, text="Results", image=results_icon, compound="left", font=CTkFont(weight="bold"), command=lambda: switch_frame_callback("results"))
        self.results_button.grid(row=4, column=0, padx=20, pady=10)

        # Empty space
        self.grid_rowconfigure(5, weight=1)  # Expands

        self.docs_button = CTkButton(
            self, text="Docs", image=docs_icon, compound="left", font=CTkFont(weight="bold"), command=lambda: switch_frame_callback("encryption"))
        self.docs_button.grid(row=6, column=0, padx=20, pady=10)

        self.about_button = CTkButton(
            self, text="About", image=about_icon, compound="left", font=CTkFont(weight="bold"), command=self.show_info_popup)
        self.about_button.grid(row=7, column=0, padx=20, pady=10)
        self.grid_rowconfigure(
            99, weight=0, minsize=20)

    def show_info_popup(self):
        info_window = CTkToplevel(self)
        info_window.title("About")
        info_window.geometry("300x170")
        label = CTkLabel(
            info_window, text="ASCON UI \nImplementation of Ascon v1.2 \n\n Author: Jazmin Bernal\nPontifical Catholic University (UCA)\n Argentina \n🇦🇷🧉\n", font=("Arial", 14))
        label.pack(padx=20, pady=20)
