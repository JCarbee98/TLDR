import sqlite3
import os.path

'''if not os.path.isfile('main.db'):
    maindb = sqlite3.connect('main.db')
    maindb.execute(create table accounts (atname text))
else:'''
db = sqlite3.connect('main.db')
maindb = db.cursor()
maindb.execute('''create table accounts (atname text)''')


def adduser(usrname):
    maindb.execute("insert into accounts values(?) ", (usrname,))
    db.commit()


def printusr(usrname):
    maindb.execute("select * from accounts where atname=:uname", {"uname": usrname})
    print(maindb.fetchone())
