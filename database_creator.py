import sqlite3

class DatabaseCreators:
    def setup(self):
        conn = sqlite3.connect('persona.db')
        cursor = conn.cursor()

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS person ('
        person TEXT );
        ''')

if __name__ == "__main__":
    db = DatabaseCreators()
    db.setup