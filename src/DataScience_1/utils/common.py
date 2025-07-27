import os 
import yaml
from src.DataScience_1 import logger
import json
import joblib
from typeguard import typechecked
from box import ConfigBox
from pathlib import Path
from typing import Any
from box.exceptions import BoxValueError

@typechecked
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """reads yaml file and returns

    Args:
        path_to_yaml (str): path like input

    Raises:
        ValueError: if yaml file is empty
        e: empty file

    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    
@typechecked
def create_directories(path_to_directories:list, verbose=True):
    """Creaste a list of directories 

    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optinal):ignore if multiple dirs is ti be created
    """

    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f'Created directory at_{path}')

@typechecked
def save_json(path:Path, data:dict):
    with open(path,'w') as f:
        json.dump(data,f,indent=4)

    logger.info(f'json file saved at {path}')    

def load_json(path:Path, data:dict):
    with open(path) as f:
        content=json.load(f)

    logger.info(f'json file loaded from:{path}')
    return ConfigBox(content)   

def save_bin(data: Any, path: Path):
    """save binary file

    Args:
        data (Any): data to be saved as binary
        path (Path): path to binary file
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"binary file saved at: {path}")

@typechecked
def load_bin(path: Path) -> Any:
    """load binary data

    Args:
        path (Path): path to binary file

    Returns:
        Any: object stored in the file
    """
    data = joblib.load(path)
    logger.info(f"binary file loaded from: {path}")
    return data