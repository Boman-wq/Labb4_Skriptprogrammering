import sqlite3

class DataBase():
    def create_table(self):
        """Create a database table"""
        # Connect to database
        conn = sqlite3.connect(self)
        # Create a cursor
        c = conn.cursor()

        # Create a Table
        c.execute("""CREATE TABLE weather (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        sensor text,
        location text,
        temperature real,
        description text,
        time text
        )""")
        # Commit our command
        conn.commit()
        # Close our connection
        conn.close()
