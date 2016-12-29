# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\codes\python\pyqt\taxCalc.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

from Ui_taxCalc import Ui_MainWindow

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


#class MyApp(QtGui.QMainWindow, Ui_MainWindow):
#    def __init__(self):
#        QtGui.QMainWindow.__init__(self)
#        Ui_MainWindow.__init__(self)
#        self.setupUi(self)

class MyApp(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        QtCore.QObject.connect(self.btCalcTax, QtCore.SIGNAL(_fromUtf8("clicked()")), self.fTaxCalc)

    def fTaxCalc(self):
        print type(self.tePrice.toPlainText())
        print self.tePrice.toPlainText()
        print type(self.tePrice.toPlainText().toInt())
        print self.tePrice.toPlainText().toInt()
        print type(self.sbTax.value())
        print self.sbTax.value()
        price, isInt = self.tePrice.toPlainText().toInt()
        if isInt:
            self.teResult.setText(str(price * self.sbTax.value()))
        else:
            self.teResult.clear()


#if __name__ == "__main__":
#    import sys
#    app = QtGui.QApplication(sys.argv)
#    MainWindow = QtGui.QMainWindow()
#    ui = Ui_MainWindow()
#    ui.setupUi(MainWindow)
#    MainWindow.show()
#    sys.exit(app.exec_())

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
