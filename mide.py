# -*- coding:utf-8 -*-

"""
:author bug320
:purpose purpose
:time 2017-09-27
"""

from create_py import createmode as cm

import os
import sys
import getopt


class IDE(object):
    def __init__(self):
        pass

    def createfile(self, fname=None):
        co = cm.CMode()
        co.tofile(fname=fname)
        pass

    pass


def perror():
    print("mide.py -c filename")
    print("     or mide.py --create_file filename")
    pass

def main(argv):
    ide = IDE()
    if not len(argv):
        perror()
        pass
    try:
        opts, args = getopt.getopt(argv,  "hc:", ["create_file="])
        # if len(args) == 0:
        #     perror()
        #     print(len(args))
        #     exit(0)
        #     pass
        pass
    except getopt.GetoptError:
        perror()
        sys.exit(2)
        pass
    for opt, arg in  opts:
        if opt == "-h":
            perror()
            pass
        elif opt in ("-c","--create_file"):
            ide.createfile(fname=arg)
            pass
        else:
            pass

        pass
    pass

if __name__ == "__main__":
    # ide  = IDE()
    main(sys.argv[1:])
    pass
