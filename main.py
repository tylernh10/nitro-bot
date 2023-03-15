import customtkinter as ctk
import tkinter as tk
from nitro import Nitro_Bot
from frame import TopFrame, UserFrame, CompeteFrame

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.protocol("WM_DELETE_WINDOW", self.on_close)

        # bot init
        self.bot = Nitro_Bot()

        # UI init
        self.geometry("500x250")
        self.title("Nitro Bot")
        self.minsize(500, 300)
        self.maxsize(500, 300)
        self.configure(fg_color="#e3e3e3")

        # create grid system
        self.grid_rowconfigure(0, weight=0)
        self.grid_columnconfigure((0, 1), weight=1)

        # setup topframe
        self.topframe = TopFrame(self, bot=self.bot)
        self.topframe.grid(row=0, column=0, columnspan=2)

        # setup userframe
        self.userframe = UserFrame(self, userinfo_dict=self.bot.users, bot=self.bot)
        self.userframe.grid(row=1, column=0, columnspan=1, padx=20, pady=(20,0), stick="ew")
        
        # setup competeframe
        self.competeframe = CompeteFrame(self, bot=self.bot)
        self.competeframe.grid(row=1, column=1, columnspan=1, padx=20, pady=20)
        
    # when user clicks the x button, all data is saved to file
    def on_close(self):
        self.bot.write_users()
        self.destroy()
        
if __name__ == "__main__":
    ctk.set_default_color_theme("green")
    app = App()
    app.mainloop()
