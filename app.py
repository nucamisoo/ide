import tkinter as tk
from tkinter import ttk
import subprocess
import time
import csv
import pprint


if __name__ == '__main__':
    root = tk.Tk()
    root.title('IDE')
    #root.geometry('600x400+50+50')
    
    label_frame = ttk.Frame(root)
    #button_frame = ttk.Frame(root)
    
    with open('demo/csv/data.csv') as f:
        reader = csv.reader(f)
        lines = [line for line in reader]
        lines_t = [list(x) for x in zip(*lines)]  # transposed
        
        label_inner_frames = []
        #button_inner_frames = []
        for column, items in enumerate(lines_t):
            # for labels
            label_inner_frames.insert(column, ttk.Frame(label_frame, borderwidth=1, relief='solid'))
            for row, item in enumerate(items):
                ttk.Label(label_inner_frames[column], text=item).grid(row=row, column=0)
            label_inner_frames[column].grid(row=0, column=column)
            
            # for buttons(not working)
            #for column, btn in enumerate(['run', 'edit'])
            #    button_inner_frames.insert(column, ttk.Frame(button_frame))
            #    if '.csh' in item:
            #        ttk.Button(button_inner_frames[column], text='run').grid(row=row, column=0)
            #    ttk.Button(button_inner_frames[column], text='edit').grid(row=row, column=1)
            #button_inner_frames[column].grid(row=0, column=column)
        
    label_frame.grid(row=0, column=0)
    #button_frame.grid(row=0, column=1)
                   
    root.mainloop()

