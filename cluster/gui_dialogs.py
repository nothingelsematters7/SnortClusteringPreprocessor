#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
ZetCode PyQt4 tutorial 

In this example, we receive data from
a QtGui.QInputDialog dialog. 

author: Jan Bodnar
website: zetcode.com 
last edited: October 2011
"""

import sys
from PyQt4 import QtGui


class Example(QtGui.QWidget):
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
    def initUI(self):      

        self.btn = QtGui.QPushButton('Dialog text', self)
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.showDialog)
        
        self.le = QtGui.QLineEdit(self)
        self.le.move(130, 22)
        
        self.color_btn = QtGui.QPushButton('Color dialog', self)
        self.color_btn.move(20, 130)
        self.color_btn.clicked.connect(self.showDialog)

        col = QtGui.QColor(127, 127, 127)

        self.frm = QtGui.QFrame(self)
        self.frm.setStyleSheet("QWidget { background-color: %s }" % col.name())
        self.frm.setGeometry(130, 130, 100, 100)

        self.font = QtGui.QPushButton('Font dialog', self)
        self.font.move(20, 260)
        self.font.clicked.connect(self.showDialog)


        self.setGeometry(300, 300, 290, 500)
        self.setWindowTitle('Input dialog')
        self.show()
        
    def showDialog(self):
        
        if self.sender() == self.btn:
            text, ok = QtGui.QInputDialog.getText(self, 'Input Dialog', 
                'Enter your name:')
            
            if ok:
                self.le.setText(str(text))
        elif self.sender() == self.color_btn:
            col = QtGui.QColorDialog.getColor()

            if col.isValid():
                self.frm.setStyleSheet("QWidget { background-color: %s }" % col.name())
        elif self.sender() == self.font:
            # font, ok = QtGui.QFontDialog.getFont()
            # if ok:
            #     self.le.setFont(font)
            fname = QtGui.QFileDialog.getOpenFileName(self, 'Open file', '/home')
            self.le.setText(fname)

        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()