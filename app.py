import tkinter as tk
from tkinter import ttk
import subprocess
import time
import csv
import pprint


def make_label_dictlist_lists(label_column_lists):
    label_dictlist_lists = []
    for column_list in label_column_lists:
        label_dictlist = []
        for text in column_list:
            label_dictlist.append({'widget_type': 'Label', 'text': text, 'context': 'label_frame'})
        label_dictlist_lists.append(label_dictlist)
    return label_dictlist_lists


def make_button_run_dictlist(filename_list):
    button_run_dictlist = []
    for filename in filename_list:
        if '.csh' in filename:
            button_run_dictlist.append({'widget_type': 'Button', 'text': 'run', 'context': 'button_frame'})
        else:
            button_run_dictlist.append({'widget_type': 'Label', 'text': '-', 'context': 'button_frame'})
    button_run_dictlist.insert(0, {'widget_type': 'Label', 'text': 'run', 'context': 'button_frame'})  # for header
    return button_run_dictlist


def make_button_edit_dictlist(filename_list):
    button_edit_dictlist = []
    for _ in range(len(filename_list)):
        button_edit_dictlist.append({'widget_type': 'Button', 'text': 'edit', 'context': 'button_frame'})
    button_edit_dictlist.insert(0, {'widget_type': 'Label', 'text': 'edit', 'context': 'button_frame'})  # for header
    return button_edit_dictlist


def create_table(container, sheet_dictlist_lists):
    sheet_frame = ttk.Frame(container)
    for c_index, sheet_dictlist_list in enumerate(sheet_dictlist_lists):
        for r_index, cell in enumerate(sheet_dictlist_list):
            cell_copied = cell.copy()
            widgt_type = cell_copied.pop('widget_type')
            context = cell_copied.pop('context')
            if widgt_type == 'Label':
                if context == 'label_frame':
                    ttk.Label(sheet_frame, **cell_copied).grid(row=r_index, column=c_index, sticky=tk.W)
                else:
                    ttk.Label(sheet_frame, **cell_copied).grid(row=r_index, column=c_index)
            elif widgt_type == 'Button':
                ttk.Button(sheet_frame, **cell_copied).grid(row=r_index, column=c_index)
    return sheet_frame


if __name__ == '__main__':
    root = tk.Tk()
    root.title('IDE')
    
    in_file = 'demo/csv/data.csv'
    #in_file = 'csvprepro/sample.csv'
    
    with open(in_file) as f:
        reader = csv.reader(f)
        
        # shape csv data
        label_row_lists = [row for row in reader]
        label_header_list = label_row_lists[0]  # ['index', 'task', 'path', 'filename']
        label_column_lists = [list(x) for x in zip(*label_row_lists)]  # transposed
        
        # for labels
        label_dictlist_lists = make_label_dictlist_lists(label_column_lists)
        
        # for buttons
        filename_list = label_column_lists[label_header_list.index('filename')][1:]  # for data.csv
        #filename_list = label_column_lists[0][1:]  # for sample.csv
        button_run_dictlist = make_button_run_dictlist(filename_list)
        button_edit_dictlist = make_button_edit_dictlist(filename_list)
        button_dictlist_lists = [button_run_dictlist] + [button_edit_dictlist]
        
        # create sheet table
        sheet_header_list = label_header_list + ['run', 'edit']
        sheet_dictlist_lists = label_dictlist_lists + button_dictlist_lists
        pprint.pprint(sheet_dictlist_lists)
        sheet_frame = create_table(root, sheet_dictlist_lists)
    
    sheet_frame.grid(row=0, column=0)
    
    root.mainloop()

