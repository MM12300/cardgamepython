class Compte:
    __droitBase={}
    def __init__(self,nom,dictPathDroit={}):
        self.__setNom(nom)
        self.__pathDroits={}
        for path in dictPathDroit:
            self.__pathDroits[path]=dictPathDroit[path]
    def __setNom(self,no):
        self.__nom=nom
    def getNom(self,nom):
        return self.__nom
    def getPathDroit(self,path):

        if path in self.__pathDroits:
            return self.__pathDroits[path]
        else:
            for p in self.__pathDroits:
                if p in path or path in p:
                    return self.__pathDroits[p]
            return (0,0,0)
    def setPathDroit(self,path,r,w,x):
        droitCompte=self.getPathDroit(path)
        if droitCompte!=(0,0,0) and droitCompte[0]>=r and droitCompte[1]>=w and droitCompte[2]>=x:
            self.__pathDroits[path]=(r,w,x)
        else :
            print('Not allowed to increase privileges!')

class Root(Compte):
    __droitBase={'/':(1,1,1)}
    def __init__(self,nom='root',dictPathDroit=__droitBase):
        super().__init__(nom,dictPathDroit)
    def setPathDroitUser(self,compte,path,r,w,x):
        droitCompte=compte.getPathDroit(path)
        if droitCompte!=(0,0,0) and droitCompte[0]>=r and droitCompte[1]>=w and droitCompte[2]>=x:
            compte.setPathDroit(path,r,w,x)
        else:
            print('Permissions not enough restrictive!')

class Admin(Root):
    __droitBase={'/usr':(1,1,1),'/lib':(1,1,1),'/etc':(1,1,1),'/bin':(1,0,1),'/sbin':(1,0,1)}
    def __init__(self,nom,dictPathDroit=__droitBase):
        super().__init__(nom,dictPathDroit)
    def setPathDroitUser(self,compte,path,r,w,x):
        if compte.__class__ != 'Root':
            super().setPathDroitUser(self,path,r,w,x)
        else:
            print('Permission denied!')

class Privilegie(Admin):
    __droitBase={'/usr':(1,0,1),'/lib':(1,0,1),'/etc':(1,0,1),'/bin':(0,0,1),'/sbin':(0,0,1)}
    def __init__(self,nom,dictPathDroit=__droitBase):
        dictPathDroit['/home/'+nom]=(1,1,1)
        super().__init__(nom,dictPathDroit)
    def setPathDroitUser(self,compte,path,r,w,x):
        if compte.__class__ != 'Admin':
            super().setPathDroitUser(self,path,r,w,x)
        else:
            print('Permission denied!')
            
class Simple(Privilegie):
    __droitBase={'/bin':(0,0,1)}
    def __init__(self,nom,dictPathDroit=__droitBase):
        super().__init__(nom,dictPathDroit)
    def setPathDroitUser(self,compte,path,r,w,x):
        if compte.__class__ != 'Privilegie':
            super().setPathDroitUser(self,path,r,w,x)
        else:
            print('Permission denied!')
            
    
            
def main():
    r=Root()
    a=Admin('hyper_toto')
    p=Privilegie('super_toto')
    s=Simple('average_toto')
    a.setPathDroitUser(p,'/bin/shells',0,0,0)
    a.setPathDroitUser(p,'/bin/shells',0,1,0)
if __name__=='__main__':
    main()