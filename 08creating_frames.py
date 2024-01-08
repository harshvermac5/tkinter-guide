import tkinter as tk

root = tk.Tk()

#adding the width x height value using geometry function
root.geometry("640x480")

#adding the title using title method
root.title("This is my Third GUI Project")

#Frame is a great way to group multiple ui elements in one go, as it need to pack at once
buttonlayout = tk.Frame(root)

#configuring the available space for the buttons based on weight
buttonlayout.columnconfigure(0, weight=1)
buttonlayout.columnconfigure(1, weight=1)
buttonlayout.columnconfigure(2, weight=1)

#Sticky function helps to grid out based on the directions
btn1 = tk.Button(buttonlayout,text="1", font=("Fira Sans", 12))
btn1.grid(row=0, column=0, sticky=tk.W+tk.E)
btn2 = tk.Button(buttonlayout,text="2", font=("Fira Sans", 12))
btn2.grid(row=0, column=1, sticky=tk.W+tk.E)
btn3 = tk.Button(buttonlayout,text="3", font=("Fira Sans", 12))
btn3.grid(row=0, column=2, sticky=tk.W+tk.E)
btn4 = tk.Button(buttonlayout,text="4", font=("Fira Sans", 12))
btn4.grid(row=1, column=0, sticky=tk.W+tk.E)
btn5 = tk.Button(buttonlayout,text="5", font=("Fira Sans", 12))
btn5.grid(row=1, column=1, sticky=tk.W+tk.E)
btn6 = tk.Button(buttonlayout,text="6", font=("Fira Sans", 12))
btn6.grid(row=1, column=2, sticky=tk.W+tk.E)
btn7 = tk.Button(buttonlayout,text="7", font=("Fira Sans", 12))
btn7.grid(row=2, column=0, sticky=tk.W+tk.E)
btn8 = tk.Button(buttonlayout,text="8", font=("Fira Sans", 12))
btn8.grid(row=2, column=1, sticky=tk.W+tk.E)
btn9 = tk.Button(buttonlayout,text="9", font=("Fira Sans", 12))
btn9.grid(row=2, column=2, sticky=tk.W+tk.E)
btnx = tk.Button(buttonlayout,text="X", font=("Fira Sans", 12))
btnx.grid(row=3, column=0, sticky=tk.W+tk.E)
btn0 = tk.Button(buttonlayout,text="0", font=("Fira Sans", 12))
btn0.grid(row=3, column=1, sticky=tk.W+tk.E)
btncall = tk.Button(buttonlayout,text="Call", font=("Fira Sans", 12))
btncall.grid(row=3, column=2, sticky=tk.W+tk.E)

#Filling as X streches out the whole to window
buttonlayout.pack()

#placing another button using text function
#we can either use the abosolute or the relaive values for height, width and size
btnrcnt = tk.Button(root, text="Recent calls", font=("Fira Sans Heavy", 18))
btnrcnt.place(relx=0.37, rely=0.5)


root.mainloop()