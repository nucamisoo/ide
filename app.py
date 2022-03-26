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
    
    # Note: - foobar_list means 1d list
    #     : - foobar_lists means 2d list
    with open('demo/csv/data.csv') as f:
        reader = csv.reader(f)
        row_lists = [row for row in reader]
        column_lists = [list(x) for x in zip(*row_lists)]  # transposed
        
        column_dict = {}
        header_list = row_lists[0]
        print(header_list)
        for c_index, c_name in enumerate(header_list):
            column_dict[c_name] = column_lists[c_index][1:]
        pprint.pprint(column_dict)
        
        label_inner_frames = []
        for c_index, c_name in enumerate(header_list):
            label_inner_frames.insert(c_index, ttk.Frame(label_frame, borderwidth=1, relief='solid'))
            
            # for the table header
            ttk.Label(label_inner_frames[c_index], text=c_name).grid(row=0, column=0)
            # for the table contents
            for r_index, item in enumerate(column_dict[c_name]):
                ttk.Label(label_inner_frames[c_index], text=item).grid(row=r_index+1, column=0)
            label_inner_frames[c_index].grid(row=0, column=c_index)
        
    label_frame.grid(row=0, column=0)
                   
    root.mainloop()

