import os
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

log_dir = "logs"
log_filepath = os.path.join(log_dir,"running_logs.log")
os.makedirs(log_dir, exist_ok=True)


logging.basicConfig(
    level= logging.INFO,
    format= logging_str,

    handlers=[
        logging.FileHandler(log_filepath), # FileHandler will create a logging file
        logging.StreamHandler(sys.stdout) # StreamHandler will display the logs in running terminal
    ]
)

logger = logging.getLogger("WineQualityProjectLogger") # logger will be imported in any python file