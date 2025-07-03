import os
from pathlib import Path
import logging

# Logging info 
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(threadName)-12.12s] [%(levelname)-8s]  %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)


project_name='KidneyDiseaseClassifier'

list_of_files=[
    '.github/workflows/.gitkeep',
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    f"src/{project_name}/config/configuration.py",
    'config/config.yaml',
    'requirements.txt',
    'setup.py',
    'templates/index.html',
    'static/style.css',
    'params.yaml',
    'dvc.yaml',
    'research/trials.ipynb'
]


for filepath in list_of_files:
    dirpath = Path(filepath) # required for windows to change backslash
    filedir,filename=os.path.split(filepath) # find directory and filename

    if filedir!="": # if directory is not there
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating directory :{filedir} for file name {filename}")

# if file donot exist
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath ,'w') as f:
            logging.info(f"Creating file :{filepath}")
            pass
    else:
        logging.info(f"File {filepath} already exists")