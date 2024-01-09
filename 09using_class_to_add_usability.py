import tkinter as tk
from tkinter import messagebox

class MyGUI:
    def __init__(self):
        self.root = tk.Tk()

        self.label = tk.Label(self.root, text="My Message", font=("Fira Sans", 20))
        self.label.pack(padx=10, pady=20)

        self.textbox = tk.Text(self.root, font=("Fira Code", 10), width=50, height=10)
        self.textbox.pack()

        self.check_state = tk.IntVar() #initialise a intvar to keep track of state

        self.check = tk.Checkbutton(self.root, text="Show Messagebox", font=("Fira Sans", 10), variable=self.check_state)
        self.check.pack(padx=10, pady=20)

        self.button = tk.Button(self.root, text="Show Messagebox", font=("Fira Code", 10), command=self.show_message)
        self.button.pack(padx=10, pady=10)

        self.root.mainloop()
        
    def show_message(self):
        if self.check_state.get() == 0:
            print(self.textbox.get("1.0", tk.END))
        else:
            messagebox.showinfo(title="Message", message=self.textbox.get("1.0", tk.END))
        
MyGUI()