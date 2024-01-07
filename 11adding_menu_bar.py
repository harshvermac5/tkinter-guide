import tkinter as tk
from tkinter import messagebox

class MyGUI:

    def __init__(self):

        self.root = tk.Tk()

        self.menubar = tk.Menu(self.root)
        
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Close", command= self.on_closing)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Force Close", command=quit)

        self.actionmenu = tk.Menu(self.menubar, tearoff=0)
        self.actionmenu.add_command(label="Show message", command=self.show_message)

        self.menubar.add_cascade(menu=self.filemenu, label="File")
        self.menubar.add_cascade(menu=self.actionmenu, label="Action")

        self.root.config(menu=self.menubar)

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

        self.clearbutton = tk.Button(self.root, text="Clear", command=self.clear)
        self.clearbutton.pack()

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.root.mainloop()

    def clear(self):
        self.textbox.delete("1.0", tk.END)

    def show_message(self):
        if self.check_state.get() == 0:
            print(self.textbox.get(1.0, tk.END))
        else:
            messagebox.showinfo(title="The Message", message=self.textbox.get(1.0, tk.END))


    def shortcut(self, event):
        if event.state == 12 and event.keysym == "Return":
            self.show_message()
        pass

    def on_closing(self):
        if messagebox.askyesno(title="Quit?", message="Are you sure?"):
            self.root.destroy()
MyGUI()