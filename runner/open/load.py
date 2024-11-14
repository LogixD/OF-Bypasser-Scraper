import logging
import os
import platform
import traceback

import runner.open.run as run
import utils.args.accessors.read as read_args
import utils.checkers as checkers
import utils.config.config as config_
import utils.dates as dates
import utils.logs.globals as log_globals
import utils.logs.logger as logger
import utils.logs.logs as logs
import utils.paths.manage as paths_manage
import utils.system.system as system


def main():
    try:
        systemSet()
        args_loader()
        setdate()
        readConfig()
        setLogger()
        make_folder()
        check()
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


def args_loader():
    read_args.retriveArgs()


def setdate():
    dates.resetLogDateVManager()


def setLogger():
    log_globals.init_values()
    logger.get_shared_logger()
    logs.discord_warning()
    logger.start_threads()


def systemSet():
    system.setName()
    system.set_eventloop()
    if platform.system() == "Windows":
        os.system("color")


def readConfig():
    config_.read_config()


def make_folder():
    paths_manage.make_folders()


def check():
    checkers.check_config()
    checkers.check_config_key_mode()
