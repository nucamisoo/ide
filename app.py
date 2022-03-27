import tkinter as tk
from tkinter import ttk
import subprocess
import time
import csv
import pprint


def make_label_dict(label_headered_column_lists):
    label_dict = {}
    for column_list in label_headered_column_lists:
        label_dict[column_list[0]] = [{'widget_type': 'Label', 'text': text} for text in column_list[1:]]
    return label_dict
    
    
def make_btn_run_cell_dlist(filename_list):
    btn_run_cell_dlist = []
    for filename in filename_list:
        if '.csh' in filename:
            btn_run_cell_dlist.append({'widget_type': 'Button', 'text': 'run'})
        else:
            btn_run_cell_dlist.append({'widget_type': 'Label', 'text': '-'})
    return btn_run_cell_dlist


def make_btn_edit_cell_dlist(filename_list):
    btn_edit_cell_dlist = []
    for _ in range(len(filename_list)):
        btn_edit_cell_dlist.append({'widget_type': 'Button',
                                    'text': 'edit'})
    return btn_edit_cell_dlist
    

def create_table(container, all_header_list, sheet_dict):
    sheet_frame = ttk.Frame(container)
    for c_index, c_name in enumerate(all_header_list):
        ttk.Label(sheet_frame, text=c_name).grid(row=0, column=c_index)
        for r_index, cell in enumerate(sheet_dict[c_name]):
            cell_copied = cell.copy()
            widgt_type = cell_copied.pop('widget_type')
            if widgt_type == 'Label':
                ttk.Label(sheet_frame, **cell_copied).grid(row=r_index+1, column=c_index)
            elif widgt_type == 'Button':
                ttk.Button(sheet_frame, **cell_copied).grid(row=r_index+1, column=c_index)
    return sheet_frame
    

if __name__ == '__main__':
    root = tk.Tk()
    root.title('IDE')
    
    with open('demo/csv/data.csv') as f:
        reader = csv.reader(f)
        
        # make data for label(_frame)
        label_row_lists = [row for row in reader]
        label_header_list = label_row_lists[0]  # ['index', 'task', 'path', 'filename']
        label_headered_column_lists = [list(x) for x in zip(*label_row_lists)]  # transposed
        
        label_dict = make_label_dict(label_headered_column_lists)
            
        # for button
        filename_list = label_headered_column_lists[label_header_list.index('filename')][1:]
        button_dict = {}
        button_dict['run'] = make_btn_run_cell_dlist(filename_list)
        button_dict['edit'] = make_btn_edit_cell_dlist(filename_list)
        button_header_list = ['run', 'edit']
        
        # create table
        sheet_header_list = label_header_list + button_header_list
        sheet_dict = {**label_dict, **button_dict}
        
        sheet_frame = create_table(root, sheet_header_list, sheet_dict)
    
    sheet_frame.grid(row=0, column=0)
    
    root.mainloop()

