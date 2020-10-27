from PyQt5.QtWidgets import *
from PyQt5.QtGui  import  *
from PyQt5.QtCore import *
import sys , os
import socket
import subprocess
import scapy.all as scapy
import time
import sqlite3 as sql
from datetime import datetime 
os.chdir(r'C:\Users\user16\Desktop\png')
s=socket.socket()
con=sql.connect('messanger_socket_database.sq3')
cur=con.cursor()

cur.execute("create table if not exists friends(mac_address text primary key , name text , mawsoug text) ")
cur.close()
con.close()
class scanining(QThread):
    value=pyqtSignal(float)
    value2=pyqtSignal(list)
    def scanip(self,ip,j):
        l=[]
        arp_request= scapy.ARP(pdst=ip)
        broadcast= scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
        arp_request_broadcast = broadcast/arp_request
        answred_list=scapy.srp(arp_request_broadcast, timeout=0.2,verbose=False)[0]
        for i in answred_list :
            return (i[1].psrc,i[1].hwsrc)
    def scan_network (self):
        data=subprocess.check_output(['arp','-a']).decode('cp1252').split("\n")
        modem_ip=data[3][2:18][:10]
        print(modem_ip)
        l=[]
        for i in range(1,255):
            x=self.scanip(modem_ip+str(i),i)
            if x!=None :
                l.append(x)
            self.value.emit(i*100/255)
        return l
    def run(self):
        val2=self.scan_network()
        self.value2.emit(val2)
        print(val2)
class server(QThread):
    def __init__(self,cmd,index=1):
        super().__init__()
        self.cmd=cmd
        self.index=index
    def createsocket(self):
        try :
            self.host=''
            self.port = 9999
            self.s= socket.socket()
        except socket.error as msg:
            print('socket creation error'+str(msg))
    def binding_socket(self):
        try :
            print('binding the port '+str(self.port))
            self.s.bind((self.host,self.port))
            self.s.listen(5)
        except socket.error as msg :
            print('socket binding error '+str(msg) +'\n'+'retrying ...')
            bind_socket()
    def get_mac(self,ip):
        arp_request= scapy.ARP(pdst=ip)
        broadcast= scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
        arp_request_broadcast = broadcast/arp_request
        answred_list=scapy.srp(arp_request_broadcast, timeout=0.2,verbose=False)[0]
        for i in answred_list :
            return i[1].hwsrc
    def socket_accept(self) :
        con,adresse = self.s.accept()
        print('connection has been established () IP: {} , port: {}'.format(adresse[0],str(adresse[1])))
        if self.index==1:
            self.send_commande(con,"ahmed")
            self.send_commande(con,self.cmd)
            con.close()
        elif self.index==0 :
            self.mac=self.get_mac(adresse[0])
            if self.mac==None :
                self.mac="80-C5-F2-49-82-63"
            self.send_commande(con,"ahmed")
            self.thread3=client(adresse[0],mac)
            self.thread3.start() 
            self.send_commande(con,self.cmd)
            con.close()    
    def send_commande(self,con,cmd):
        
        if cmd=='quit':
            con.close()
            self.s.close()
            sys.exit()
        if len(str.encode(cmd))>0 :
            con.send(str.encode("echo "+cmd))
            client_reponse = str(con.recv(1024),'utf-8')
            print(client_reponse , end='')
    def run(self):
        self.createsocket()
        self.binding_socket()
        self.socket_accept()
        while 1 :
            self.send_commande(con,cmd)
class client(QThread):
    value1=pyqtSignal(str)
    def __init__(self,ip,mac):
        super().__init__()
        self.ip=ip
        self.mac=mac
    def run(self) :
        self.s=socket.socket()
        host=self.ip
        port= 9999
        self.s.connect((host,port))
        while 1 :
            data=self.s.recv(1024)
            if data[:2].decode('utf-8')=='cd':
                os.chdir(data[3:].decode('utf-8'))
            if len(data) > 0:
                cmd= subprocess.Popen(data[:].decode('utf-8'), shell=True , stdout=subprocess.PIPE , stdin=subprocess.PIPE , stderr=subprocess.PIPE)
                output_bytes=cmd.stdout.read()+cmd.stderr.read()
                output_str = str(output_bytes,'cp1252')
                currentWD = os.getcwd()+' >'
                self.s.send(str.encode(output_str + currentWD))
                time=datetime.now().strftime("%Y/%M/%d, %H:%M")
                ch=time+' >>> '+output_str
                con=sql.connect('messanger_socket_database.sq3')
                cur=con.cursor()
                if self.mac==None :
                    self.mac="80-C5-F2-49-82-63"
                cur.execute("select mac_address , mawsoug from friends where mac_address='{}'".format(self.mac))
                x=cur.fetchall()
                y="------ starting conversation at "+datetime.now().strftime("%m:%d:%Y,%H:%M:%S")+" -------+ \n "
                if len(x)<1:
                    print(self.mac)
                    cur.execute(f"insert into friends (mac_address , name , mawsoug ) values(?,?,?)",(self.mac,"name1",y))
                else :
                    ch=x[0][1]+ch
                    cur.execute("update friends set mawsoug = (?)  where mac_address = (?)",(ch,self.mac,))
                    self.value1.emit(ch)
                con.commit()
                cur.close()
                con.close()
                
class window(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('shit')
        self.setWindowIcon(QIcon('detective1.png'))
        self.setGeometry(200,100,1000,400)

        oImage = QImage("back2.jpg")
        sImage = oImage.scaled(QSize(500,300))                   # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))                     # 10 = Windowrole
        self.setPalette(palette)
        self.initWindow()
        self.show()
        cmd="rami"
        self.thread_enter=server(cmd,0)
        self.thread_enter.start()

    def initWindow(self):
        global items
        ip='44'
        name='None'
        statu='Connected'
        self.great_vbox=QVBoxLayout()
        great_hbox=QHBoxLayout()
        vbox2=QVBoxLayout()
        vbox=QVBoxLayout()
        #layout.setContentsMargins(left, top, right, bottom)
        vbox2.setContentsMargins(50, 10, 10, 10)


        hbox=QHBoxLayout()
        hbox1=QHBoxLayout()
        hbox2=QHBoxLayout()
        self.message_show=QTextEdit()
        self.message_show.setFont(QFont('SansSerif', 10))
        self.message_show.setStyleSheet('background-color: rgb(40,40,40);font-size:20;color: purple;')
        self.message_show.setMinimumSize(700,350)
        self.messagesender=self.line('purple',600)

        l=QLabel('list of connected ip :',self)
        l.setStyleSheet('color:red')
        l.setFont(QFont('sanserif',13))
        ################################################# gbox part #########################################################""
        gbox=QGroupBox()
        hbox0=QHBoxLayout()
        hbox0_1=QHBoxLayout()
        vbox0=QVBoxLayout()
        self.insert_text=QLineEdit()
        button_scan=self.button('scan network ','grey',160 ,30 )
        button_scan.clicked.connect(self.scan)
        button_insert=self.button('insert ','grey',160 ,30 )
        button_insert.clicked.connect(self.insert_manuelly)
        hbox0.addWidget(self.label(' Or just insert the ip manuelly :  '))
        hbox0.addWidget(self.insert_text)
        hbox0.addWidget(button_insert)
        hbox0_1.addWidget(self.label('scan network for connected ip : '))
        hbox0_1.addWidget(button_scan)
        vbox0.addLayout(hbox0_1)

        vbox0.addLayout(hbox0)
        vbox0.setContentsMargins(5,5,400,5)
        gbox.setLayout(vbox0)
        ##################################################################################################################
        self.label_ip=self.label('ip   : ' ,'green')
        self.label_name=self.label('                                 name : ' , 'green')
        self.label_statu=self.label('                                 status : '+statu , 'green')

        self.button_exit=self.button(' Exit ','red',160 ,30 )
        self.button_exit.clicked.connect(self.exitt)

        hbox.addWidget(self.label('messages avec : '))
        hbox.addWidget(self.label_ip)
        hbox.setContentsMargins(5,5,380,5)
        vbox.addLayout(hbox)
        vbox.addWidget(self.label_name)
        vbox.addWidget(self.label_statu)
        vbox.addWidget(self.message_show)
        vbox.addWidget(self.label('Write a message ..'))
        vbox.addWidget(self.messagesender)
        hbox2.addWidget(self.button(' send photo ' ,'grey',160 ,30 ))
        hbox2.addWidget(self.button(' send file ','grey',160 ,30 ))
        vbox.addLayout(hbox2)

        vbox2.addWidget(l)
        self.list=self.listip()
        vbox2.addWidget(self.list)
        vbox2.addWidget(self.button_exit)

        

        great_hbox.addLayout(vbox)
        great_hbox.addLayout(vbox2)
        self.great_vbox.addWidget(gbox)
        self.great_vbox.addLayout(great_hbox)
        self.setLayout(self.great_vbox)
   ########################################### first ( Vbox ) functions ###########################################
    def button(self, name=' ' , color='orange' ,a=50,c=30 ):
        b=QPushButton(name)
        b.setStyleSheet('background-color: '+color)
        b.setMaximumSize(a,c)
        return b
    def label(self,message=' ',color='red',a=11):
        l=QLabel(message,self)
        l.setStyleSheet('color:'+color)
        l.setFont(QFont('sanserif',a))
        return l
    def line(self,color='green',width=200):
        lline=QLineEdit()
        lline.setStyleSheet('background-color:'+color)
        lline.setMaximumWidth(width)
        lline.setTextMargins(8,3,3,3)
        lline.setFont(QFont('sanserif',10))
        return lline
############################################## second ( vbox2) functions #############################################
    def exitt(self):
        sys.exit()
    def listip(self):
        list=QListWidget()

        list.setStyleSheet('background-image: url(back_m.jpg);')
        list.setFont(QFont('sanserif',13))
        list.clicked.connect(self.slot)
        list.insertItem(0,'connected ip :')
        # for j in range(len(l)) :
        #     self.list.insertItem(j,l[j][0])
        return list
    def insert_manuelly(self):
        print(self.insert_text.text())
        self.label_ip.setText('ip   : '+self.insert_text.text())
        mac=self.get_mac(self.insert_text.text())
        self.thread1=client(self.insert_text.text(),mac)
        self.thread1.value1.connect(self.blaa)
        self.thread1.start() 
        print(self.insert_text.text())
    def slot(self):
        global items
        items=self.list.currentItem().text()
        mac=self.get_mac(items)
        self.label_ip.setText('ip   : '+items)
        self.thread1=client(items,mac)
        self.thread1.value1.connect(self.blaa)
        self.thread1.start() 
        print(items)
    def valprogress(self,val):
        self.progress.setValue(val)
        ch=""
        print(val,"%")

    def valist(self,val):
        print(val)
        ch=""
        s=0
        for i in val :
            s+=1
            self.list.insertItem(s,i[0])
        time.sleep(1)
        self.great_vbox.removeWidget(self.progress)
        self.progress.deleteLater()
        self.progress=None
    def scan(self):
        self.progress=QProgressBar()
        self.progress.setStyleSheet("color:red")
        self.great_vbox.addWidget(self.progress)
        self.thread=scanining()
        self.thread.value.connect(self.valprogress)
        self.thread.value2.connect(self.valist)
        self.thread.start() 
    def blaa(self,val):
        self.message_show.clear()
        self.message_show.setText(val)
    def get_mac(self,ip):
        arp_request= scapy.ARP(pdst=ip)
        broadcast= scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
        arp_request_broadcast = broadcast/arp_request
        answred_list=scapy.srp(arp_request_broadcast, timeout=0.2,verbose=False)[0]
        for i in answred_list :
            return i[1].hwsrc
app = QApplication(sys.argv)

win=window()
sys.exit(app.exec_())
