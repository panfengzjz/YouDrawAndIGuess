# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DrawAndGuessUi.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(243, 327)
        self.randomWord_button = QtWidgets.QPushButton(Form)
        self.randomWord_button.setGeometry(QtCore.QRect(30, 200, 81, 23))
        self.randomWord_button.setObjectName("randomWord_button")
        self.confirmWord_button = QtWidgets.QPushButton(Form)
        self.confirmWord_button.setGeometry(QtCore.QRect(134, 200, 81, 23))
        self.confirmWord_button.setObjectName("confirmWord_button")
        self.titleBlank = QtWidgets.QTextEdit(Form)
        self.titleBlank.setGeometry(QtCore.QRect(20, 20, 201, 41))
        self.titleBlank.setObjectName("titleBlank")
        self.start_Button = QtWidgets.QPushButton(Form)
        self.start_Button.setGeometry(QtCore.QRect(40, 70, 161, 23))
        self.start_Button.setObjectName("start_Button")
        self.word1_radioButton = QtWidgets.QRadioButton(Form)
        self.word1_radioButton.setGeometry(QtCore.QRect(40, 110, 111, 16))
        self.word1_radioButton.setText("")
        self.word1_radioButton.setObjectName("word1_radioButton")
        self.word2_radioButton = QtWidgets.QRadioButton(Form)
        self.word2_radioButton.setGeometry(QtCore.QRect(40, 130, 111, 16))
        self.word2_radioButton.setText("")
        self.word2_radioButton.setObjectName("word2_radioButton")
        self.word4_radioButton = QtWidgets.QRadioButton(Form)
        self.word4_radioButton.setGeometry(QtCore.QRect(40, 170, 111, 16))
        self.word4_radioButton.setText("")
        self.word4_radioButton.setObjectName("word4_radioButton")
        self.word3_radioButton = QtWidgets.QRadioButton(Form)
        self.word3_radioButton.setGeometry(QtCore.QRect(40, 150, 111, 16))
        self.word3_radioButton.setText("")
        self.word3_radioButton.setObjectName("word3_radioButton")
        self.time_progressBar = QtWidgets.QProgressBar(Form)
        self.time_progressBar.setGeometry(QtCore.QRect(20, 250, 151, 21))
        self.time_progressBar.setMaximum(90)
        self.time_progressBar.setProperty("value", 24)
        self.time_progressBar.setFormat("")
        self.time_progressBar.setObjectName("time_progressBar")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(150, 240, 71, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setCursorPosition(1)
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.randomWord_button.setText(_translate("Form", "换一组"))
        self.confirmWord_button.setText(_translate("Form", "确认选词"))
        self.titleBlank.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-weight:600;\">你画我猜</span></p></body></html>"))
        self.start_Button.setText(_translate("Form", "开始游戏"))
        self.lineEdit.setText(_translate("Form", "0"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
