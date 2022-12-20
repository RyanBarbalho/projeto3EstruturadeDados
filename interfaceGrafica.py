

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QBrush, QPen
from PyQt5.QtWidgets import *
import os

ind = 0

class Node:
    def __init__(self, key, ind, X, Y):
        self.name = key
        self.count = ind
        self.x = X
        self.y = Y
        self.left = None
        self.right = None
        
        
def comparison(fatherlist, sonlist, size):
    resembles = 0
    for i in range (size):
        if fatherlist[i] == sonlist[i]:
            resembles+=1

    return resembles


#print inOrder
def printTree(root):
        if root.left:
            printTree(root.left)
        print(root.name)
        if root.right:
            printTree(root.right)

class lista:
    def __init__(root, name, car1,car2,car3,car4):
        root.name = name 
        root.charac = [car1,car2,car3,car4]
#criar lista         
LISTA = []

class Ui_MainWindow(QtWidgets.QWidget):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 200)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(40, 20, 101, 20))
        self.lineEdit.setObjectName("lineEdit")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(50, 180, 75, 23))
        self.pushButton.setObjectName("pushButton")

       
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(10, 60, 161, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")

        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(10, 90, 161, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")

        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(10, 150, 161, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")

        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(10, 120, 161, 20))
        self.lineEdit_6.setObjectName("lineEdit_6")

        #botao 1 eh clicado
        self.pushButton.clicked.connect(self.insertNode)
        

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 926, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    
    def insertNode(self):
        global ind
        name = self.lineEdit.text()
        
        caracteristica1 = self.lineEdit_3.text()
        caracteristica2 = self.lineEdit_4.text()
        caracteristica3 = self.lineEdit_5.text()
        caracteristica4 = self.lineEdit_6.text()
        object = lista(name, caracteristica1, caracteristica2, caracteristica3, caracteristica4)
        LISTA.append(object)
        if ind == 0:
            
            with open('entry.txt', 'a+') as file:
                file.write(LISTA[ind].name + "\n" + LISTA[ind].charac[0] + "\n" + LISTA[ind].charac[1] + "\n" + LISTA[ind].charac[2] + "\n" + LISTA[ind].charac[3] + "\n")
            ind+=1  
        else:

            with open('entry.txt', 'a+') as file:
                file.write(str(1) + "\n" +LISTA[ind].name + "\n" + LISTA[ind].charac[0] + "\n" + LISTA[ind].charac[1] + "\n" + LISTA[ind].charac[2] + "\n" + LISTA[ind].charac[3] + "\n")
            ind+=1      
        os.system('C:/TDM-GCC-32/bin/g++.exe -fdiagnostics-color=always -g "D:\estrutura de dados\graphicsProgram\projeto3.cpp" -o "D:\estrutura de dados\graphicsProgram\projeto3.exe" -lbgi -lgdi32 -lcomdlg32 -luuid -loleaut32 -lole32 && "D:\estrutura de dados\graphicsProgram\projeto3.exe"')
        
    
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Insert Node"))
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

