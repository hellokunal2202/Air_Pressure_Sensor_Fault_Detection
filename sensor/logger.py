import logging 
import pandas as pd
from datetime import datetime
import os

LOG_FILE_NAME = f"{datetime.now().strftime('%m%d%Y_%H%M%S')}.log"
LOG_dir = "logs"

os.makedirs(LOG_dir,exist_ok=True)
LOG_FILE_PATH = os.path.join(LOG_dir,LOG_FILE_NAME)
logging.basicConfig(
    filename=LOG_FILE_PATH,
    level=logging.INFO,
    format="%(asctime)s:%(levelname)s:%(message)s"
    )