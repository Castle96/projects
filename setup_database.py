import sqlite3

def setup_database():
    conn = sqlite3.connect('subscriptions.db')
    cursor = conn.cursor()
    cursor.execute(''' CREATE TABLE IF NOT EXISTS subscriptions ( id INTEGER PRIMARY KEY AUTOINCREMENT,
                email TEXT NOT NULL ) ''')
    conn.commit()
    conn.close()


    if __name__ == "__main__":
        setup_database
