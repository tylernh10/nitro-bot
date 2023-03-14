import customtkinter as ctk
import tkinter as tk
from nitro import Nitro_Bot
from frame import TopFrame, UserFrame, CompeteFrame

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # bot init
        self.bot = Nitro_Bot()

        # UI init
        self.geometry("500x250")
        self.title("Nitro Typing Bot")
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

    def button_callback(self):
        self.textbox.insert("insert", self.combobox.get() + "\n")
        
        # # self.button = ctk.CTkButton(self, command=self.button_click)
        # # self.button.grid(row=0, column=0, padx=10, pady=10)

        # slider = ctk.CTkSlider(self, from_=0, to=1000, command=self.slider_event, width=350)
        # slider.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # # self.textbox = ctk.CTkTextbox(self, text_color=("green"), width)
        # # self.slider_event(500)
        # # self.textbox = ctk.CTkTextbox(master=self, width=400, corner_radius=0)
        # # self.textbox.grid(row=0, column=0, sticky="nsew")
        # # self.textbox.insert("0.0", "Some example text!\n")

        # self.speed_text = tk.StringVar(value="Typing Speed (ms):")
        
        # self.speed_label = ctk.CTkLabel(master=self,
        #                        textvariable=self.speed_text,
        #                        width=120,
        #                        height=40,
        #                        corner_radius=8)
        # self.speed_label.place(relx=0.5, rely=0.35, anchor=tk.CENTER)
        
        # self.text_var = tk.StringVar(value="500")

        # self.label1 = ctk.CTkLabel(master=self,
        #                        textvariable=self.text_var,
        #                        width=120,
        #                        height=25,
        #                        fg_color=("white", "gray75"),
        #                        corner_radius=8)
        # self.label1.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
        

    def slider_event(self, value):
        self.text_var = tk.StringVar(value = str(int(value)))
        self.label1.configure(textvariable=self.text_var)

    def start_session(self):
        self.bot.initialize_driver()


if __name__ == "__main__":
    ctk.set_default_color_theme("green")
    app = App()
    app.mainloop()
