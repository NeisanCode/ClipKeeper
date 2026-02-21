import customtkinter as ctk

ctk.set_appearance_mode("system")  # Set the appearance mode to dark


class MainScreen(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Main Window")
        self.geometry("400x300")

        self.label = ctk.CTkLabel(self, text="Welcome to the Main Window!")
        self.label.pack(pady=20)

        self.button = ctk.CTkButton(self, text="Click Me", command=self.on_button_click)
        self.button.pack(pady=10)


        label = ctk.CTkLabel(self, text="Fermer = minimiser !")
        label.pack(pady=20)

        self.protocol("WM_DELETE_WINDOW", self.onclose)

    def on_button_click(self):
        self.label.configure(text="Button Clicked!")

    def onclose(self):
        self.iconify()
