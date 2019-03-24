import sqlite3

class DbWriter:

    def __init__(self):
        self.my_db = 'temp.db'
        self.my_conn = None
        self.c = self.my_conn.cursor()

    def start_db(self):
        self.my_conn = sqlite3.connect(self.my_db)
        print(f"Connected to Database {self.my_db}")
        self.c.execute('''CREATE TABLE classes
                (classname text PRIMARY KEY, classats text, classme text, classre text)''')
        print("table created")

    def add_db_data(self, new_module):
        for a_class in new_module.all_my_classes:
            cn = a_class.name
            self.c.execute(f'''INSERT INTO classes VALUES
            ({cn})''')
            for an_a in a_class.all_my_attributes:
                self.c.execute(f'''INSERT INTO classes WHERE classname = '{cn}' 
                VALUES ({an_a}, null)''')
            for an_m in a_class.all_my_methods:
                self.c.execute(f'''INSERT INTO classes WHERE classname = '{cn}' 
                VALUES ( null, {an_m})''')