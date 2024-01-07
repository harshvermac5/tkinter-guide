import tkinter as tk
from tkinter import messagebox

class MyGUI:

    def __init__(self):

        self.root = tk.Tk()

        self.label = tk.Label(self.root, text="Hello World")
        self.label.pack()

        self.textbox = tk.Text(self.root)
        self.textbox.bind("<KeyPress>", self.shortcut)
        self.textbox.pack()

        self.check_state = tk.IntVar()

        self.check = tk.Checkbutton(self.root, text="show message", variable=self.check_state)
        self.check.pack()

        self.button = tk.Button(self.root, text="Click Me!", command=self.show_message)
        self.button.pack()

        self.root.mainloop()

    def show_message(self):
        if self.check_state.get() == 0:
            print(self.textbox.get(1.0, tk.END))
        else:
            messagebox.showinfo(title="The Message", message=self.textbox.get(1.0, tk.END))


    def shortcut(self, event):
        if event.state == 12 and event.keysym == "Return":
            self.show_message()
        pass
MyGUI()