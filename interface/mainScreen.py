import customtkinter as ctk

from repo import savejson


ctk.set_appearance_mode("system")

ctk.FontManager.load_font("fonts/Poppins-Bold.ttf")
ctk.FontManager.load_font("fonts/Poppins-Light.ttf")
ctk.FontManager.load_font("fonts/Poppins-Regular.ttf")


class MainScreen(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.FONT_NORMAL = ctk.CTkFont(family="Poppins", size=14)
        self.FONT_BOLD = ctk.CTkFont(family="Poppins", size=14, weight="bold")
        self.FONT_TITLE = ctk.CTkFont(family="Poppins", size=24, weight="bold")

        self.title("Clipboard Manager")
        self.geometry("400x300")
        self.protocol("WM_DELETE_WINDOW", self.onclose)
        self.createSideBar()
        self.main_frame = ctk.CTkFrame(self, bg_color="#191F25", fg_color="#191F25")
        self.main_frame.pack(side="left", fill="both", expand=True)
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(1, weight=1)
        self.main_frame.grid_columnconfigure(2, weight=1)
        self.main_frame.grid_rowconfigure(0, weight=1)
        self.main_frame.grid_rowconfigure(1, weight=1)
        self.main_frame.grid_rowconfigure(2, weight=1)
        self.create_clip_elements()

    def createSideBar(self):
        self.sidebar = ctk.CTkFrame(self, width=200, corner_radius=0)
        self.sidebar.pack(side="left", fill="both", expand=False)

        self.clip_elements = ctk.CTkButton(
            self.sidebar,
            text="ClipBoard",
            command=self.on_button_clip_click,
            font=self.FONT_BOLD,
            fg_color="#1F618D",
            hover_color="#1F618D",
            cursor="hand2",
        )
        self.clip_elements.pack(pady=10, padx=14)

        self.button_close = ctk.CTkButton(
            self.sidebar,
            text="Close",
            command=self.on_button_close_click,
            font=self.FONT_BOLD,
            fg_color="#C0392B",
            hover_color="#C0392B",
            cursor="hand2",
        )
        self.button_close.pack(pady=10, padx=14)

    def create_clip_elements(self, clips: list[dict] = None):
        frame_color = "#FFFFFF"
        label_color = "#272727"
        label_background_color = "#FFFFFF"
        for clip in clips:
            container = ctk.CTkFrame(
                self.main_frame,
                fg_color=frame_color,
                corner_radius=8,
            )
            container.grid(row=0, column=0, sticky="nsew", padx=12, pady=12)
            title = ctk.CTkLabel(
                container,
                text=clip["timestamp"],
                font=self.FONT_TITLE,
                text_color=label_color,
            )
            title.pack(pady=10, padx=10)
            clip = ctk.CTkLabel(
                container,
                text=clip["content"],
                font=self.FONT_NORMAL,
                text_color=label_color,
            )
            clip.pack(pady=10, padx=10, fill="both", expand=True)

    def on_button_clip_click(self):
        clips = savejson.load_clips()
        self.create_clip_elements(clips)

    def on_button_close_click(self):
        self.destroy()

    def onclose(self):
        self.iconify()


if __name__ == "__main__":
    MainScreen().mainloop()
