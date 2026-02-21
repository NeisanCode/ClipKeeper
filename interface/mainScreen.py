from venv import create

import customtkinter as ctk

ctk.set_appearance_mode("system")

ctk.FontManager.load_font("fonts/Poppins-Bold.ttf")
ctk.FontManager.load_font("fonts/Poppins-Light.ttf")
ctk.FontManager.load_font("fonts/Poppins-Regular.ttf")


class MainScreen(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Les fonts APRES super().__init__()
        self.FONT_NORMAL = ctk.CTkFont(family="Poppins", size=14)
        self.FONT_BOLD = ctk.CTkFont(family="Poppins", size=14, weight="bold")
        self.FONT_TITLE = ctk.CTkFont(family="Poppins", size=24, weight="bold")

        self.title("Clipboard Manager")
        self.geometry("400x300")
        self.protocol("WM_DELETE_WINDOW", self.onclose)
        self.createSideBar()

    def createSideBar(self):
        self.sidebar = ctk.CTkFrame(self, width=200, corner_radius=0)
        self.sidebar.pack(side="left", fill="y")

        self.clip_elements = ctk.CTkButton(
            self.sidebar,
            text="ClipBoard",
            command=self.on_button_click,
            font=self.FONT_BOLD,
            fg_color="#1F618D",
            hover_color="#1F618D",
            cursor="hand2",
        )
        self.clip_elements.pack(pady=10, padx=14)

        self.button_close = ctk.CTkButton(
            self.sidebar,
            text="Close",
            command=self.on_button_close,
            font=self.FONT_BOLD,
            fg_color="#C0392B",
            hover_color="#C0392B",
            cursor="hand2",
        )
        self.button_close.pack(pady=10, padx=14)

    def on_button_click(self):
        print("Button clicked!")

    def on_button_close(self):
        self.destroy()

    def onclose(self):
        self.iconify()


if __name__ == "__main__":
    MainScreen().mainloop()
