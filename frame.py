import customtkinter as ctk
import tkinter as tk

class TopFrame(ctk.CTkFrame):
    def __init__(self, *args, bot, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.bot = bot
        
        self.configure(fg_color="#e3e3e3")
        
        self.header = ctk.CTkLabel(self, text="Nitro Type Bot", font=(ctk.CTkFont(), 14))
        self.header.pack(pady=(0, 3))

        self.button1 = ctk.CTkButton(self, command=self.initialize, text="Start New Session")
        self.button1.pack()

    def initialize(self):
        self.bot.bot_thread(self.bot.initialize_driver)

class UserFrame(ctk.CTkFrame):
    def __init__(self, *args, userinfo_dict, bot, **kwargs):
        super().__init__(*args, **kwargs)

        self.userinfo_dict = userinfo_dict
        self.bot = bot
        
        self.configure(fg_color="#e3e3e3")

        # username entry
        self.dialog1 = ctk.CTkEntry(master=self, placeholder_text="username")
        self.dialog1.pack(padx=5, pady=5)

        # password entry
        self.dialog2 = ctk.CTkEntry(master=self, placeholder_text="password", show="*")
        self.dialog2.pack(padx=5, pady=5)

        self.label = ctk.CTkLabel(self, text="Saved User Info", font=(ctk.CTkFont(), 11))
        self.label.pack(pady=(20, 0))
        
        # username dropdown
        self.combobox = ctk.CTkComboBox(
            master=self, 
            values=["Select a user"] + list(self.userinfo_dict.keys()),
            command=self.select_user,
        )
        self.combobox.pack(padx=5)

        # login button
        self.login = ctk.CTkButton(master=self, command=self.login, text="Login")
        self.login.pack(padx=5, pady=5)

    def select_user(self, choice):
        self.dialog1.delete(0, 1000000)
        self.dialog2.delete(0, 1000000)
        if choice != "No user selected":
            self.dialog1.insert(0, choice)
            self.dialog2.insert(0, self.userinfo_dict[choice])
        else:
            self.dialog1.configure(placeholder_text="username")
            self.dialog2.configure(placeholder_text="password")

    def login(self):
        if self.bot.valid_session():
            try:
                username = self.dialog1.get()
                password = self.dialog2.get()
                self.bot.bot_thread(self.bot.sign_in, username, password)
            except Exception as e:
                print("signin failed: ", type(e), e)

class CompeteFrame(ctk.CTkFrame):
    def __init__(self, *args, bot, **kwargs):
        super().__init__(*args, **kwargs)

        self.bot = bot

        self.configure(fg_color="#e3e3e3")
        
        # text speed label
        self.label = ctk.CTkLabel(self, text="Delay: 500ms", font=(ctk.CTkFont(), 12))
        self.label.pack(padx=20)
        
        # text speed slider
        self.slider = ctk.CTkSlider(self, from_=0, to=1000, command=self.change_speed)
        self.slider.pack(padx=20, pady=(0, 5))

        # auto check box
        self.checkbox = ctk.CTkCheckBox(self, text="auto continue", command=self.checkbox_event, border_width=3)
        self.checkbox.pack()

        # race now button
        self.racenow_button = ctk.CTkButton(self, command=self.racenow_event, text="Race Now", fg_color="#d32b3b", hover_color="#a3242c")
        self.racenow_button.pack(padx=20, pady=20)

    def change_speed(self, value):
        value_str = f"Delay: {int(value - value % 1)}ms"
        string_var = tk.StringVar(value=value_str)
        self.label.configure(textvariable=string_var)
        self.bot.update_speed(int(value))

    def checkbox_event(self):
        print("checkbox clicked")

    def racenow_event(self):
        if self.bot.valid_session():
            self.bot.bot_thread(self.bot.race_now)
