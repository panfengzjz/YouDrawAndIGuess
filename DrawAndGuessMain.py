# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DrawAndGuess.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import random
import time
from PyQt5 import QtCore, QtGui, QtWidgets

import DrawAndGuessUi

class DAG_UI(DrawAndGuessUi.Ui_Form, QtCore.QObject):
    def signal(self, Form):
        self.randomWord_button.clicked.connect(self.randomWord)
        self.confirmWord_button.clicked.connect(self.confirmWord)
    
    def initSystem(self):
        fileName = "词库.txt"
        self.loadWord(fileName)
        self.click_random = 0
        
    def loadWord(self, fileName):
        f = open(fileName, 'r')
        lines = f.readlines()
        self.word_list = []
        for l in lines:
            self.word_list.append(l.strip())

    def randomWord(self):
        self.click_random += 1
        if (self.click_random >= 3):
            print("You cannot change words again")
            return
        for i in range(4):
            random.shuffle(self.word_list)
            item = self.word_list.pop(0)
            while (item == ""):
                random.shuffle(self.word_list)
                item = self.word_list.pop(0)
            eval("self.word{}_radioButton".format(i+1)).setText(item)

    def confirmWord(self):
        self.click_random = 0
        for i in range(4):
            button = eval("self.word{}_radioButton".format(i+1))
            if button.isChecked():
                self.current_word = button.text()
                print(self.current_word)
            button.setText("")
        self.count_down = 90
    
    def countDown(self):
        while (self.count_down):
            self.time_progressBar.setProperty("value", (90-self.count_down))
            self.count_down -= 1
            time.sleep(1)

if __name__ == "__main__":    
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = DAG_UI()
    ui.setupUi(Form)
    ui.initSystem()
    #ui.init_box(Form)
    #ui.init_thread()
    ui.signal(Form)
    Form.show()
    sys.exit(app.exec_())