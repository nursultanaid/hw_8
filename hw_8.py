import sqlite3

def create_connection(db_name):
    conn = None
    try:
        conn = sqlite3.connect(db_name)
    except sqlite3.Error as e:
        print(e)
    return conn

def create_table(conn, sql):
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
    except sqlite3.Error as e:
        print(e)
    return conn

def insert_data(conn, sql, data):
    try:
        cursor = conn.cursor()
        cursor.executemany(sql, data)
        conn.commit()
    except sqlite3.Error as e:
        print(e)

sql_create_students_table = '''
CREATE TABLE students(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXXT NOT NULL,    
    last_name TEXT NOT NULL,
    city_id INTEGER,    
    FOREIGN KEY (city_id) REFERENCES cities (id)
    )'''

sql_to_create_cities_table = '''
    CREATE TABLE IF NOT EXISTS cities(    
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,    
    area REAL DEFAULT 0,
    country_id INTEGER,    
    FOREIGN KEY (country_id) REFERENCES countries (id)
    )'''

sql_to_create_countries_table = '''
    CREATE TABLE IF NOT EXISTS countries(    
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL    )
'''

sql_insert_students_data = '''
INSERT INTO students (first_name, last_name, city_id) VALUES (?,?,?)
'''

sql_insert_countries_data = '''
INSERT INTO countries (title) VALUES (?)
'''

sql_insert_cities_data = '''
INSERT INTO cities (title, country_id) VALUES (?, ?)
'''

cities_data = [('New-York', 1), ('Los_Angeles', 1), ('Paris', 2), ('Toulouse', 2), ('Milan', 3), ('Rome', 3), ('Venice', 3)]
countries_data = [('USA',), ('France',), ('Italy',)]
students_data = [
    ('Nursultan', 'Aidarbekov', 1),
    ('John', 'Doe', 1),
    ('Mike', 'John', 2),
    ('Mitt', 'Rose', 3),
    ('Will', 'Smith', 2),
    ('Amber', 'Miles', 3),
    ('Close', 'Miroslav', 2),
    ('Ali', 'Owairan', 2),
    ('Jenny', 'Ben', 2),
    ('Wilson', 'Son', 1),
    ('Nui', 'Anderson', 3),
    ('Lois', 'Vuitton', 2),
    ('Peter', 'Griffin', 1),
    ('Rui', 'Patrik', 1),
    ('Sam', 'Dorris', 3),
    ('Michael', 'Cors', 1),
]


connection = create_connection('hw_8.db')
if connection is not None:
    print('Successfully connected')
    # create_table(connection, sql_create_students_table)
    # insert_data(connection, sql_insert_students_data, students_data)

    # create_table(connection, sql_to_create_countries_table)
    # insert_data(connection, sql_insert_countries_data, countries_data)

    # create_table(connection, sql_to_create_cities_table)
    # insert_data(connection, sql_insert_cities_data, cities_data)

    connection.close()