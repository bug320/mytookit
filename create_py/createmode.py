# -*- coding:utf-8 -*-

from time import ctime, strptime, strftime

import os


class CMode(object):

    def __init__(self, author="bug320"):
        self._encoding = "utf-8"
        self._author = author
        self._purpose = "purpose"
        self._time = "xxxx-xx-xx"
        self.set_time()
        pass

    @property
    def encoding(self):
        return self._encoding
        pass

    @property
    def author(self):
        return self._author
        pass

    @property
    def purpose(self):
        return self._purpose
        pass

    @property
    def time(self):
        return self._time
        pass

    def set_time(self, time=None):
        if time:
            self._time = time
            pass
        else:
            # "%Y-%m-%d %H:%M:%S"
            # Thu Sep 28 00:41:37 2017
            # strptime(a, "%Y-%m-%d %H:%M:%S")
            time = ctime()
            time = strptime(time, "%a %b %d %H:%M:%S %Y")
            time = strftime("%Y-%m-%d", time)
            self._time = time
            pass
        pass

    def __str__(self):
        return '''# -*- coding:{self._encoding} -*-

"""
:author {self._author}
:purpose {self._purpose}
:time {self._time}
"""


if __name__ == "__main__":
    pass'''.format(self=self)
        pass

    def tofile(self, fname=None):
        pwd = os.getcwd()
        time = ctime()
        time = strptime(time, "%a %b %d %H:%M:%S %Y")
        time = strftime("%Y%m%d%H%M", time)
        fname = fname if fname else "Unname{0}.py".format(time)
        if not fname.endswith(".py"):
            fname += ".py"
            pass
        with open(fname, "w") as writer:
            writer.write(str(self))
            pass
        print(pwd)
        pass

    pass


if __name__ == "__main__":
    # print("__START")
    # para = {
    #     "encoding": "utf-8",
    #     "author": "bug320",
    #     "purpose": "purpose one",
    #     "time": "2017-09-27"
    # }
    # print(BASE_MODE.format(**para))
    # print("__END")
    cmode = CMode()
    # cmode.set_time()
    # print(str(cmode))
    cmode.tofile()
    pass
