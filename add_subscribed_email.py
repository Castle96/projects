import sqlite3

def add_subscribed_email(email):
    conn = sqlite3.connect('subscriptions.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO subscriptions (email) VALUES (?)' , (email, ))
    conn.commit()
    conn.close()

if __name__ == "__main__":

    add_subscribed_email('example@domain.com')
