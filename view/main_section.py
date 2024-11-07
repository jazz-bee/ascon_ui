from customtkinter import CTkFrame


class MainSectionFrame(CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color="transparent")

        self._common_grid_config()
        self.add_inputs_widgets()

    def _common_grid_config(self):

        # Config 4 columns
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)  # Expands (inputs)
        self.grid_columnconfigure(2, weight=0)
        self.grid_columnconfigure(3, weight=0, minsize=250)

        self.grid_rowconfigure(0, minsize=50)     # Row 0 with minsize
        # self.grid_rowconfigure(11, weight=1)  # Row expands
        self.grid_rowconfigure(
            99, weight=0, minsize=20)  # Min space at the end of the window

    def add_inputs_widgets(self):
        pass  # Meant to be overridden by child classes
