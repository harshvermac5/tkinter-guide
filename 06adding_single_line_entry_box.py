import tkinter as tk

root = tk.Tk()

#adding the width x height value using geometry function
root.geometry("640x480")

#adding the title using title method
root.title("This is my Third GUI Project")

#Creating the label field
label = tk.Label(root, text="Hello Harsh!", font=("Fira Sans", 24))

#adding the label field using pack method
label.pack()
label.pack(padx=20, pady=30) #adding the custom paddings

#creating the configurable text box, Height is Font size dependent
textbox = tk.Text(root, font=("Fira Code", 16), height=5, width=20)

#adding the text box to ui using pack method
textbox.pack()

#creating one liner entry box
myentry = tk.Entry(root)

#adding the entry to ui
myentry.pack()

root.mainloop()