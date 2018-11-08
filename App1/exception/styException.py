#   -*- coding: Utf-8 -*-

def styExc(args1):
    try:

        print "", int(args1)

        raise BussniessException,"this is BussniessException"

    except BaseException,e:
        print "exception:",e

    else:
        print "no exception"


class BussniessException(RuntimeError):
    def __init__(self, arg):
        self.args = arg
        print arg

if __name__ == '__main__':
    styExc(5)
