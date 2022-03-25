import tkinter as tk
from tkinter import ttk
import subprocess
import time

root = tk.Tk()
root.title('IDE')
root.geometry('600x400+50+50')

message = tk.Label(root, text="Table Area")
message.pack()

def button_clicked():
    print('Button clicked')
    subprocess.run(['vi', 'abc.txt'])
    time.sleep(3)
    print('You closed vi 3 seconds ago.')

button = ttk.Button(root, text='Click to open abc.txt in vi', command=button_clicked)
button.pack()

root.mainloop()

