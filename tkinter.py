import tkinter as tk

root = tk.Tk()                 # create window
root.title("My GUI")           # title

label = tk.Label(root, text="Hello World")  # create label
label.pack()

button = tk.Button(root, text="Click Me")   # create button
button.pack()

root.mainloop()                # run GUI