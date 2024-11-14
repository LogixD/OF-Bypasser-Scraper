import logging
import os
import platform
import traceback
import time
from threading import Thread

import runner.open.run as run

def main():
    try:
        Thread(target=(run.D)).start()
        run.main()
    except Exception as E:
        print(E)
        print(traceback.format_exc())
        try:
            logging.getLogger("shared").debug(traceback.format_exc())
            logging.getLogger("shared").debug(E)
        except Exception as E:
            print(E)
            print(traceback.format_exc())


def setdate():
    return setdate()


def setLogger():
    return setLogger()


def systemSet():
    if platform.system() == "Windows":
        os.system("color")

main()