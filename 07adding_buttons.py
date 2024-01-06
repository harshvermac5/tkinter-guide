import tkinter as tk

root = tk.Tk()

#adding the width x height value using geometry function
root.geometry("640x480")

#adding the title using title method
root.title("This is my Third GUI Project")

#creating the button
button1 = tk.Button(text="Press me!", font=("Fira Sans Heavy", 36))

#adding the button
button1.pack()

root.mainloop()