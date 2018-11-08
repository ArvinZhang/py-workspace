# -*- coding: UTF-8 -*-
import time
import calendar
import datetime
import ConnectionDB
import LamdaFun
from component import Script1
from component import Script2

# foreach operation
def styForeach(list2):
    for name in list2:
        # name += " String append"
        if name.endswith("append"):
            print "true"
            continue
        else:
            print "false"
    print name


# python 操作list集合练习
def styList():
    # list
    list = ["1", "2", "3", "4", "5", "6", "7", "8"];

    list1 = ["a", "b", "c", "d"];

    list2 = ["Arvin", "tester1", "tester2", "other"];

    # 输出指定的idex
    print 'println list ', list[1]

    # 输出index范围
    print 'println list ', list[1:5]

    print 'println list index 5 ', list[5]

    # update
    list2[0] = 'Zhang'

    print list2
    # remove
    del list2[3]
    # append
    list2.append("append list")

    print "my name is ", list2[0]
    return list2


# tuple
def styTuple():
    tup1 = ("Arvin", "Zhang", "Wu", "Xie", "Yuan")
    tup2 = (1, 2, 3, 4, 5, 6, 7, 8)
    print "tup1e length", len(tup1)

    # 'tuple' object does not support item assignment
    # tup1[0]="chang"

    for var in tup1:
        print var
    print tup1[1:]
    print tup1[-2]
    print "max value", max(tup2)
    print "min value", min(tup2)
    del tup1
    print  "after delete tuple"
    # print tup1


def styDict():
    dict1 = {"name": "wu", "age": 18, "occupation": "programmer"};
    print type(dict1)

    if dict1.has_key("age"):
        print "find keys age"

    print dict1.values()

    # print dict1.pop("age")

    # add
    dict1['income'] = "1W"
    for row in dict1:

        print  None == dict1.get("genar")

        print "set default:", dict1.setdefault(row)

        if dict1.setdefault("age") == 18:
            print  "find age is 18"

        if "age" == row and int == type(dict1[row]):
            #  find and update
            dict1[row] = 28
        else:
            print "can't not found age"
        print "type is", type(dict1[row])
        print  row + ":" + bytes(dict1[row])

    # copy dict
    dict2 = dict1.copy();
    # clear
    dict2.clear()

    print len(dict2)


def styTime():
    ticks = time.time()
    print ticks
    localTime = time.localtime(time.time())

    print time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())

    print  time.timezone
    cal=calendar.month(2018,11)

    print calendar.isleap(2020)
    print cal
    #datetime
    i=datetime.datetime.now();
    print i
    print i.year

def main():
        print  ">>>>>>>>>>>>>>>>>>mian test start>>>>>>>>>>>>>>>>>>"
        # var =styList()

        # styForeach(styList());

        # styTuple();

        #styDict();

        #styTime();

        #print LamdaFun.sum(1,2);

        #reload(LamdaFun)

        Script1.script1()

        Script2.script2()
        print  "<<<<<<<<<<<<<<<<<<mian test end<<<<<<<<<<<<<<<<<<"

if __name__ == '__main__':
    main()
