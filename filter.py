from exchangelib import DELEGATE, Account, Credentials, Configuration, Message
from exchangelib.folders import Inbox, DeletedItems
import re
import sqlite3

def get_subscribed_emails():
    conn = sqlite3.connect('subscriptions.db')
    cursor = conn.cursor()
    cursor.execute('SELECT email FROM subscriptions')
    subscribed_emails = [row[0] for row in cursor.fetchall()]
    conn.close()
    return subscribed_emails


def connect_to_exchange(username, password):
    credentials = Credentials(username, password)
    account = Account(username, credentials=credentials, autodiscover=True, access_type=DELEGATE)
    return account

def fetch_emails(account, subscribed_emails):
    inbox = account.inbox.all()
    for item in inbox:
        from_ = item.author.email_address
        if from_:
            if from_ not in subscribed_emails and check_if_spam(item):
                item.move(account.trash)
            else:
                print(f'Legitimate email from: {from_}')

def check_if_spam(item):
    spam_keywords = ['win money' 'claim your prize', 'urgent']
    subject = item.subject
    for keyword in spam_keywords:
        if re.search(keyword, subject, re.IGNORECASE):
            return True
        return False

def main():
    username = 'email.com'



