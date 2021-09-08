# coding: utf-8

def split_word_file(orgFile, newFile):
    f = open(orgFile, "r")
    fLines = f.readlines()
    f.close()
    fp = open(newFile, "w")
    for i in fLines:
        arr = i.split("、")
        for j in arr:
            if (j != '\n'):
                fp.write(j+'\n')
    fp.close()

def remove_empty_replicate_line(orgFile, newFile):
    f = open(orgFile, "r")
    fLines = f.readlines()
    f.close()
    fLines = set(fLines)
    fp = open(newFile, "w")
    for i in fLines:
        fp.write(i)
    fp.close()

if __name__ == "__main__":
    fileName = "备选.txt"
    newFile = "词库.txt"
    split_word_file(fileName, newFile)
    remove_empty_replicate_line(fileName, newFile)