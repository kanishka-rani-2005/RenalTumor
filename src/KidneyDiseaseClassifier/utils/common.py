import os
from box.exceptions import BoxValueError
import yaml
from src.KidneyDiseaseClassifier import logger
import json
import joblib

from ensure import ensure_annotations
import base64
from typing import Any
from pathlib import Path
from box import ConfigBox


@ensure_annotations
def read_yaml(path_to_yaml:Path)->ConfigBox:
    with open(path_to_yaml, 'r') as file:
        try:
            data = yaml.safe_load(file)
            logger.info('Loading Yaml file succesfully.')
            return ConfigBox(data)       #df['key'] -> d.key easy acess 
        except BoxValueError:
            logger.error('Error in loading yaml file.')
            raise BoxValueError('Error in loading yaml file')
        except Exception as e:
            logger.error(f'Error in loading yaml file: {e}')
            raise e


@ensure_annotations
def create_directories(path_to_directories:list,verbose=True):
    for path in path_to_directories:
        try:
            os.makedirs(path, exist_ok=True)
            if verbose:
                logger.info(f'Directory created at: {path}')
        except Exception as e:
            logger.error(f'Error in creating directory: {e}')
            raise e
        
@ensure_annotations
def save_json(path:Path,data:dict):
    try:
        with open(path, 'w') as file:
            json.dump(data, file, indent=4)
            logger.info(f'Json file saved at: {path}')
    except Exception as e:
        logger.error(f'Error in saving json file: {e}')
        raise e
    
@ensure_annotations
def load_json(path:Path)->ConfigBox:
    try:
        with open(path, 'r') as file:
            data = json.load(file)
            logger.info('Loading Json file succesfully.')
            return ConfigBox(data)
    except Exception as e:
        logger.error(f'Error in loading json file: {e}')
        raise e
    
@ensure_annotations
def save_yaml(path:Path,data:dict):
    try:
        with open(path, 'w') as file:
            yaml.dump(data, file, default_flow_style=False)
            logger.info(f'Yaml file saved at: {path}')
    except Exception as e:
        logger.error(f'Error in saving yaml file: {e}')
        raise e
    
@ensure_annotations
def save_bin(data:Any,path:Path):
    try:
        with open(path, 'wb') as file:
            file.write(data)
            logger.info(f'Binary file saved at: {path}')
    except Exception as e:
        logger.error(f'Error in saving binary file: {e}')
        raise e
    
@ensure_annotations
def load_bin(path:Path)->Any:
    try:
        with open(path, 'rb') as file:
            data = file.read()
            logger.info('Loading binary file succesfully.')
            return data
    except Exception as e:
        logger.error(f'Error in loading binary file: {e}')
        raise e
    

@ensure_annotations
def get_size(path:Path)->str:
    try:
        size = round(os.path.getsize(path)/1024)
        return f'{size} KB'
    except Exception as e:
        logger.error(f'Error in getting size of file: {e}')
        raise e
    

@ensure_annotations
def decodeImage(imgstring,filename):
    try:
        imgdata=base64.b64decode(imgstring)
        with open(filename, 'wb') as file:
            file.write(imgdata)
            logger.info(f'Image saved at: {filename}')
    except Exception as e:
        logger.error(f'Error in decoding image: {e}')
        raise e
    

@ensure_annotations
def encodeImageIntoBase64(croppedImagePath):
    try:
        with open(croppedImagePath, "rb") as f:
            encoded_string = base64.b64encode(f.read()).decode('utf-8')
            return encoded_string
    except Exception as e:
        logger.error(f'Error in encoding image into base64: {e}')
        raise e