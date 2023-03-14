import tkinter as tk
from tkinter import ttk

class StylishGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Stylish GUI")
        self.master.geometry("400x300")
        self.master.config(bg="#f2f2f2")

        # Create a frame
        self.frame = ttk.Frame(self.master, padding=20)
        self.frame.pack()

        # Add a label
        self.label = ttk.Label(self.frame, text="Hello, World!", font=("Helvetica", 24), foreground="#333")
        self.label.pack(pady=20)

        # Add a button
        self.button = ttk.Button(self.frame, text="Click me!", style="Custom.TButton", command=self.clicked)
        self.button.pack()

        # Define a custom style for the button
        self.master.style = ttk.Style()
        self.master.style.configure("Custom.TButton", foreground="#fff", background="#333", font=("Helvetica", 14), padding=10, borderwidth=0)
        self.master.style.map("Custom.TButton", foreground=[("active", "#333"), ("disabled", "#ccc")], background=[("active", "#ccc"), ("disabled", "#f2f2f2")])

    def clicked(self):
        self.label.config(text="Button clicked!")

if __name__ == '__main__':
    root = tk.Tk()
    gui = StylishGUI(root)
    root.mainloop()


# import tkinter as tk
# from tkinter import ttk

# class StylishGUI:
#     def __init__(self, master):
#         self.master = master
#         self.master.title("Stylish GUI")
#         self.master.geometry("400x300")
#         self.master.config(bg="#f2f2f2")

#         # Create a frame
#         self.frame = ttk.Frame(self.master, padding=20)
#         self.frame.pack()

#         # Add a label
#         self.label = ttk.Label(self.frame, text="Hello, World!", font=("Helvetica", 24), foreground="#333")
#         self.label.pack(pady=20)

#         # Add a button
#         self.button = ttk.Button(self.frame, text="Click me!", style="Custom.TButton", command=self.clicked)
#         self.button.pack()

#         # Define a custom style for the button
#         self.master.style = ttk.Style()
#         self.master.style.configure("Custom.TButton", foreground="#fff", background="#333", font=("Helvetica", 14), padding=10)

#         # Add a scrollable list
#         self.scrollbar = ttk.Scrollbar(self.frame, orient="vertical")
#         self.listbox = tk.Listbox(self.frame, yscrollcommand=self.scrollbar.set)
#         self.scrollbar.config(command=self.listbox.yview)
#         self.scrollbar.pack(side="right", fill="y")
#         self.listbox.pack(side="left", fill="both", expand=True)

#         # Add items to the list
#         for i in range(20):
#             self.listbox.insert("end", f"Item {i+1}")

#         # Add a text box
#         self.textbox = tk.Text(self.frame, height=5, width=40)
#         self.textbox.pack(pady=20)

#         # Bind the text box to a callback function
#         self.textbox.bind("<KeyRelease>", self.update_text)

#     def clicked(self):
#         self.label.config(text="Button clicked!")

#     def update_text(self, event):
#         text = self.textbox.get("1.0", "end-1c")
#         self.label.config(text=text)

# if __name__ == '__main__':
#     root = tk.Tk()
#     gui = StylishGUI(root)
#     root.mainloop()


# import tkinter as tk
# from tkinter import ttk

# class StylishGUI:
#     def __init__(self, master):
#         self.master = master
#         self.master.title("Stylish GUI")
#         self.master.geometry("400x300")
#         self.master.config(bg="#f2f2f2")

#         # Create a frame
#         self.frame = ttk.Frame(self.master, padding=20)
#         self.frame.pack()

#         # Add a label
#         self.label = ttk.Label(self.frame, text="Hello, World!", font=("Helvetica", 24), foreground="#333")
#         self.label.pack(pady=20)

#         # Add a button
#         self.button = ttk.Button(self.frame, text="Click me!", style="Custom.TButton", command=self.clicked)
#         self.button.pack()

#         # Define a custom style for the button
#         self.master.style = ttk.Style()
#         self.master.style.configure("Custom.TButton", foreground="#fff", background="#333", font=("Helvetica", 14), padding=10)

#         # Add a scrollable list
#         self.scrollbar = ttk.Scrollbar(self.frame, orient="vertical")
#         self.listbox = tk.Listbox(self.frame, yscrollcommand=self.scrollbar.set)
#         self.scrollbar.config(command=self.listbox.yview)
#         self.scrollbar.pack(side="right", fill="y")
#         self.listbox.pack(side="left", fill="both", expand=True)

#         # Add items to the list
#         for i in range(20):
#             self.listbox.insert("end", f"Item {i+1}")

#     def clicked(self):
#         self.label.config(text="Button clicked!")

# if __name__ == '__main__':
#     root = tk.Tk()
#     gui = StylishGUI(root)
#     root.mainloop()
