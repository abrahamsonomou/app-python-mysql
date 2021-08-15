from datetime import datetime


class User():
    def __init__(self,username,login,password,role):
        self._id=0
        self._username=username
        self._login=login
        self._password=password
        self._role=role
        self._date_create=datetime.now()
    
    def _getId(self):
        return self._id

    def _setId(self,newId):
        self._id=newId

    def _getUsername(self):
        return self._username

    def _setUsername(self,newUsername):
        self._username=newUsername

    def _getLogin(self):
        return self._login

    def _setLogin(self,newLogin):
        self._login=newLogin

    def _getPassword(self):
        return self._password
    
    def _setPassword(self,newPassword):
        self._password=newPassword

    def _getRole(self):
        return self._role
    
    def _setRole(self,newRole):
        self._role=newRole

    def _getDateCreate(self):
        return self._datecreate
    
    def _setDateCreate(self,newDateCreate):
        self._datecreate=newDateCreate

    id_user=property(_getId,_setId)
    username=property(_getUsername,_setUsername)
    login=property(_getLogin,_setLogin)
    password=property(_getPassword,_setPassword)
    role=property(_getRole,_setRole)
    datecreate=property(_getDateCreate,_setDateCreate)

    def __eq__(self,other):
        return(self._username==other.username and self._login==other.login)