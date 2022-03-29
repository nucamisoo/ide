import tkinter as tk
from tkinter import ttk
import subprocess
import time
import csv
import pprint

def make_label_dictlist(label_column_lists):
    label_dictlist = []
    for column_list in label_column_lists:
        for text in column_list:
            label_dictlist.append({'widget_type': 'Label', 'text': text, 'context': 'label_frame'})
    return label_dictlist

def make_button_run_dictlist(filename_list):
    button_run_dictlist = []
    for filename in filename_list:
        if '.csh' in filename:
            button_run_dictlist.append({'widget_type': 'Button', 'text': 'run', 'context': 'button_frame'})
        else:
            button_run_dictlist.append({'widget_type': 'Label', 'text': '-', 'context': 'button_frame'})
    button_run_dictlist[0]['text'] = encode_header_text('run')
    return button_run_dictlist


def make_button_edit_dictlist(filename_list):
    button_edit_dictlist = []
    for _ in range(len(filename_list)):
        button_edit_dictlist.append({'widget_type': 'Button', 'text': 'edit', 'context': 'button_frame'})
    button_edit_dictlist[0]['text'] = encode_header_text('edit')
    return button_edit_dictlist


def c_indexer(h_list, txt, c_idx):
    return (h_list.index(txt), True) if txt in h_list else (c_idx, False)

def create_table(container, sheet_header_list, sheet_dictlist):
    sheet_frame = ttk.Frame(container)
    c_index = -1
    for r_index, cell in enumerate(sheet_dictlist):
        print(cell['text'])
        c_index, is_header = c_indexer(sheet_header_list, cell['text'], c_index)
        print((c_index, is_header))
        cell_copied = cell.copy()
        widgt_type = cell_copied.pop('widget_type')
        context = cell_copied.pop('context')
        if is_header:        
            ttk.Label(sheet_frame, **cell_copied).grid(row=0, column=c_index)
        else:
            if widgt_type == 'Label':
                if context == 'label_frame':
                    ttk.Label(sheet_frame, **cell_copied).grid(row=r_index+1, column=c_index, sticky=tk.W)
                else:
                    ttk.Label(sheet_frame, **cell_copied).grid(row=r_index+1, column=c_index)
            elif widgt_type == 'Button':
                ttk.Button(sheet_frame, **cell_copied).grid(row=r_index+1, column=c_index)
    return sheet_frame

    
    
def encode_header_text(text):
    return f'__:{text}:__'


if __name__ == '__main__':
    root = tk.Tk()
    root.title('IDE')
    
    with open('demo/csv/data.csv') as f:
        reader = csv.reader(f)
        label_row_lists = [row for row in reader]
        
        # ['index', 'task', 'path', 'filename']
        # -> ['__:index:__', '__:task:__', '__:path:__', '__:filename:__']
        label_header_list = label_row_lists[0]
        label_row_lists[0] = [encode_header_text(text) for text in label_header_list]
        label_header_list = label_row_lists[0]
        label_column_lists = [list(x) for x in zip(*label_row_lists)]  # transposed
        
        # for labels
        label_dictlist = make_label_dictlist(label_column_lists)
        
        # for buttons
        filename_list = label_column_lists[label_header_list.index(encode_header_text('filename'))]
        button_run_dictlist = make_button_run_dictlist(filename_list)
        button_edit_dictlist = make_button_edit_dictlist(filename_list)
        
        # create sheet table
        sheet_header_list = label_header_list + [encode_header_text('run'), encode_header_text('edit')]
        sheet_dictlist = label_dictlist + button_run_dictlist + button_edit_dictlist
        sheet_frame = create_table(root, sheet_header_list, sheet_dictlist)
    
    sheet_frame.grid(row=0, column=0)
    
    root.mainloop()

