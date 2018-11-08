# -*- coding: Utf-8 -*-

def funs():
    tuple1 = ("1", "2", "3", "a", "b", 0);

    print "bulid in function"
    print "absolute value", abs(-998)
    print  "all method:", all(tuple1)
    for row in tuple1:

        if str == type(row):

            print ord(row)
        else:
            print  "not str", row
        # hash code
        # print  hash(row)
        print memoryview(row)


class Demo1(object):
    @staticmethod
    def outPrint():
        print "this is static method"


class Demo2(object):
    def outPrint(self):
        print "this is  general method";


class Demo3(object):

    def __init__(self):
        pass


def sty_map():
      print  map(lambda x: x * 10, [1, 3, 8, 9, 87])


def styFilter():
    print filter(lambda x:x>10,[10,19,18,29,8,9,23])

def sty_zip():
    tuple1=(1,2,3);
    tuple2 = ("a", "b", "c");
    tuple3 = ("我", "是", "谁");
    zipped=zip(tuple1, tuple2,tuple3)
    print zipped
    print zip(*zipped)



if __name__ == '__main__':

    # funs()
    # static method
    # Demo1.outPrint()

    # general method
    # demo2 = Demo2()
    # demo2.outPrint()
    # sty_map()
    # styFilter()
    sty_zip()
