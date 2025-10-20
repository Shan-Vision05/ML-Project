import logging
import os
from datetime import datetime

LOG_FILE = f"ml_project_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
LOG_PATH = os.path.join(os.getcwd(), "logs")
os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)

LOG_FILE_PATH = os.path.join(LOG_PATH, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    level=logging.INFO,
    format='[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s',
)

if __name__ == "__main__":
    logging.info("Logger has been configured.")