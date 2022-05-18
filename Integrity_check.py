import sqlite3
from os.path import exists


def create_table(file_name,code_tb_creation_dict):

    conn = sqlite3.connect(file_name)
    conn.execute(code_tb_creation_dict)
    conn.commit()
    conn.close()

def create_tables(file_name,tb_in_file,tb_creation_dict):

    for tb_name in tb_creation_dict:
        if tb_name not in tb_in_file:
            create_table(file_name,tb_creation_dict[tb_name])

def check_tb_existence(file_name,tb_creation_dict):

    conn = sqlite3.connect(file_name)
    cursor = conn.cursor()
    cursor.execute('''
    SELECT name FROM sqlite_master WHERE type='table';''')
    res = cursor.fetchall()
    if len(res) == 0: create_tables(file_name,res,tb_creation_dict)

def fill_tb(file_name,tb_name,columns,values):

    conn = sqlite3.connect(file_name)
    for value in values:
        conn.execute(f'''insert into {tb_name}({columns}) values( {', '.join(map(lambda x: "'"+str(x)+"'",value) )}); ''')
        conn.commit()
    conn.close() 

def columns_tb(file_name,tb_name):

    connection = sqlite3.connect(file_name)
    cursor = connection.cursor()
    cursor.execute('PRAGMA table_info({})'.format(tb_name))
    f=cursor.fetchall()
    name=[]
    for i in range(len(f)):  name.append(f[i][1])
    return name[1:]

def erase_tb(file_name,tb_name):

    conn = sqlite3.connect(file_name)
    cursor = conn.cursor()
    cursor.execute(f'''DROP TABLE {tb_name};''')

def check_fill_tb(file_name,tb_name, values):

    connection = sqlite3.connect(file_name)
    cursor = connection.cursor()
    cursor.execute(f'select * from {tb_name};)')
    f=cursor.fetchall()

    if len(f)!=len(values): 
        erase_tb(file_name,tb_name)
        return True

    for i in range(len(f)):
        if sorted(f[i][1:]) != sorted(values[i]):
            erase_tb(file_name,tb_name)
            return True
    return False

def fill_tbs(file_name,tb_fill_dict):

    for tb_name in tb_fill_dict:
        if check_fill_tb(file_name,tb_name,tb_fill_dict[tb_name]):   
            columns=columns_tb(file_name,tb_name)
            fill_tb(file_name,tb_name,columns,tb_fill_dict[tb_name])

def integrity_check(file_name,tb_creation_dict,tb_fill_dict):

    if len(tb_creation_dict)==0 or len(tb_fill_dict)==0:
        print('Empty file')
    else:
        check_tb_existence(file_name,tb_creation_dict)

        conn = sqlite3.connect(file_name)
        cursor = conn.cursor()
        cursor.execute('''
        SELECT name FROM sqlite_master WHERE type='table';''')
        print(cursor.fetchall())

        fill_tbs(file_name,tb_fill_dict)