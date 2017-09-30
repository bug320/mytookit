# -*- coding:utf-8 -*-

"""
:author bug320
:purpose purpose
:time 2017-09-30
"""


import sys
import termios
import select


class Setter(object):
    fd = sys.stdin.fileno()
    oldf = termios.tcgetattr(fd)
    newf = termios.tcgetattr(fd)

    def __init__(self,echo=True, icanon=True):
        self.echo = echo
        self.icanon = icanon
        pass

    def update(self):
        Setter.newf[3] = Setter.newf[3] & (termios.ECHO
                                           if self.echo else ~termios.ECHO)
        Setter.newf[3] = Setter.newf[3] & (termios.ICANON
                                           if self.icanon else ~termios.ICANON)
        termios.tcsetattr(Setter.fd, termios.TCSADRAIN, Setter.newf)
        pass

    def reset(self):
        termios.tcsetattr(Setter.fd, termios.TCSADRAIN, Setter.oldf)
        return sys.stdin
        pass
    pass

def kin(func,echo=True,icanon=True):
    def _kin(*args,**argv):
        seter = Setter(echo,icanon)
        try:
            seter.update()
            func()
            return func
            pass
        finally:
            seter.reset()
            pass
        pass
    return _kin
    pass

@kin
def test():
    a = raw_input("input1")
    print("have input {0}".format(a))
    pass


if __name__ == "__main__":
    # try:
    #     tcset = Setter()
    #     print("开始")
    #     # old = sys.stdin
    #     # print("老的读取1个字符")
    #     # c = old.read(1)
    #     # print("读取到 {0}".format(c))
    #     # sys.stdin.flush()
    #     tcset.echo = False
    #     necho = tcset.stdin()
    #     print("关闭回显")
    #     a = raw_input("输入")
    #     print("读取的结果为{0}".format(a))
    #     pass
    # finally:
    #     tcset.reset()
    #     pass

    test()
    b = raw_input("input:")
    print("have input {0}".format(b))


    pass
