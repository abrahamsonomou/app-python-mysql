from EntityUser import *
from service import *
import hashlib

# db.insert('Saolomou','user6','user1','user1.png',1)
class Fenetre_User:
    def __init__(self,root):
        self.root=root
        self.root.title("Details users")
        self.root.geometry("1200x700")
        self.root.minsize(width=1200,height=700)
        self.root.maxsize(width=1200,height=700)

        #declaration des variables
        self.r=StringVar()
        self.id_users=StringVar()
        self.users_name=StringVar()
        self.users_login=StringVar()
        self.users_passwd=StringVar()
        self.users_passwdConfirm=StringVar()
        self.role_user=StringVar()

        self.fontLabel="times new roman",12,"bold"
        self.fontEntry="times new roman",12,"bold"

        wrapper1=LabelFrame(self.root,text="Liste des Users",bg="white")
        wrapper2=LabelFrame(self.root,text="Zone de recherche",bg="white")
        wrapper3=LabelFrame(self.root,text="Detail d'un User",bg="white")

        wrapper1.pack(fill="both",expand="yes",padx=20,pady=10)
        wrapper2.pack(fill="both",expand="yes",padx=20,pady=10)
        wrapper3.pack(fill="both",expand="yes",padx=20,pady=10)

        #entete du tableau
        self.trv=ttk.Treeview(wrapper1,columns=(1,2,3,4,5,6),show="headings",height="8")
        self.trv.pack()
        s=ttk.Style(wrapper1)
        s.theme_use("clam")
        s.configure(".",font=('Helvetiva',11))
        s.configure("Treeview.Heading",foreground='#562',font=('Helvetiva',12,"bold"))
        self.trv.pack()
        self.trv['columns']=(1,2,3,4,5,6)
        self.trv.column(1,width=90,minwidth=5,anchor=CENTER)
        self.trv.column(2,width=200,minwidth=5,anchor=CENTER)
        self.trv.column(3,width=200,minwidth=5,anchor=CENTER)
        self.trv.column(4,width=200,minwidth=5,anchor=CENTER)
        self.trv.column(5,width=180,minwidth=5,anchor=CENTER)
        self.trv.column(6,width=190,minwidth=5,anchor=CENTER)

        #definition de l'entete du tableau
        self.trv.heading(1,text="ID user")
        self.trv.heading(2,text="Username")
        self.trv.heading(3,text="Login")
        self.trv.heading(4,text="Password")
        self.trv.heading(5,text="Role")
        self.trv.heading(6,text="Date de creation")

        #Selection d'une ligne du tableau
        self.trv.bind('<Double 1>', self.getrow)


        # scrollbar=Scrollbar(wrapper1)
        # scrollbar.pack()

        #Section recherche d'un user
        self.lblrecherche=Label(wrapper2,text="Recherche")
        self.lblrecherche.pack(side=LEFT,padx=10)

        self.entRech=Entry(wrapper2,textvariable=self.r)
        self.entRech.pack(side=LEFT,padx=6)

        #le bouton recherche
        btn=Button(wrapper2,text="Search",command=self.search)
        btn.pack(side=LEFT,padx=6)

        #le bouton clear
        cbtn=Button(wrapper2,text="Effacer",command=self.effacer)
        cbtn.pack(side=LEFT,padx=6)

        #Section detail d'un user
        #champ ID user
        self.lblId=Label(wrapper3,text="ID user",font=self.fontLabel,bg="white")
        self.lblId.grid(row=0,column=0,padx=5,pady=3)
        self.entId=Entry(wrapper3,textvariable=self.id_users,state="readonly",font=self.fontEntry)
        self.entId.grid(row=0,column=1,padx=5,pady=3)

         #champ username
        self.lbluserName=Label(wrapper3,text="Username",compound=LEFT,font=self.fontLabel,bg="white")
        self.lbluserName.grid(row=1,column=0,pady=10,padx=20)
        self.entUserName=Entry(wrapper3,textvariable=self.users_name,bd=5,relief=GROOVE,font=self.fontEntry)
        self.entUserName.grid(row=1,column=1,padx=5,pady=3) 

        #champ login
        self.lblLogin=Label(wrapper3,text="Login",compound=LEFT,font=self.fontLabel,bg="white")
        self.lblLogin.grid(row=2,column=0,padx=5,pady=3)
        self.entLogin=Entry(wrapper3,textvariable=self.users_login,bd=5,relief=GROOVE,font=self.fontEntry)
        self.entLogin.grid(row=2,column=1,padx=5,pady=3)

        #champ Create Date
        # self.lblDateCreate=Label(wrapper3,text="Create Date",compound=LEFT,font=self.fontLabel,bg="white")
        # self.lblDateCreate.grid(row=4,column=0,padx=5,pady=3)
        # self.entDateCreate=Entry(wrapper3,textvariable=self.dates_create,bd=5,relief=GROOVE,font=self.fontEntry)
        # self.entDateCreate.grid(row=4,column=1,padx=5,pady=3)

        #champ role
        self.lblRole=Label(wrapper3,text="Role",compound=LEFT,font=self.fontLabel,bg="white")
        self.lblRole.grid(row=5,column=0,padx=5,pady=3)

        self.comboRole=ttk.Combobox(wrapper3,textvariable=self.role_user,width=18,font=self.fontEntry)
        self.comboRole['values']=[0,1]
        self.comboRole.grid(row=5,column=1,padx=5,pady=3)
        self.comboRole.current(1)

        self.lblpass=Label(wrapper3,text="Password",compound=LEFT,font=self.fontLabel,bg="white")
        self.lblpass.grid(row=6,column=0,pady=10,padx=20)
        self.entPass=Entry(wrapper3,textvariable=self.users_passwd,bd=5,relief=GROOVE,font=self.fontEntry,show="*")
        self.entPass.grid(row=6,column=1,padx=5,pady=3)

        self.lblConfirm=Label(wrapper3,text="Confirm",compound=LEFT,font=self.fontLabel,bg="white")
        self.lblConfirm.grid(row=7,column=0,pady=10,padx=20)
        self.entConfirm=Entry(wrapper3,textvariable=self.users_passwdConfirm,bd=5,relief=GROOVE,font=self.fontEntry,show="*")
        self.entConfirm.grid(row=7,column=1,padx=5,pady=3)

        #bouton add new
        add_btn=Button(wrapper3,text="Add New",command=self.add_item)
        add_btn.grid(row=9,column=2,padx=5,pady=3)

        #bouton update
        upd_btn=Button(wrapper3,text="Update",command=self.update_item)
        upd_btn.grid(row=9,column=3,padx=5,pady=3)

        #bouton delete
        del_btn=Button(wrapper3,text="Delete",command=self.delete_item)
        del_btn.grid(row=9,column=4,padx=5,pady=3)
    
        #bouton delete
        cls_btn=Button(wrapper3,text="Effacer",command=self.clear)
        cls_btn.grid(row=9,column=5,padx=5,pady=3)

    def clear(self):
        self.entUserName.delete(0,END)  
        self.entLogin.delete(0,END)  
        self.entPass.delete(0,END)  
        self.entConfirm.delete(0,END)  
    
    def add_item(self):
        user_name=self.users_name.get()
        user_login=self.users_login.get()
        user_passwd=self.users_passwd.get()
        confirm=self.users_passwdConfirm.get()
        role=self.role_user.get()
        if(user_name and user_login and user_passwd and confirm):
            if (user_passwd==confirm):
                listel=db.listelogins()
                if (user_login in listel):
                        messagebox.showerror("Ce login exist","veullez changer le login")
                else:
                    pw=hashlib.sha1(user_passwd.encode()).hexdigest()
                    user=User(user_name,user_login,pw,role) 
                    if messagebox.askyesno("Confirm please","Are you sure you want to add this user ?"):
                        db.insertUser(user)
                        self.effacer()
                        self.clear()
                    else:
                        return True
            else:
                messagebox.showerror("Erreur","Password non identique")
        else:
            messagebox.showerror("Insertion impossible","Veuillez remplir tous les champs")

    def delete_item(self):
        id_user=self.id_users.get()
        if (id_user==""):
            messagebox.showerror("Suppression impossible","Le champ ID user est vide. Veuillez selectionner un enregistrement")
        else:
            if messagebox.askyesno("confirm delete","Are you sure you want to delete this user ?"):
                db.removeUser(id_user)
                self.effacer()
                self.clear()
            else:
                return True  
    
    def update_item(self):
        id_user=self.id_users.get()
        user_name=self.users_name.get()
        user_login=self.users_login.get()
        user_passwd=self.users_passwd.get()
        role=self.role_user.get()
       
        if (id_user==""):
            messagebox.showerror("Mises a jour impossible","Le champ ID user est vide. Veuillez selectionner un enregistrement")
        else:
            if messagebox.askyesno("Confirm please","Are you sure you want to update this user ?"):
              db.updateUser(id_user,user_name,user_login,user_passwd,role)
              self.effacer()
              self.clear()
            else:
                return True

    def search(self):
        param=self.r.get()
        if (param==""):
            messagebox.showerror("Recherche impossible","Veuillez donner un critere")
        else:
            rows=db.searchUser(param)
            self.update(rows)
            
    def effacer(self):
        rows=db.fetchUsers()
        self.update(rows)
        self.r.set("")

    #definition de la methode update de la liste
    def update(self,rows):
        self.trv.delete(*self.trv.get_children())
        if (len(rows)):
            for i in rows:
                self.trv.insert('',"end",values=i)

    def getrow(self,event):
        rowid=self.trv.identify_row(event.y)
        self.item=self.trv.item(self.trv.focus())
        self.id_users.set(self.item['values'][0])
        self.users_name.set(self.item['values'][1])
        self.users_login.set(self.item['values'][2])
        self.role_user.set(self.item['values'][4])
        self.users_passwd.set(self.item['values'][3])
        self.users_passwdConfirm.set(self.item['values'][3])

    def remplissage(self):
        rows=db.fetchUsers()
        self.update(rows)

def fenUser():
    root=Tk()
    obj=Fenetre_User(root)
    obj.remplissage()
    root.mainloop()

fenUser()








