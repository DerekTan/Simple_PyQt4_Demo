# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\codes\python\pyqt\taxCalc.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(517, 459)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tePrice = QtGui.QTextEdit(self.centralwidget)
        self.tePrice.setGeometry(QtCore.QRect(240, 100, 104, 71))
        self.tePrice.setObjectName(_fromUtf8("tePrice"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 130, 46, 13))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.sbTax = QtGui.QSpinBox(self.centralwidget)
        self.sbTax.setGeometry(QtCore.QRect(250, 220, 42, 22))
        self.sbTax.setProperty("value", 20)
        self.sbTax.setObjectName(_fromUtf8("sbTax"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(170, 230, 46, 13))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.btCalcTax = QtGui.QPushButton(self.centralwidget)
        self.btCalcTax.setGeometry(QtCore.QRect(190, 350, 75, 23))
        self.btCalcTax.setObjectName(_fromUtf8("btCalcTax"))
        self.teResult = QtGui.QTextEdit(self.centralwidget)
        self.teResult.setGeometry(QtCore.QRect(380, 310, 104, 71))
        self.teResult.setObjectName(_fromUtf8("teResult"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 517, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuTax_Calc = QtGui.QMenu(self.menubar)
        self.menuTax_Calc.setObjectName(_fromUtf8("menuTax_Calc"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuTax_Calc.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "Price", None))
        self.label_2.setText(_translate("MainWindow", "Tax Rate", None))
        self.btCalcTax.setText(_translate("MainWindow", "Caculate", None))
        self.menuTax_Calc.setTitle(_translate("MainWindow", "Tax Calc", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

