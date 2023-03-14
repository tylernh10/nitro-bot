import tkinter as tk

class MyWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        # Set window properties
        self.title("My App")
        self.geometry("400x300")
        self.resizable(False, False)

        # Create some widgets
        self.label = tk.Label(self, text="Enter your name:")
        self.textbox = tk.Entry(self)
        self.button = tk.Button(self, text="Submit", bg="#4CAF50", fg="white", font=("Helvetica", 12, "bold"), command=self.on_submit)

        # Create a list box and add some items to it
        self.listbox = tk.Listbox(self, selectmode=tk.MULTIPLE)
        for i in range(10):
            self.listbox.insert(tk.END, f"Item {i}")

        # Create a slider and a label to display its value
        self.slider = tk.Scale(self, from_=0, to=100, orient=tk.HORIZONTAL, command=self.on_slider_changed)
        self.slider.set(50)
        self.slider_label = tk.Label(self, text="50", font=("Helvetica", 18))

        # Create a grid layout to arrange the widgets
        self.label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
        self.textbox.grid(row=0, column=1, padx=10, pady=10, sticky=tk.EW)
        self.button.grid(row=0, column=2, padx=10, pady=10, sticky=tk.E)
        self.listbox.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky=tk.NSEW)
        self.slider.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky=tk.NSEW)
        self.slider_label.grid(row=2, column=2, padx=10, pady=10, sticky=tk.NSEW)

        # Set grid weights
        self.columnconfigure(1, weight=1)
        self.rowconfigure(1, weight=1)

        # Set style
        self.configure(bg="#F1F1F1")

    def on_submit(self):
        name = self.textbox.get()
        print(f"Hello, {name}!")

    def on_slider_changed(self, value):
        self.slider_label.configure(text=value)

window = MyWindow()
window.mainloop()
