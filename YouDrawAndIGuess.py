# coding: utf-8
import random
import time

def load_word(fileName):
    f = open(fileName, 'r')
    lines = f.readlines()
    words = []
    
    for l in lines:
        words.append(l.strip())
    return words

def select_words(word_list, num=4):
    for i in range(num):
        random.shuffle(word_list)
        item = word_list.pop(0)
        while (item == ""):
            random.shuffle(word_list)
            item = word_list.pop(0)
        print("%d. %s" %(i+1, item))

def count_down(default_time=30):
    for i in range(0, default_time, 10):
        time.sleep(10)
        print("作画时间还剩%d秒" %(default_time-10-i))
    print("\n")

if __name__ == "__main__":
    fileName = "词库.txt"
    word_list = load_word(fileName)
    while True:
        select_words(word_list, 2)
        number = input("请从以上词汇中选一个作图（按q退出）：")
        if (number == 'q') or (number == 'Q'):
            break
        print("请在60秒内完成作画")
        count_down(60)
    print("本次游戏结束")
        