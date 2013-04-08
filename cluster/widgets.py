from PyQt4 import QtGui, QtCore

class AlgSettingsWidget(QtGui.QWidget):
    
    def __init__(self, columns):
        super(AlgSettingsWidget, self).__init__()

        self.initUI(columns)

    def initUI(self, columns):
        layout = QtGui.QVBoxLayout()
        self.checkBoxes = {}
        for column in columns:
            checkBox = QtGui.QCheckBox(column, self)
            self.checkBoxes[column] = checkBox
            layout.addWidget(checkBox)

        self.setLayout(layout)
        self.show()

    def get_column_value(self, column):
        print column
        print self.checkBoxes
        return self.checkBoxes[column].isChecked()