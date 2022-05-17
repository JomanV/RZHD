#TODO1: add all tables, one commit per adding one table
#TODO2: fill all tables with separate functions, one commit per filling one table with a function; perform a check after each filling with a "select * below"
#TODO3: make a select query that shows run timetables like in http://izformatika.ru/mod/assign/view.php?id=2564
#TODO4: (optional for this task) add foreign keys

import sqlite3

_file='file_RZHD.db'

create_table={'locomotive_types':
         '''CREATE TABLE locomotive_types
            (
            locomotive_type_id INTEGER PRIMARY KEY NOT NULL,
            type_name TEXT NOT NULL
            );'''

    }
tables_fill={'locomotive_types':[
            ['Паровоз'], 
            ['Тепловоз'],
            ['Электровоз']
        ]

    }
    
    

def _create_tables():
    conn = sqlite3.connect(_file)
    for i in create_table:
        conn.execute(crate_table[i])
        conn.commit()
    conn.close()  
    
def _fill_table(table, conn):
    for j in range(len(tables_fill[table])):
        conn.execute('''insert into {0}(type_name) values('{1}'); '''.format(table,', '.join(tables_fill[table][j])))
        conn.commit()

def _fill_tables():
    conn = sqlite3.connect(_file)
    for i in tables_fill:
        _fill_table(i, conn)
    conn.close()     

def _check_change(): 
    conn = sqlite3.connect(_file)
    for table_name in tables_fill:
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM {};'''.format(table_name))        
        table_values=cursor.fetchall()
        
        _len=len(tables_fill[table_name])
        if _len != len(table_values) or _len > 0:
            return True
        for j in range(_len):
            if ', '.join(table_values[j][1:]) != ', '.join(tables_fill[table_name][j]):#possible error: the order is not guaranteed to stay the same
                return True
        return False
                
def _check_tables():
    conn = sqlite3.connect(_file)
    cursor = conn.cursor()
    cursor.execute('''
    SELECT name FROM sqlite_master WHERE type='table';''')
    res = cursor.fetchall()
    print(*res)
    
def _db_init():    
    _create_tables()
    _check_tables()
    _fill_tables()

def _erase_table(table):
    conn = sqlite3.connect(_file)
    for i in tables_fill:
        cursor = conn.cursor()
        cursor.execute('''DROP TABLE {};'''.format(i)) 

def _erase_tables():
    conn = sqlite3.connect(_file)
    for i in tables_fill:
        _erase_table(i)
    conn.close() 

from os.path import exists

if not exists(_file):
    _db_init()
elif _check_change():
    _erase_tables()
    _db_init()
    
else:
    _check_tables()
    
conn = sqlite3.connect(_file)
cursor = conn.cursor()
cursor.execute('''SELECT * FROM locomotive_types;''')
print(*cursor.fetchall(),sep='\n')