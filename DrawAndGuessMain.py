# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DrawAndGuess.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import random
import time
import threading
from PyQt5 import QtCore, QtGui, QtWidgets

import DrawAndGuessUi

class DAG_UI(DrawAndGuessUi.Ui_Form, QtCore.QObject):
    _time_signal = QtCore.pyqtSignal()
    def signal(self, Form):
        self.randomWord_button.clicked.connect(self.randomWord)
        self.confirmWord_button.clicked.connect(self.confirmWord)
        self.start_Button.clicked.connect(self.resetGame)
        self._time_signal.connect(self.changeTimeBar)
    
    def initSystem(self):
        self.game_time = 90
        self.select_time = 30
        fileName = "词库.txt"
        self.loadWord(fileName)
        self.time_progressBar.setProperty("value", 0)
        self.click_random = 0
        self.count_down = self.select_time
    
    def resetGame(self):
        self.randomWord_button.setEnabled(True)
        self.confirmWord_button.setEnabled(True)
        #猜出答案就提前结束
        self.pause()
        self.count_down = self.select_time
        self.randomWord()
        #重置 progressBar
        self._time_signal.emit()
        self.resume()
        
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
            #清空词汇格中的备选项
            button = eval("self.word{}_radioButton".format(i+1))
            if button.isChecked():
                self.current_word = button.text()
                print(self.current_word)
            button.setText("")
        self.count_down = self.game_time
        self._time_signal.emit()
        #游戏中这两个按键的功能应该无效
        self.randomWord_button.setEnabled(False)
        self.confirmWord_button.setEnabled(False)
    
    def countDownSingal(self):
        while self.__running.isSet():
            self.__flag.wait()        
            while (self.count_down):
                self.__flag.wait()
                self._time_signal.emit()
                self.count_down -= 1
                time.sleep(1)
    
    def changeTimeBar(self):
        self.time_progressBar.setProperty("value", (self.count_down))

    def init_thread(self):
        self.t = threading.Thread(target=self.countDownSingal)
        self.__flag = threading.Event()
        self.__flag.set()
        self.__running = threading.Event()
        self.__running.set()
        self.t.setDaemon(True)
        self.t.start()
        self.pause()

    def pause(self):
        self.__flag.clear()     # 设置为False, 让线程阻塞

    def resume(self):
        self.__flag.set()    # 设置为True, 让线程停止阻塞

    def stop(self):
        self.__flag.set()       # 将线程从暂停状态恢复, 如何已经暂停的话
        self.__running.clear()  # 设置为False

if __name__ == "__main__":    
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = DAG_UI()
    ui.setupUi(Form)
    ui.initSystem()
    ui.init_thread()
    ui.signal(Form)
    Form.show()
    sys.exit(app.exec_())