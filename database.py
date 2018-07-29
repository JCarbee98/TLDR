import sqlite3
import os.path

if not os.path.isfile('main.db'):
    maindb = sqlite3.connect('main.db')
    maindb.execute('''create table accounts (atname text)''')
else:
    db = sqlite3.connect('main.db')
maindb = db.cursor()
maindb.execute('''create table twitacct (atname text,time)''')
maindb.execute('''create table rposts (title text, rlinx text,category text)''')

def addtuser(usrname):
    maindb.execute("insert into twitacct values(?) ", (usrname,))
    db.commit()
def addrpost (title,link,category):
    maindb.execute("insert into rposts values (?,?,?)",(title,link,category))
    db.commit()
def getrpost(category):

def printusr(usrname):
    maindb.execute("select * from twitacct where atname=:uname", {"uname": usrname})
    print(maindb.fetchone())

