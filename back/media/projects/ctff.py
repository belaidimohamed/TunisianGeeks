from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon ,QImage ,QPalette,QBrush,QFont
from PyQt5.QtCore import QSize
import os

os.chdir(r'C:\Users\user16\Desktop\png')


class main(QDialog) :
    def __init__(self):
        super().__init__()
        self.initwindow()
        oImage = QImage("back2.jpg")
        sImage = oImage.scaled(QSize(500,300))
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))
        self.setPalette(palette)
        self.show()
    def initwindow(self):
        self.setWindowTitle('CTF')
        self.setWindowIcon(QIcon('detective1.png'))
        self.setGeometry(200,80,1000,600)
        vbox=QVBoxLayout()
        vbox.setContentsMargins(20,0,50,2)
        self.score_int=0
        self.score=self.label("Your score is : "+str(self.score_int),"red","Ink Free",15)
        hbox=QHBoxLayout()
        hbox.setContentsMargins(20,0,50,10)
        gbox=QGridLayout()
        gbox.setContentsMargins(20,10,20,10)
        gbox.addWidget(self.challenge('challenge 1  (50 points)'),1,1)
        gbox.addWidget(self.challenge('challenge 2  (50 points)'),1,2)
        gbox.addWidget(self.challenge('challenge 3  (100 points)','green'),2,1)
        gbox.addWidget(self.challenge('challenge 4  (100 points)',"green"),2,2)
        gbox.addWidget(self.challenge('challenge 5  (150 points)','blue'),3,1)
        gbox.addWidget(self.challenge('challenge 6  (250 points)','red'),3,2)
        hbox.addWidget(self.challenge('Previous page','grey',100,30,9))
        hbox.addWidget(self.challenge('Next page','grey',100,30,9))
        vbox.addWidget(self.label("Choose one of thee following challenges : ","yellow","Jokerman",20))
        vbox.addLayout(gbox)
        vbox.addWidget(self.score)

        vbox.addLayout(hbox)
        self.setLayout(vbox)
    def challenge(self,name='challenge',color="orange",a=400,e=200,f=20):
        b=QPushButton(name)
        b.setStyleSheet("background-color:"+color)
        b.setFont(QFont('Viner Hand ITC',f))
        b.setMaximumSize(a,e)
        if name=='challenge 1  (50 points)':
            b.clicked.connect(self.challenge1)
        elif name=='challenge 2  (50 points)':
            b.clicked.connect(self.challenge2)
        elif name=='challenge 3  (100 points)':
            b.clicked.connect(self.challenge3)

        return b
    def label(self,txt='',color="grey",form="sanserif",a=10):
        l=QLabel(txt)
        l.setFont(QFont(form,a))
        l.setStyleSheet('color:'+color)
        return l
    def challenge1(self):
            text,ok=QInputDialog.getText(self,"answer this ^_^ ","This ur first challenge i hope you like it :) \n               how much is : 1\\1 ",QLineEdit.Normal)
            if ok and text == "1" :
                self.score_int+=50
                self.score.setText("Your score is : {}".format(str(self.score_int)))
    def challenge2(self):
            text,ok=QInputDialog.getText(self,"answer this ^_^ ","This ur second challenge :\n                      how much is : 5*5 ",QLineEdit.Normal)
            if ok and text == "25" :
                self.score_int+=50
                self.score.setText("Your score is : {}".format(str(self.score_int)))
    def challenge3(self):
            text,ok=QInputDialog.getText(self,"answer this ^_^ ","Now let's try somthing hard ! \n   what is mohamed favorite series ? \n   (note : lower_case input)",QLineEdit.Normal)
            if ok and text == "person of interest" :
                self.score_int+=100
                self.score.setText("Your score is : {}".format(str(self.score_int)))

w=main()