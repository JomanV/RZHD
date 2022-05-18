#TODO1: add all tables, one commit per adding one table
#TODO2: fill all tables with separate functions, one commit per filling one table with a function; perform a check after each filling with a "select * below"
#TODO3: make a select query that shows run timetables like in http://izformatika.ru/mod/assign/view.php?id=2564
#TODO4: (optional for this task) add foreign keys

def clean_data(_dict): # proplem: after every loop length of dict decreases, so we get out of range
    if len(_dict)!=0:
        _del=[]
        for i in _dict:
            if _dict[i]=='':
                _del.append(i)
        for i in _del:
            del _dict[i]
        return _dict
    return 0

def clean_text(_text):
    return open(_text,'r').read().replace('\n','').replace('\t','')

import sqlite3
from Integrity_check import *

file_name='file_RZHD.db'

a=clean_text('tables_and_creation_code.txt')
b=clean_text('tables_fill.txt')

tb_creation_dict=clean_data(eval(a))
tb_fill_dict=clean_data(eval(b))

if len(tb_fill_dict)!=0 and len(tb_creation_dict)!=0:
    integrity_check(file_name,tb_creation_dict,tb_fill_dict)

    conn = sqlite3.connect(file_name)
    cursor = conn.cursor()
    cursor.execute('''
    SELECT * FROM locomotive_types;
    ''')

    print(*cursor.fetchall(),sep='\n')

print(*tb_fill_dict,'\n',*tb_creation_dict,sep='\n')
