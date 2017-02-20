#!/usr/bin/python2.7
import logging
import sys

logger = logging.getLogger('testlog')

handler = logging.FileHandler('log/teste.log')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
handler.setFormatter(formatter)

ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.WARNING)

logger.addHandler(handler)
logger.addHandler(ch)
logger.setLevel(logging.DEBUG)

logging.disable(logging.INFO)
logging.disable(logging.ERROR)
logging.disable(logging.WARNING)

logger.error("some error occurred")
logger.info('some info msg')
logger.info('another info msg')
logger.info('last info msg')
logger.warning('last info msg')
