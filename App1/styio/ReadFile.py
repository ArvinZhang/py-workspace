# -*- coding: Utf-8 -*-
import os


def readfile():
    if os.path.exists("/Users/arvin.chang/Documents/gitfile.txt"):
        print "true"
    else:
        print "false"

    if os.access("/Users/arvin.chang/Documents/gitfile.txt", os.R_OK):
        print "Given file path is exist."

    try:
        file = open("/Users/arvin.chang/Documents/gitfile.txt", "r+")
        # print  file.name
        print  file.closed
        print  file.mode
        print  file.softspace

        print  file.read()

        print "当前文件位置 : ", file.tell()

        # file.seek(0,2)

    except IOError:
        print("File is not accessible.")
    file.close()


def wirteFile():
    if os.access("/Users/arvin.chang/Documents/gitfile.txt", os.W_OK):
        print "Given file path is exist."

    try:
        file = open("/Users/arvin.chang/Documents/gitfile.txt", "a+")

        str1 = "this is test content\n"

        file.write(str1)
    except IOError:
        print "File is not accessible"

    finally:

        file.close()


def createFolder():
    os.mkdir("newdir")
    os.rmdir("newdir")
    os.remove("test.sh")


def styWith():
    if not os.access("/Users/arvin.chang/Documents/gitfile.txt", os.W_OK):
        print "Given file path is not exist."
        return

    with open("/Users/arvin.chang/Documents/gitfile.txt", "r+") as f:
        print "file content", f.read();


if __name__ == '__main__':
    # readfile()
    # wirteFile()
    # createFolder()
    styWith()
