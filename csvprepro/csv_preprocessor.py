import csv
import pprint
import re

#
# Under construction
# No longer necessary
#

def preprocessor(raw_lines, num, raw_line, idx, item):
    if item.count('"') % 2:
        if idx == len(raw_line)-1:
            item_newlined = raw_lines[num+1].pop(0)
            if item_newlined.endswith('"') and len(raw_lines):
                return preprocessor(raw_lines, num+1, raw_line, idx, item)
            else:
                return f'{item}\n{item_newlined}'
        else:
            item_separated = raw_line.pop(idx+1)
            if item_separated.endswith('"'):
                return preprocessor(raw_lines, num, raw_line, idx, item)
            else:
                return f'{item},{item_separated}'
    return item


with open('sample.csv', newline='', encoding='utf_8') as f:
    reader = csv.reader(f, delimiter=',', doublequote=True, escapechar=None, quotechar='"', skipinitialspace=False)
    raw_lines = [row for row in reader]
    
    pprint.pprint(raw_lines)
    
    print('+--+--+')
    
    lines = []
    for num, raw_line in enumerate(raw_lines):
        line = []
        for idx, item in enumerate(raw_line):
            if '"' in item:
                item = preprocessor(raw_lines, num, raw_line, idx, item)
                line.append(item[1:-1].replace('""', '"'))
            else:
                line.append(item)
        lines.append(line)
        
    pprint.pprint(lines)

