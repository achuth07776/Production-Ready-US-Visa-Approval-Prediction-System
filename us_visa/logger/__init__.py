import logging
import os
from datetime import datetime


# Get the project root directory
PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..")
)

# Create logs directory inside project root
LOG_DIR = os.path.join(PROJECT_ROOT, "logs")

os.makedirs(LOG_DIR, exist_ok=True)


# Create a unique log file name for every run
LOG_FILE = datetime.now().strftime("%m_%d_%Y_%H_%M_%S_%f.log")

LOG_PATH = os.path.join(LOG_DIR, LOG_FILE)


# Configure logging
logging.basicConfig(
    filename=LOG_PATH,
    format="[%(asctime)s] %(name)s %(levelname)s - %(message)s",
    level=logging.DEBUG,
    force=True
)


# Create logger
logger = logging.getLogger("us_visa")