import sqlite3

def get_subscribed_emails():
    conn = sqlite3.connect('subscriptions.db')
    cursor = conn.cursor()
    cursor.execute('SELECT email FROM subscriptions')
    subscribed_emails = [row[0] for row in cursor.fetchall()]
    conn.close()
    return subscribed_emails

