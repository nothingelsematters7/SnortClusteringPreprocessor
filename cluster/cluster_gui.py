#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
ZetCode PyQt4 tutorial 

This example shows an icon
in the titlebar of the window.

author: Jan Bodnar
website: zetcode.com 
last edited: October 2011
"""

import sys
from PyQt4 import QtGui, QtCore


class Example(QtGui.QMainWindow):
    
    def __init__(self):
        super(Example, self).__init__()

        self.file_name = ''
        
        self.initUI()
        
    def initUI(self):

        self.statusBar().showMessage('Ready')

        # Make central widget
        # textEdit = QtGui.QTextEdit()
        # self.setCentralWidget(textEdit)
        
        # QtGui.QToolTip.setFont(QtGui.QFont('SansSerif', 10))
        
        # self.setToolTip('This is a <b>QWidget</b> widget')
        
        # btn = QtGui.QPushButton('Button', self)
        # btn.setToolTip('This is a <b>QPushButton</b> widget')
        # btn.resize(btn.sizeHint())
        # btn.move(50, 50)       

        # qbtn = QtGui.QPushButton('Quit', self)
        # qbtn.clicked.connect(QtCore.QCoreApplication.instance().quit)
        # qbtn.resize(qbtn.sizeHint())
        # qbtn.move(50, 150)

        self.table = QtGui.QTableWidget(5, 3, self)
        for i in range(5):
            for j in range(3):
                self.table.setItem(i, j, QtGui.QTableWidgetItem(str(i * j)))

        openFileAction = QtGui.QAction(QtGui.QIcon.fromTheme('document-open'), '&Open file', self)
        openFileAction.setShortcut('Ctrl+O')
        openFileAction.setStatusTip('Open data file')
        openFileAction.triggered.connect(self.openFile)

        exitAction = QtGui.QAction(QtGui.QIcon('exit.svg'), '&Exit', self)        
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(QtGui.qApp.quit)

        # Create Menu bar

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openFileAction)
        fileMenu.addAction(exitAction)

        # Create Tool bar

        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(openFileAction)
        self.toolbar.addAction(exitAction)
        
        self.resize(500, 400)
        self.center()

        self.setCentralWidget(self.table)

        self.setWindowTitle('Network data analyzer')
        self.setWindowIcon(QtGui.QIcon.fromTheme('applications-science'))
        self.show()

    def center(self):
        qr = self.frameGeometry()
        print qr
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def openFile(self):
        fname = QtGui.QFileDialog.getOpenFileName(self, 'Open file', '/home/devil/')
        self.file_name = fname
        self.setWindowTitle(self.file_name)


    def closeEvent(self, event):
        
        reply = QtGui.QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QtGui.QMessageBox.Yes | 
            QtGui.QMessageBox.No, QtGui.QMessageBox.No)

        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()    