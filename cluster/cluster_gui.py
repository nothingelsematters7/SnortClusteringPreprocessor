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
import os
from PyQt4 import QtGui, QtCore
from widgets import AlgSettingsWidget
from cluster import NetworkDataFile


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

        openTrainingDataSet = QtGui.QAction(QtGui.QIcon.fromTheme('document-open'), '&Open training data set', self)
        openTrainingDataSet.setShortcut('Ctrl+O')
        openTrainingDataSet.setStatusTip('Open training data set')
        openTrainingDataSet.triggered.connect(self.openTrainingFile)

        openTestDataSet = QtGui.QAction(QtGui.QIcon.fromTheme('document-open'), '&Open test data set', self)
        openTestDataSet.setShortcut('Ctrl+T')
        openTestDataSet.setStatusTip('Open test data set')
        openTestDataSet.triggered.connect(self.openTestFile)

        exitAction = QtGui.QAction(QtGui.QIcon('exit.svg'), '&Exit', self)        
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(QtGui.qApp.quit)

        # Create Menu bar

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openTrainingDataSet)
        fileMenu.addAction(openTestDataSet)
        fileMenu.addAction(exitAction)

        # Create Tool bar

        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(openTrainingDataSet)
        self.toolbar.addAction(openTestDataSet)
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

    def openTrainingFile(self):
        fname = QtGui.QFileDialog.getOpenFileName(self, 'Open training file', os.curdir)
        if fname:
            self.training_file = NetworkDataFile(fname)
            self.settings = AlgSettingsWidget(self.training_file.columns)
            self.setCentralWidget(self.settings)
            self.statusBar().showMessage('Training file selected:' + fname)

    def openTestFile(self):
        fname = QtGui.QFileDialog.getOpenFileName(self, 'Open test file', os.curdir)
        self.test_file_name = fname
        self.statusBar().showMessage('Test file selected:' + fname)


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