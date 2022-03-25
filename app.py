import tkinter as tk
from tkinter import ttk
import subprocess
import time
import csv


#def button_clicked():
#    print('Button clicked')
#    subprocess.run(['vi', 'abc.txt'])
#    time.sleep(3)
#    print('You closed vi 3 seconds ago.')


if __name__ == '__main__':
    root = tk.Tk()
    root.title('IDE')
    #root.geometry('600x400+50+50')
    
    #message = tk.Label(root, text="Table Area")
    #message.pack()
    
    #button = ttk.Button(root, text='Click to open abc.txt in vi', command=button_clicked)
    #button.pack()
    
    
    with open('demo/csv/data.csv') as f:
        lines = csv.reader(f)
        for row, items in enumerate(lines):
            for column, item in enumerate(items):
                label = ttk.Label(root, text=item)
                label.grid(row=row, column=column)
                
                   
    root.mainloop()

