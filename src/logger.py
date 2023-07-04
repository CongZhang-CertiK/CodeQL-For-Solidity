import logging
from src.config import CONFIG

logger = logging.getLogger('CodeQL-For-Solidity')
logger.setLevel(CONFIG.log_level)

# fh = logging.FileHandler('my_log.log')
#
# fh.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
ch.setLevel(CONFIG.log_level)

# formatter = logging.Formatter('[%(asctime)s][%(name)s][%(levelname)s] %(message)s')
formatter = logging.Formatter('[%(asctime)s][%(levelname)s] %(message)s')
# fh.setFormatter(formatter)
ch.setFormatter(formatter)

# logger.addHandler(fh)
logger.addHandler(ch)
