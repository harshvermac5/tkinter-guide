import tkinter as tk

root = tk.Tk()

class MyGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.label = tk.Label(self.root, text="My Message", font=("Fira Sans", 12))
        self.label.pack(padx=10, pady=20)
        self.textbox = tk.textbox(self.root, font=("Fira Code", 8))
        self.textbox.pack(padx=10, pady=20)

        self.check_state = tk.IntVar()

        self.check = tk.Checkbutton(self.root, text="Show Textbox" font=("Fira Sans", 6), variable=self.check_state)
        self.check.pack(padx=10, pady=20)

        self.button = tk.Button(self.root, text="Show Textbook", font=("Fira Code", 4), command=self.show_message())
        self.button.pack(padx=10, pady=10)

        self.root.mainloop()
        
    def show_message(self):
        if self.check_state.get() == 0:
            print(self.textbox.get("1.0", tk.END))
        else:
            messagebox.showinfo(title="Message", message = self.textbox.get("1.0", tk.END))
MyGUI