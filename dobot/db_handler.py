import sqlite3

def connect_db():
    conn = sqlite3.connect('../data/char_sheets.db')
    cursor = conn.cursor()
    return conn, cursor

def create_table():
    conn, cursor = connect_db()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS characters (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        initiative INTEGER NOT NULL,
        initiative_ad INTEGER NOT NULL DEFAULT 0
    )
    ''')
    conn.commit()
    conn.close()

def drop_table(table_name):
    conn, cursor = connect_db()
    cursor.execute(f'DROP TABLE {table_name}')
    conn.commit()
    conn.close()

def add_character(name, initiative, initiative_ad=0):
    conn, cursor = connect_db()
    cursor.execute('''
    INSERT INTO characters (name, initiative, initiative_ad)
    VALUES (?, ?, ?)
    ''', (name, initiative, initiative_ad))
    conn.commit()
    conn.close()

def get_initiative():
    conn, cursor = connect_db()
    cursor.execute('''
    SELECT name, initiative, initiative_ad
    FROM characters
    ''')
    response = cursor.fetchall()
    response = [{'name': row[0], 'initiative': row[1], 'initiative_ad': row[2]} for row in response]
    conn.close()
    return response