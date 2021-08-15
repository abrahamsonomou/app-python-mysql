import mysql.connector as mysql
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class Database:
    def __init__(self,host,user,passwd,db):
        self.conn=mysql.connect(
            host=host,
            user=user,
            passwd=passwd,
            database=db)
        self.curseur=self.conn.cursor()
    
    #Entity User
    listlogins=[]
    listeComptLogin=[]
    listeComptPass=[]

    def fetchUsers(self):
        self.curseur.execute("SELECT * FROM users ")
        rows=self.curseur.fetchall()
        return rows

    def insertUser(self,user):
        query=("INSERT INTO users\
                        values(null,%s,%s,%s,%s,null)")
        self.curseur.execute(query,(user.username,user.login,user.password,user.role))
        self.conn.commit()

    def removeUser(self,id):
        query=("DELETE from users where id_user="+id)
        self.curseur.execute(query)
        self.conn.commit()

    def updateUser(self,id,username,login,password,role):
        query="UPDATE users set\
                    username=%s,\
                    login=%s,\
                    password=%s,\
                    role=%s\
                    where id_user=%s"
        self.curseur.execute(query,(username,login,password,role,id))
        self.conn.commit()

       #add in liste login
    def listelogins(self):
        query="SELECT login FROM users "
        self.curseur.execute(query)
        rows=self.curseur.fetchall()
        listLogin=[]
        for i in rows:
            listLogin.append(i)

        for i in listLogin:
            self.listlogins.append(i[0])
        return self.listlogins
        
    def searchUser(self,param):
        query="SELECT * FROM users where\
                id_user like '%"+param+"%'\
                or username like '%"+param+"%'\
                or login like '%"+param+"%'\
                or password like '%"+param+"%'\
                or role like '%"+param+"%'\
                or date_create like '%"+param+"%'"
        self.curseur.execute(query)
        rows=self.curseur.fetchall()
        return rows

    def __del__(self):
        self.conn.close()

host="localhost"
user="root"
passwd=""
database="db"
db=Database(host,user,passwd,database)
# db.insert('Saolomou','user2','user1','user1.png',1)

# print(db.fetch())
    