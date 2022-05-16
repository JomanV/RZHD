#TODO1: add all tables, one commit per adding one table
#TODO2: fill all tables with separate functions, one commit per filling one table with a function; perform a check after each filling with a "select * below"
#TODO3: make a select query that shows run timetables like in http://izformatika.ru/mod/assign/view.php?id=2564
#TODO4: (optional for this task) add foreign keys

import sqlite3

create_table=[]
tables_fill=[]


def _create_tables():
    conn = sqlite3.connect('railways.db')
    for i in range(len(create_table)):
        conn.execute(create_table[i][0])
        conn.commit()
    conn.close()  

def _fill():
    conn = sqlite3.connect('railways.db')
    conn.execute()
    conn.commit()
    conn.close()     

def _check_tables():
    conn = sqlite3.connect('railways.db')
    cursor = conn.cursor()
    cursor.execute('''
    SELECT name FROM sqlite_master WHERE type='table';''')
    res = cursor.fetchall()
    for r in res:
        print(r)
    
def _db_init():    
    _create_tables()
    _check_tables()
     #_fill()

from os.path import exists

if not exists('railways.db'):
    _db_init()

#fill_locomotive_types()
conn = sqlite3.connect('railways.db')
cursor = conn.cursor()

cursor.execute()
res = cursor.fetchall()

for r in res:
    print(r)
