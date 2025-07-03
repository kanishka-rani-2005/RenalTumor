import os 
import sys
import logging


# %(asctime)s: Time the log message was created.
# %(levelname)s: Log level (INFO, ERROR, etc.)
# %(module)s: Name of the module where the log is coming from.
# %(message)s: The actual log message.

logging_str="[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"


log_dir='logs'
log_filepath=os.path.join(log_dir,'running_logs.log')

os.makedirs(log_dir,exist_ok=True)


logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    datefmt='%a, %d %b %Y %H:%M:%S',
    handlers=[
        logging.FileHandler(log_filepath), #Logs go to file.
        logging.StreamHandler(sys.stdout) #Logs also appear on the terminal/console.
    ]
)

logger=logging.getLogger('KidneyDiseaseClassifier') #Creates (or retrieves) a named logger called 'DiseaseLogger'
