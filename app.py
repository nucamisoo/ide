import tkinter as tk
from tkinter import ttk
import subprocess
import time
import csv
import pprint


class Table(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.column_frames = []
        
    def create_table(self, column_dict, header_list, widget_type):
        for c_index, c_name in enumerate(header_list):
            self.column_frames.insert(c_index, ttk.Frame(self, borderwidth=1, relief='solid'))
            # for header
            ttk.Label(self.column_frames[c_index], text=c_name).grid(row=0, column=0)
            # for contents
            for r_index, item in enumerate(column_dict[c_name]):
                if widget_type == 'Label':
                    ttk.Label(self.column_frames[c_index], text=item).grid(row=r_index+1, column=0)
                elif widget_type == 'Button':
                    ttk.Button(self.column_frames[c_index], text=item).grid(row=r_index+1, column=0)
            self.column_frames[c_index].grid(row=0, column=c_index)
        return self


if __name__ == '__main__':
    root = tk.Tk()
    root.title('IDE')
    #root.geometry('600x400+50+50')
    
    label_frame = ttk.Frame(root)
    button_frame = ttk.Frame(root)
    
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
        
        C_FILENAME = header_list[3]
        button_header_list = ['run', 'edit']
        button_column_dict = {
            'run': [ 'run' if '.csh' in filename else '-' for filename in column_dict[C_FILENAME] ],
            'edit': [ 'edit' for _ in column_dict[C_FILENAME] ]
            }
        
        
        params = [[label_frame, column_dict, header_list, 'Label'],
                  [button_frame, button_column_dict, button_header_list, 'Button']]
        
        for param in params:
            table = Table(param[0])
            table.create_table(*param[1:])
            table.grid(row=0, column=0)
            
        
    label_frame.grid(row=0, column=0)
    button_frame.grid(row=0, column=1)
                   
    root.mainloop()

