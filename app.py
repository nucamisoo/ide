import tkinter as tk
from tkinter import ttk
import subprocess
import time
import csv
import pprint


def create_label_frame(container, row_lists):
    label_frame = ttk.Frame(container)
    for r_index, items in enumerate(row_lists):
        for c_index, item in enumerate(items):
            ttk.Label(label_frame, text=item).grid(row=r_index, column=c_index)
    return label_frame
    
    
def create_button_frame(container, filename_list):
    button_frame = ttk.Frame(container)
    
    button_header_list = ['run', 'edit']
    for c_index, c_name in enumerate(button_header_list):
        ttk.Label(button_frame, text=c_name).grid(row=0, column=c_index)
        for r_index, filename in enumerate(filename_list):
            if c_name == 'run':
                if '.csh' in filename:
                    ttk.Button(button_frame, text=c_name).grid(row=r_index+1, column=c_index)
                else:
                    ttk.Label(button_frame, text='-').grid(row=r_index+1, column=c_index)
            else:
                ttk.Button(button_frame, text=c_name).grid(row=r_index+1, column=c_index)
    
    return button_frame
    


if __name__ == '__main__':
    root = tk.Tk()
    root.title('IDE')
    #root.geometry('600x400+50+50')
    
    with open('demo/csv/data.csv') as f:
        reader = csv.reader(f)
        row_lists = [row for row in reader]
        column_lists = [list(x) for x in zip(*row_lists)]  # transposed
        
        label_frame = create_label_frame(root, row_lists)
        
        label_header_list = row_lists[0]
        filename_list = column_lists[label_header_list.index('filename')][1:]
        pprint.pprint(filename_list)
        button_frame = create_button_frame(root, filename_list)
        
        for widget in label_frame.winfo_children():
            widget.config(anchor='w', padding=[10], width=15, borderwidth=1, relief='solid')
        for widget in button_frame.winfo_children():
            widget.config(padding=[10], width=15)
            
    label_frame.grid(row=0, column=0)
    button_frame.grid(row=0, column=1)
    
    root.mainloop()

