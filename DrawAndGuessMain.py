# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DrawAndGuess.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

import DrawAndGuessUi

class DAG_UI(DrawAndGuessUi.Ui_Form, QtCore.QObject):
    def signal(self, Form):
        pass

if __name__ == "__main__":    
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = DAG_UI()
    #ui.init_box(Form)
    #ui.init_thread()
    #ui.signal(Form)
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())