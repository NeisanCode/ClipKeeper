from datetime import datetime
import customtkinter as ctk
import threading
from repo import savejson
from service.service import watcher_clipper


ctk.set_appearance_mode("system")

ctk.FontManager.load_font("assets/fonts/Poppins-Bold.ttf")
ctk.FontManager.load_font("assets/fonts/Poppins-Light.ttf")
ctk.FontManager.load_font("assets/fonts/Poppins-Regular.ttf")
from PIL import Image


class MainScreen(ctk.CTk):
    CARD_WIDTH = 200
    CARD_MAX_HEIGHT = 150
    CARD_CHARS_PER_LINE = 20
    CARD_MAX_LINES = 4

    def __init__(self):
        super().__init__()
        self.FONT_NORMAL = ctk.CTkFont(family="Poppins", size=12)
        self.FONT_BOLD = ctk.CTkFont(family="Poppins", size=12, weight="bold")
        self.FONT_TITLE = ctk.CTkFont(family="Poppins", size=24, weight="bold")

        self.title("Clipboard Manager")
        self.geometry("900x600")
        self.protocol("WM_DELETE_WINDOW", self.onclose)
        self.createSideBar()

        self.main_frame = ctk.CTkFrame(self, bg_color="#191F25", fg_color="#191F25")
        self.main_frame.pack(side="left", fill="both", expand=True)

        self.scroll_frame = ctk.CTkScrollableFrame(
            self.main_frame,
            fg_color="#191F25",
            scrollbar_button_color="#2A2F35",
        )
        self.scroll_frame.pack(fill="both", expand=True, padx=16, pady=16)
        self.scroll_frame.bind("<Button-4>", self._on_mousewheel)
        self.scroll_frame.bind("<Button-5>", self._on_mousewheel)

        for col in range(3):
            self.scroll_frame.columnconfigure(col, weight=0, minsize=220)
        self.on_app_load()
        watcher_clipper(lambda: self.after(0, self.on_app_load))

    def _on_mousewheel(self, event):
        if event.num == 4:
            self.scroll_frame._parent_canvas.yview_scroll(-1, "units")
        elif event.num == 5:
            self.scroll_frame._parent_canvas.yview_scroll(1, "units")

    def createSideBar(self):
        self.sidebar = ctk.CTkFrame(self, width=200, corner_radius=0)
        self.sidebar.pack(side="left", fill="both", expand=False)

        self.clip_elements = ctk.CTkButton(
            self.sidebar,
            text="Reload",
            command=self.on_app_load,
            font=self.FONT_BOLD,
            fg_color="#1F618D",
            hover_color="#1F618D",
            cursor="hand2",
        )
        self.clip_elements.pack(pady=10, padx=14)

        self.button_close = ctk.CTkButton(
            self.sidebar,
            text="Close",
            command=self.on_close_click,
            font=self.FONT_BOLD,
            fg_color="#C0392B",
            hover_color="#C0392B",
            cursor="hand2",
        )
        self.button_close.pack(pady=10, padx=14)

    def on_app_load(self):
        clips = savejson.load_clips()
        self.create_clip_elements(clips)

    def on_close_click(self):
        self.destroy()

    def onclose(self):
        self.iconify()

    def truncate_text(self, text: str) -> str:
        max_chars = self.CARD_MAX_LINES * self.CARD_CHARS_PER_LINE
        if len(text) <= max_chars:
            return text
        return text[: max_chars - 1].rstrip() + "..."

    def create_clip_elements(self, clips: list[dict]):
        for widget in self.scroll_frame.winfo_children():
            widget.destroy()

        for index, clip in enumerate(clips):
            row = index // 3
            column = index % 3

            # Outer frame avec taille strictement fixée
            outer = ctk.CTkFrame(
                self.scroll_frame,
                fg_color="#2A2F35",
                corner_radius=8,
                width=self.CARD_WIDTH,
                height=self.CARD_MAX_HEIGHT,
            )
            outer.grid(row=row, column=column, padx=8, pady=8, sticky="nw")
            timestamp = datetime.fromisoformat(clip["timestamp"])
            formatted_timestamp = timestamp.strftime("%d/%m/%Y")

            truncated = self.truncate_text(clip["content"])
            content = ctk.CTkLabel(
                outer,
                text=truncated,
                font=self.FONT_NORMAL,
                text_color="#FFFFFF",
                wraplength=178,
                justify="left",
                anchor="nw",
                width=180,
            )
            content.place(x=10, y=44)
            icon = ctk.CTkImage(Image.open("assets/icons/copy.png"), size=(16, 16))

            clip_button = ctk.CTkButton(
                outer,
                text="",
                font=self.FONT_BOLD,
                fg_color="#1F658D",
                hover_color="#1F618D",
                cursor="hand2",
                width=32,
                height=32,
                image=icon,
            )
            clip_button.configure(
                command=lambda b=clip_button, i=icon, c=clip["content"]: self.on_copy(
                    button=b,
                    icon=i,
                    content=c,
                )
            )
            clip_button.place(x=160, y=8)

    def copy_to_clipboard(self, text: str):
        self.clipboard_clear()
        self.clipboard_append(text)
        self.update()

    def on_copy(self, button: ctk.CTkButton, icon: ctk.CTkImage, content: str):
        self.copy_to_clipboard(content)
        check_icon = ctk.CTkImage(Image.open("assets/icons/check.png"), size=(16, 16))
        button.configure(image=check_icon)
        threading.Timer(
            1.5,
            lambda: self.after(
                0,
                lambda: button.configure(image=icon) if button.winfo_exists() else None,
            ),
        ).start()


if __name__ == "__main__":
    MainScreen().mainloop()
