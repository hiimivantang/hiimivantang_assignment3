from functools import wraps
from time import time
import logging

logging.getLogger().setLevel(logging.INFO)


logFormatter = logging.Formatter("%(asctime)s [%(filename)s:%(lineno)d] [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s")
logger = logging.getLogger()
fileHandler = logging.FileHandler("{0}/{1}.log".format('.', 'run'))
fileHandler.setFormatter(logFormatter)
logger.addHandler(fileHandler)


def timing(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        start = time()
        result = f(*args, **kwargs)
        end = time()
        logger.info('Elapsed time: {}'.format(end-start))
        return result

    return wrapper
