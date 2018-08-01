import sqlite3
import os.path

if not os.path.isfile('main.db'):
    maindb = sqlite3.connect('main.db')
    maindb.execute('''create table accounts (atname text)''')
    maindb.execute('''create table twitacct (atname text,time)''')
    maindb.execute('''create table rposts (title text, rlinx text,category text)''')
    db = sqlite3.connect('main.db')
    maindb = db.cursor()

else:

    db = sqlite3.connect('main.db')
    maindb=db.cursor()
def addtuser(usrname,time):
    maindb.execute("insert into twitacct values(?,?) ", (usrname,time))
    db.commit()
def addrpost (title,link,category):
    maindb.execute("insert into rposts values (?,?,?)",(title,link,category))
    db.commit()
def getrpost(category):
    maindb.execute("select * from rposts where category=:category order by random() LIMIT 1", {"category": category})
    rlist=[]
    rows=maindb.fetchall()
    for row in rows:
        title,link,category=row
        rlist.extend((title,link,category))
    return rlist
def printusr(usrname):
    maindb.execute("select * from twitacct where atname=:uname", {"uname": usrname})
    print(maindb.fetchone())
def returnsubs():
    maindb.execute("select distinct categories from rposts")
    rlist = []
    rows = maindb.fetchall()
    for row in rows:
        rlist.extend(row)
    return rlist
def clearposts():
    maindb.execute("delete from rposts")
    db.commit()
