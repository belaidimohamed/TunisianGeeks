from PyQt5.QtWidgets import *
from PyQt5.QtGui  import  QIcon , QFont , QImage , QPalette , QBrush , QPixmap
from PyQt5.QtCore import QSize , QRect
import sys , os
os.chdir(r'C:\Users\user16\Desktop\png')
class encryption(QDialog):
    print('en train de construire ..')
class one(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('convertisseur')
        self.setWindowIcon(QIcon('detective1.png'))
        self.setGeometry(350,100,190,500)
        oImage = QImage("back2.jpg")
        sImage = oImage.scaled(QSize(470,300))
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))
        self.setPalette(palette)
        self.initwindow()
        self.show()
    def initwindow(self):
        self.vbox=QVBoxLayout()
        self.hbox=QHBoxLayout()
        self.vbox.setContentsMargins(30,0,30,20)
        label=QLabel('choose one of the folowing Editions : ')
        label.setStyleSheet('color: red')
        label.setFont(QFont('bold',11))
        label1=QLabel('                      Made by Mohamed')
        label1.setStyleSheet('color: yellow')
        label1.setFont(QFont('ink free',25))
        pix=QPixmap('binaire1.jpg')
        image=QLabel(self)
        image.setPixmap(pix)

        self.hbox.addWidget(label)
        button1=QPushButton(' Version 1 ')
        button1.setStyleSheet('background-color:green')
        button1.clicked.connect(self.b1)
        button2=QPushButton(' Version 2 ')
        button2.setStyleSheet('background-color:orange')
        button2.clicked.connect(self.b2)
        self.hbox.addWidget(button1)
        self.hbox.addWidget(button2)

        self.vbox.addWidget(label)
        self.vbox.addLayout(self.hbox)
        self.vbox.addWidget(image)
        self.vbox.addWidget(label1)

        self.setLayout(self.vbox)

    def b1(self):
        self.p=window1()
        self.close()
    def b2(self):
        self.q=window2()
        self.close()
class window1(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('shit')
        self.setWindowIcon(QIcon('detective1.png'))
        self.setGeometry(350,100,500,400)
        oImage = QImage("back2.jpg")
        sImage = oImage.scaled(QSize(470,300))
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))
        self.setPalette(palette)
        self.initwindow()
        self.show()
################ i've could used a much simpler method but i used this way only to learn more :D
    def oct_bin(self,x):
        s=''
        for i in x :
            s=s+self.dec_bin(i)
        return s
    def bin_oct(self,x):
        s=''
        if len(x)%3 ==1 :
            for i in range(len(x),0,3):
                if i==len(x) :
                    s=s+self.bin_dec('00'+x[i])
                else :
                    s=s+self.bin_dec(x[i]+x[i-1]+x[i-2])
        elif len(x)%3 == 2 :
            for i in range(len(x),0,3):
                if i==len(x):
                    s=s+self.bin_dec('0'+x[i])
                else :
                    s=s+self.bin_dec(x[i]+x[i-1]+x[i-2])
        return s
    def hexa_dec(self,x):
        d={'A':10 ,'B':11,'C':12,'D':13,'E':14,'F':15}
        s=0
        for i in range(len(x)) :
            if x[i] in ['0','1','2','3','4','5','6','7','8','9'] :
                print("{} , {} , {} ".format(s, int(x[i]), len(x)-i))
                s=s+int(x[i])*(16**(len(x)-i-1))
            elif x[i] in list(d.keys()):
                s=s+int(d[x[i]])*(16**(len(x)-i-1))
        return str(s)
    def dec_hexa(self,y):
        l=[]
        x=int(y)
        while (x!= 0):
            l.append(str(x%16))
            x=x//16
        l.reverse()
        hex="".join(l)
        return hex



    def dec_bin(self,y):
        l=[]
        x=int(y)
        while (x!= 0):
            l.append(str(x%2))
            x=x//2
        l.reverse()
        binaire="".join(l)
        return binaire
    def dec_oct(self,y):
        l=[]
        x=int(y)
        while (x!= 0):
            l.append(str(x%8))
            x=x//8
        l.reverse()
        oct="".join(l)
        return oct

    def bin_dec(self,y):
        x=str(y)
        s=0
        for i in range(len(x)) :
            print("{} , {} , {} ".format(s, int(x[i]), len(x)-i))
            s=s+int(x[i])*(2**(len(x)-i-1))
        return str(s)
    def oct_dec(self,y):
        x=str(y)
        s=0
        for i in range(len(x)) :
            print("{} , {} , {} ".format(s, int(x[i]), len(x)-i))
            s=s+int(x[i])*(8**(len(x)-i-1))
        return str(s)
    def initwindow(self):
        self.vbox=QVBoxLayout()
        self.hbox=QHBoxLayout()
        self.hbox.setContentsMargins(50,5,50,3)
        self.hbox.addWidget(self.label('convert from :',"orange"))
        self.combo1=self.combo()
        self.hbox.addWidget(self.combo1)
        self.hbox.addWidget(self.label(' to : ',"orange"))
        self.combo2=self.combo()
        self.hbox.addWidget(self.combo2)
        """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        self.hbox2=QHBoxLayout()
        self.hbox2.addWidget(self.label("enter what you want to convert: ","orange"))
        self.line=QLineEdit()
        self.line.returnPressed.connect(self.onpress)
        self.hbox2.addWidget(self.line)
        self.l=self.label('waiting for command ...')
        self.hbox.setContentsMargins(10,100,50,3)
        self.hbox2.setContentsMargins(10,50,10,3)

        self.vbox.addLayout(self.hbox)
        self.vbox.addLayout(self.hbox2)
        self.vbox.addWidget(self.l)


        self.vbox

        self.setLayout(self.vbox)
    def combo(self):
        comboBox = QComboBox()
        comboBox.setGeometry(QRect(40, 40, 491, 31))
        comboBox.setObjectName(("comboBox"))
        comboBox.addItem("decimale")
        comboBox.addItem("binaire")
        comboBox.addItem("hexadecimale")
        comboBox.addItem("octale")
        comboBox.currentTextChanged.connect(self.change)
        return comboBox
    def label(self,msg,color='red',a=12):
        llabel=QLabel(msg)
        llabel.setStyleSheet('color :'+color)
        llabel.setFont(QFont('Bold',a))
        return llabel
    def change(self) :
        self.host=self.combo1.currentText()
        self.guest=self.combo2.currentText()

    def onpress(self):
        x=self.line.text()
        if self.host == 'binaire' and self.guest =='decimale' :
            self.l.clear()
            self.l.setText(str(self.bin_dec(x)))
        elif self.host =='decimale' and self.guest =='binaire' :
            self.l.clear()
            self.l.setText(str(self.dec_bin(x)))
        elif self.host== 'octale' and self.guest == 'decimale' :
            self.l.clear()
            self.l.setText(str(self.oct_dec(x)))
        elif self.host == 'decimale' and self.guest =='octale' :
            self.l.clear()
            self.l.setText(str(self.dec_oct(x)))
        elif self.host == 'octale' and self.guest =='binaire' :
            self.l.clear()
            self.l.setText(str(self.oct_bin(x)))
        elif self.host == 'binaire' and self.guest =='octale' :
            self.l.clear()
            self.l.setText(str(self.bin_oct(x)))
        elif self.host == 'hexadecimale' and self.guest =='decimale' :
            self.l.clear()
            self.l.setText(str(self.hexa_dec(x)))
        elif self.host =='decimale' and self.guest =='decimale' :
            self.l.clear()
            self.l.setText(str(self.dec_hexa(x)))
class window2(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('shit')
        self.setWindowIcon(QIcon('detective1.png'))
        self.setGeometry(350,100,700,400)
        oImage = QImage("back2.jpg")
        sImage = oImage.scaled(QSize(470,300))
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))
        self.setPalette(palette)
        self.initwindow()
        self.show()
    def oct_bin(self,x):
        s=''
        for i in x :
            s=s+self.dec_bin(i)
        return s
    def bin_oct(self,x):
        s=''
        if len(x)%3 ==1 :
            for i in range(len(x),0,3):
                if i==len(x) :
                    s=s+self.bin_dec('00'+x[i])
                else :
                    s=s+self.bin_dec(x[i]+x[i-1]+x[i-2])
        elif len(x)%3 == 2 :
            for i in range(len(x),0,3):
                if i==len(x):
                    s=s+self.bin_dec('0'+x[i])
                else :
                    s=s+self.bin_dec(x[i]+x[i-1]+x[i-2])
        return s
    def hexa_dec(self,x):
        d={'A':10 ,'B':11,'C':12,'D':13,'E':14,'F':15}
        s=0
        for i in range(len(x)) :
            if x[i] in ['0','1','2','3','4','5','6','7','8','9'] :
                print("{} , {} , {} ".format(s, int(x[i]), len(x)-i))
                s=s+int(x[i])*(16**(len(x)-i-1))
            elif x[i] in list(d.keys()):
                s=s+int(d[x[i]])*(16**(len(x)-i-1))
        return str(s)
    def dec_hexa(self,y):
        d={10:'A' ,11:'B',12:'C',13:'D',14:'E',15:'F'}
        l=[]
        x=int(y)
        while (x!= 0):
            if str(x%16) in ['0','1','2','3','4','5','6','7','8','9'] :
                l.append(str(x%16))
                x=x//16
            else :
                z=x%16
                l.append(d[z])
                x=x//16
        l.reverse()
        hex="".join(l)
        return hex



    def dec_bin(self,y):
        l=[]
        x=int(y)
        while (x!= 0):
            l.append(str(x%2))
            x=x//2
        l.reverse()
        binaire="".join(l)
        return binaire
    def dec_oct(self,y):
        l=[]
        x=int(y)
        while (x!= 0):
            l.append(str(x%8))
            x=x//8
        l.reverse()
        oct="".join(l)
        return oct

    def bin_dec(self,y):
        x=str(y)
        s=0
        for i in range(len(x)) :
            print("{} , {} , {} ".format(s, int(x[i]), len(x)-i))
            s=s+int(x[i])*(2**(len(x)-i-1))
        return str(s)
    def oct_dec(self,y):
        x=str(y)
        s=0
        for i in range(len(x)) :
            print("{} , {} , {} ".format(s, int(x[i]), len(x)-i))
            s=s+int(x[i])*(8**(len(x)-i-1))
        return str(s)
    def initwindow(self):
        self.vbox=QVBoxLayout()
        self.hbox=QHBoxLayout()
        self.grid=QGridLayout()
        self.hbox.setContentsMargins(50,5,50,3)
        self.hbox.addWidget(self.label('Choose a base to start from : ',"orange"))
        self.combo1=self.combo()
        self.hbox.addWidget(self.combo1)
        self.grid.addWidget(self.label('Binaire',"blue"),1,1)
        self.grid.addWidget(self.label('deciamle',"blue"),1,2)
        self.grid.addWidget(self.label('hexadecimale',"blue"),1,3)
        self.grid.addWidget(self.label('octale',"blue"),1,4)
        self.bin=self.label('-',"blue")
        self.dec=self.label('-',"blue")
        self.hex=self.label('-',"blue")
        self.oct=self.label('-',"blue")
        self.grid.addWidget(self.bin,2,1)
        self.grid.addWidget(self.dec,2,2)
        self.grid.addWidget(self.hex,2,3)
        self.grid.addWidget(self.oct,2,4)

        """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        self.hbox2=QHBoxLayout()
        self.hbox2.addWidget(self.label("enter what you want to convert: ","orange"))
        self.line=QLineEdit()
        self.line.returnPressed.connect(self.onpress)
        self.hbox2.addWidget(self.line)
        self.l=self.label('waiting for command ...')
        self.hbox.setContentsMargins(10,100,50,3)
        self.hbox2.setContentsMargins(10,50,10,3)
        self.vbox.addLayout(self.hbox)
        self.vbox.addLayout(self.hbox2)
        self.vbox.addLayout(self.grid)

        self.vbox.addWidget(self.l)


        self.vbox

        self.setLayout(self.vbox)
    def combo(self):
        comboBox = QComboBox()
        comboBox.setGeometry(QRect(40, 40, 491, 31))
        comboBox.setObjectName(("comboBox"))
        comboBox.addItem("decimale")
        comboBox.addItem("binaire")
        comboBox.addItem("hexadecimale")
        comboBox.addItem("octale")
        comboBox.currentTextChanged.connect(self.change)
        return comboBox
    def label(self,msg,color='red',a=12):
        llabel=QLabel(msg)
        llabel.setStyleSheet('color :'+color)
        llabel.setFont(QFont('Bold',a))
        return llabel
    def change(self) :
        self.host =self.combo1.currentText()
    def onpress(self):
        x=self.line.text()
        try :
            y=self.host
        except AttributeError :
            y='decimale'
        if y == 'decimale' :
            self.bin.clear()
            self.bin.setText(self.dec_bin(x))
            self.dec.clear()
            self.dec.setText(x)
            self.hex.clear()
            self.hex.setText(self.dec_hexa(x))
            self.oct.clear()
            self.oct.setText(self.dec_oct(x))
        elif y =='binaire' :
            self.grid.addWidget(self.label('Binaire',"blue"),1,1)
        elif y== 'octale' :
            self.grid.addWidget(self.label('Binaire',"blue"),1,1)
        elif y == 'decimale' :
            self.grid.addWidget(self.label('Binaire',"blue"),1,1)



win=one()


