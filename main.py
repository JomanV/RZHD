#TODO1: add all tables, one commit per adding one table
#TODO2: fill all tables with separate functions, one commit per filling one table with a function; perform a check after each filling with a "select * below"
#TODO3: make a select query that shows run timetables like in http://izformatika.ru/mod/assign/view.php?id=2564
#TODO4: (optional for this task) add foreign keys

import sqlite3

_file='file_RZHD.db'

create_table=[
        ['''CREATE TABLE locomotive_types
            (
            locomotive_type_id INTEGER PRIMARY KEY NOT NULL,
            type_name TEXT NOT NULL
            );'''
            , 'locomotive_types']

    ]
tables_fill={'locomotive_types':[
            ['паровоз'], 
            ['электровоз']
        ]

    }


def _create_tables():
    conn = sqlite3.connect(_file)
    for i in range(len(create_table)):
        conn.execute(create_table[i][0])
        conn.commit()
    conn.close()  

def _fill():
    conn = sqlite3.connect(_file)
    for i in range(len(tables_fill)):
        table_name=create_table[i][1]
        for j in range(len(tables_fill[table_name])):
            conn.execute('''insert into {0}(type_name) values('{1}'); '''.format(table_name,', '.join(tables_fill[table_name][j])))
            conn.commit()
    conn.close()     

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
    _fill()

from os.path import exists

if not exists('file_RZHD.db'):
    _db_init()
else: _check_tables()
    
conn = sqlite3.connect(_file)
cursor = conn.cursor()
cursor.execute('''SELECT * FROM locomotive_types;''')
print(*cursor.fetchall(),sep='\n')