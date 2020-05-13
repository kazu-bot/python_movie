"""
CRITICAL
ERROR
WARNING
INFO
DEBUG
"""

import logging

logging.basicConfig(filename='test.log',level=logging.DEBUG)

logging.critical('critical')
logging.error('error')
logging.warning('warning')
logging.info('info %s' % 'test')
logging.debug('debug')

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.debug('debug')