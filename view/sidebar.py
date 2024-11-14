import pkg_resources
import os
import sys
from PIL import Image, ImageTk
from customtkinter import CTkFrame, CTkLabel, CTkButton, CTkFont, CTkToplevel, CTkImage, set_appearance_mode, CTkOptionMenu


class SidebarFrame(CTkFrame):
    def __init__(self, master, switch_frame_callback, **kwargs):
        super().__init__(master, **kwargs)

        encrypt_icon = CTkImage(Image.open(
            self.get_asset_path("encrypt.png")), size=(20, 20))
        decrypt_icon = CTkImage(Image.open(
            self.get_asset_path("decrypt.png")), size=(20, 20))
        results_icon = CTkImage(Image.open(
            self.get_asset_path("results.png")), size=(20, 20))
        about_icon = CTkImage(Image.open(
            self.get_asset_path("about.png")), size=(15, 15))
        docs_icon = CTkImage(Image.open(
            self.get_asset_path("docs.png")), size=(20, 20))

        # Set up grid
        self.grid(row=0, column=0, sticky="nsew")

        self.logo_label = CTkLabel(
            self, text="ASCON", font=CTkFont(size=30, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 30))

        self.encrypt_button = CTkButton(
            self, text="Encrypt", image=encrypt_icon, compound="left", font=CTkFont(weight="bold"), command=lambda: switch_frame_callback("encryption"))
        self.encrypt_button.grid(row=2, column=0, padx=20, pady=10)

        self.decrypt_button = CTkButton(
            self, text="Decrypt", image=decrypt_icon, compound="left", font=CTkFont(weight="bold"), command=lambda: switch_frame_callback("decryption"))
        self.decrypt_button.grid(row=3, column=0, padx=20, pady=10)

        self.results_button = CTkButton(
            self, text="Results", image=results_icon, compound="left", font=CTkFont(weight="bold"), command=lambda: switch_frame_callback("results"))
        self.results_button.grid(row=4, column=0, padx=20, pady=10)

        # Empty space
        self.grid_rowconfigure(5, weight=1)  # Expands

        # self.docs_button = CTkButton(
        #     self, text="Docs", image=docs_icon, compound="left", font=CTkFont(weight="bold"), command=lambda: switch_frame_callback("encryption"))
        # self.docs_button.grid(row=6, column=0, padx=20, pady=10)

        self.theme_options = CTkOptionMenu(self, values=["Light Mode", "Dark Mode"],
                                           command=lambda choice: set_appearance_mode("light" if choice == "Light Mode" else "dark"))
        self.theme_options.set("Light Mode")  # Default to light mode
        self.theme_options.grid(row=6, column=0, padx=20, pady=10)

        self.about_button = CTkButton(
            self, text="About", image=about_icon, compound="left", font=CTkFont(weight="bold"), command=self.show_about_popup)
        self.about_button.grid(row=7, column=0, padx=20, pady=10)
        self.grid_rowconfigure(
            99, weight=0, minsize=20)

    def show_about_popup(self):
        popup = CTkToplevel(self)
        popup.title("About")
        popup.geometry("300x170")
        popup.transient(self)
        popup.grab_set()

        label = CTkLabel(
            popup, text="ASCON UI \nImplementation of Ascon v1.2 \n\n Author: Jazmin Bernal\nPontifical Catholic University (UCA)\n Argentina \n🇦🇷🧉\n", font=("Arial", 14))
        label.pack(padx=20, pady=20)

    # def get_asset_path(self, filename):
    #     # In bundled mode, PyInstaller unpacks resources to _MEIPASS
    #     if getattr(sys, 'frozen', False):  # Check if we are running in a bundled app
    #         return pkg_resources.resource_filename(__name__, os.path.join('assets', filename))
    #     else:
    #         # In development mode, look for assets in the root directory
    #         return os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'assets', filename)

    # def get_asset_path(self, filename):
    #     if getattr(sys, 'frozen', False):  # If running as a frozen executable
    #         # If in a bundled application, get the asset from the _MEIPASS folder
    #         bundle_dir = sys._MEIPASS
    #     else:
    #         # Otherwise, it's in the normal project directory
    #         # Current directory of the script
    #         bundle_dir = os.path.dirname(os.path.abspath(__file__))
    #         # Go up one level and into 'assets' folder
    #         bundle_dir = os.path.join(bundle_dir, '..', 'assets')

    #     return os.path.join(bundle_dir, filename)

    def get_asset_path(self, filename):
        # Check if running from a bundled PyInstaller app
        if getattr(sys, 'frozen', False):
            # PyInstaller sets 'frozen' when running a packaged app
            return os.path.join(sys._MEIPASS, 'assets', filename)
        else:
            # In development mode, look for assets in the root directory
            return os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'assets', filename)
