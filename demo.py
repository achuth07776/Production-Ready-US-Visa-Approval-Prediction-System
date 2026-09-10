from us_visa.logger import logging
from us_visa.exception import USvisaException
import sys
try:
    # Some code that might raise an exception
    a=2/0
except Exception as e:
    raise USvisaException(e, sys)

#logging.info("welcom to Logs")