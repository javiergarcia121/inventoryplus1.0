import PySimpleGUI as sg
import re
class ITEM:
    def __init__(self,name,category,location,quantity,atribute):
        self.name=name
        self.category=category
        self.location=location
        self.quantity=quantity
        self.atribute=atribute
    def getName(self):
        return self.name
    def getCategory(self):
        return self.category
    def getLocation(self):
        return self.location
    def getQuantity(self):
        return self.quantity
    def getAtribute(self):
        return self.atribute
    def print(self):
        print('\nName: ',self.name,'\nCategory: ',self.category,'\nLocation: ',
              self.location,'\nQuantity: ',self.quantity,'\nAtribute: ',self.atribute)
    def printcsv(self):
        return ('\n'+self.name+','+self.category+','+
              self.location+','+self.quantity+','+self.atribute)
    
def IsUserAndPass(userfile,user,password):
    file=open(userfile,'r')
    for line in file:
        if line != '\n':
            first,last=line.split(":")
            if(first==user and password==last):
                return True
        
    return False
def IsUser(userfile,user):
    file=open(userfile,'r')
    for line in file:
        if line != '\n':
            
            first,last=line.split(":")
            if(first==user):
                return True
        
    return False
def IsEmpty(pathfile):
    file=open(pathfile,'r')
    for line in file:
        if line != '\n':
            return False
        
    return True
def ItemSearch(item,itemlist):
    i=1
    for i in range(len(itemlist)):
            if(item.getName()==itemlist[i].getName()):
                return True;
    return False;
sg.theme('DarkAmber')

#Welcome Screen Layout
wslayout = [[sg.Text('\n\n\nWelcome to Inventory Plus',size=(30,0), justification='center',
            font=("Times", 35))],[sg.Button('Press here to continue', size=(19, 1),pad=((195, 10), 3),font='Helvetica 14')],
            [sg.Text('',size=(10,10))]]

#User Screen Layout
uslayout=[[sg.Text('\n\n\nUser Sign-In',size=(20, 0), justification='center', font=("Times", 35))],[sg.Text('User:\t',
         font=("Times",25)),sg.Input(size=(30,100),key='User')],[sg.Text('Password: ',font=("Times",25)),sg.Input(size=(30,100),key='Pass')],
         [sg.Button('Enter', size=(10, 1),pad=((150, 10), 3),font='Helvetica 14',key='Enter')],[sg.Text('',size=(10,10))]]
#File Choose Layout
fclayout=[[sg.Text('\n\n\nChoose files: ',size=(30,0), font=("Times", 35),key='text')],
          [sg.Text('Users File: ', size=(15, 1),font=("Times",15)), sg.Input(key='UF'), sg.FileBrowse()],
          [sg.Text('Inventory File:', size=(15, 1),font=("Times",15)), sg.Input(key='IF'), sg.FileBrowse()],
          [sg.Submit(pad=((195, 10), 3),key='Submit'), sg.Cancel()],[sg.Text('',size=(10,10))]]

welcomescreen = sg.Window('Inventory Plus', wslayout)    

wsevent, wsvalues = welcomescreen.read()    
welcomescreen.close()

pathfile='PathFile.txt'
if(IsEmpty(pathfile)):
    filechoosescreen = sg.Window('Inventory Plus', fclayout)    
    fcevent, fcvalues = filechoosescreen.read()
    path=open(pathfile,'a')
    path.write(fcvalues['UF'])
    path.write("\n")
    path.write(fcvalues['IF'])
    path.close()
    if fcevent=='Submit':
        filechoosescreen .close()
ufname,ufnamefinal,ifname,ifnamefinal='','','',''
fp=open(pathfile)
for i, line in enumerate(fp):
    if line!='\n':
        if i == 0:
            ufname=line.split("/")
            ufnamefinal=ufname[len(ufname)-1]
            ufnamefinal = re.sub('\n$', '', ufnamefinal)
        elif i == 1:
            ifname=line.split("/")
            ifnamefinal=ifname[len(ifname)-1]
cond=False
path=open(ufnamefinal,'r')
for line in path:
    if line!='\n':
        cond=True
if cond:
    userwelcome=sg.Window('Inventory Plus',uslayout)
    while True:
        usevent, usvalues = userwelcome.read()
        if usevent=='Enter' and IsUserAndPass(ufnamefinal,usvalues['User'],usvalues['Pass'])!=True:
            userwelcome['text'].update('\n\n\nEnter a valid user and password')
            userwelcome['User'].update('')
            userwelcome['Pass'].update('')
        if usevent=='Enter' and IsUserAndPass(ufnamefinal,usvalues['User'],usvalues['Pass'])==True:
            sg.popup('Logged In Succesfully!')
            break
    userwelcome.close()
#Top Menu
menu_def = [['Inventory Management', ['Add...', 'Delete...', 'Update...', 'Search...']],      
            ['Dashboard',['Reports...']],      
            ['Users', ['Add User...','Delete User...','Update User...']],['Settings']] 

#Main Screen Layout
variable=[sg.Text('Choose option')]
mslayout=[[sg.Menu(menu_def, tearoff=True,key='Menu')],[sg.Text('',size=(100,100))],variable]
mainscreen=sg.Window('Inventory Plus',mslayout)
msevent,msvalues=mainscreen.read()



#AddScreenLayout
#ESTO HAY QUE ARREGLARLO Y PONERLO BONITO
#EN CADA ANADIR O LEER HAY QUE LEER DEL ARCHIVO
fp=open(ifnamefinal,'r')
inventorylist=[]
for i, line in enumerate(fp):
    if line!='\n' and i>0:
        name,category,location,quantity,atribute=line.split(',')
        item=ITEM(name,category,location,quantity,atribute)
        inventorylist.append(item)#Anadi a list
fp.close()
aslayout=[[sg.Text('\n\n\nAdd Item',size=(20, 0), justification='center', font=("Times", 35),key='Title')],
         [sg.Text('Item Name'),sg.Input(key='ITEMNAME')],[sg.Text('Category'),sg.Input(key='CATEGORY')],
         [sg.Text('Location'),sg.Input(key='LOCATION')],[sg.Text('Quantity'),sg.Input(key='QUANTITY')],
          [sg.Text('Atribute'),sg.Input(key='ATRIBUTE')],[sg.Submit(pad=((195, 10), 3),key='Submit'), sg.Cancel()]
          ,[sg.Text('',size=(10,10))]]
while True:
    msevent,msvalues=mainscreen.read()
    if msevent=='Add...':#hay que darle dos veces
        addscreen=sg.Window('Inventory Plus',aslayout)
        
        while True:
            asevent,asvalues=addscreen.read()
            item=ITEM(asvalues['ITEMNAME'],asvalues['CATEGORY'],asvalues['LOCATION'],asvalues['QUANTITY'],asvalues['ATRIBUTE'])
            if asevent=='Submit':
                if (ItemSearch(item,inventorylist)==False):
                    inventorylist.append(item) #Anadi a list
                    fp=open(ifnamefinal,'a')
                    fp.write(item.printcsv())#Anadi a csv
                    fp.close()
                    sg.popup('Added Succesfully!')
                    addscreen.close()
                    break
                else:
                   addscreen['Title'].update('\n\n\nPlease Enter A New Item')
                   addscreen['ITEMNAME'].update('')
                   addscreen['CATEGORY'].update('')
                   addscreen['LOCATION'].update('')
                   addscreen['QUANTITY'].update('')
                   addscreen['ATRIBUTE'].update('')
    if msevent=='Delete...':#un Search pero con un buton y delete
        print('')
    if msevent=='Update...':#un Search con un boton de update,una lista de search results y campos
    #de Add activados despues de esocger un item en search results
        print('')
    if msevent=='Search...':
    #Combo box para escoger campo de busqueda,input,boton y resultados
    #este es el primero que se debe hacer
        print('')

    else:
        break
mainscreen.close()







