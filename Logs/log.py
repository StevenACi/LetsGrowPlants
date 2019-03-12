import sys
import logging


_LOGGER = None
LOG_LEVEL = logging.DEBUG
LOGGER_NAME = "Lets Grow Plants!"
LOGGING_PATH = "../logs/LetsGrowPlants_log.txt"

# Make a level that will always print
logging.ALWAYS = 100
logging.addLevelName(logging.ALWAYS, "ALWAYS")




def init_logger():
    global _LOGGER
    _LOGGER = logging.getLogger(LOGGER_NAME)
    fmt = "{asctime} | {module} | {levelname} ||| {message}"
    fmtr = logging.Formatter(fmt=fmt, style="{")
    strm_handler = logging.StreamHandler(sys.stdout)

    strm_handler.setLevel(LOG_LEVEL)
    strm_handler.setFormatter(fmtr)

    file_handler = logging.FileHandler(LOGGING_PATH, mode='w')
    #file_handler = logging.FileHandler(LOGGING_PATH, mode='a')
    file_handler.setLevel(logging.DEBUG) # Always log to file
    file_handler.setFormatter(fmtr)

    _LOGGER.addHandler(strm_handler)
    _LOGGER.addHandler(file_handler)
    _LOGGER.setLevel(LOG_LEVEL)

def ALWAYS(msg):
    __log(msg, logging.ALWAYS)

def FATAL(msg):
    __log(msg, logging.CRITICAL)

def CRITICAL(msg):
    __log(msg, logging.CRITICAL)

def ERROR(msg):
    __log(msg, logging.ERROR)

def WARN(msg):
    __log(msg, logging.WARNING)

def WARNING(msg):
    __log(msg, logging.WARNING)

def INFO(msg):
    __log(msg, logging.INFO)

def DEBUG(msg):
    __log(msg, logging.DEBUG)



def __log(msg, msg_level):
    global _LOGGER
    if _LOGGER is None:
        init_logger()

    if _LOGGER:
        _LOGGER.log(msg_level, msg)
    else:
        raise Exception("Logger was not initialized")