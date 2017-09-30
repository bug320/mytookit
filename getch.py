# -*- coding:utf-8 -*-


import sys
import termios
import select
import time


class Getch(object):
    def __init__(self):
        pass

    def __call__(self):
        fd = sys.stdin.fileno()
        old = termios.tcgetattr(fd)
        new = termios.tcgetattr(fd)
        # turn off echo and press-enter
        new[3] = new[3] & ~termios.ECHO & ~termios.ICANON
        try:
            termios.tcsetattr(fd, termios.TCSADRAIN, new)
            # print("before")
            return sys.stdin.read(1)
            # while True:
            #     char = sys.stdin.read(1)
            #     print 'get:', char
            #     if char == 'q':
            #         break
        finally:
            # print("finally")
            termios.tcsetattr(fd, termios.TCSADRAIN, old)
        pass
    pass

def kbhit():
    r = select.select([sys.stdin], [], [], 0.01)
    rcode = ""
    if len(r[0]):
        rcode = sys.stdin.read(1)
        print("hh")
        pass
    return rcode
    pass

if __name__ == "__main__":
    getch = Getch()
    a = getch()
    print("hello,{0}".format(a))
    while 1:
        c = kbhit()
        print("len(c)={0}".format(c))
        print(c)
        if c == 'a':
            break
            pass
        if len(c):
            print("input {0}".format(c))
            pass
        time.sleep(1)
        pass
    pass
