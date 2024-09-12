from customtkinter import CTkTextbox, CTkFont


class Textbox(CTkTextbox):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs, border_width=2,
                         font=CTkFont(family="Courier New"), state="disabled")
        self.grid(row=0, column=1,  padx=20, pady=20, sticky="nsew")

    def insert(self, index, text, tags=None):
        self.configure(state='normal')
        super().insert(index, text, tags)
        self.configure(state='disabled')  # config to be read-only

    def insert_line(self, text):
        self.insert("end", f"{text}\n")

    def clear(self):
        self.configure(state='normal')
        self.delete("0.0", "end")  # delete all text
        self.configure(state='disabled')

    def restart(self):
        self.clear()
        self.insert_line(
            "Implementación de Ascon v1.2 - http://ascon.iaik.tugraz.at/ \n")

    def add_title(self, text):
        self.insert_line(f"\n=== {text} ===\n")
