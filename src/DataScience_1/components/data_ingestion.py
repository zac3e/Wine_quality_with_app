import os 
import urllib.request as request 
from src.DataScience_1 import logger
import zipfile
from src.DataScience_1.entity.config_entity import (DataIngestionconfig)

### Component_data ingestion
class DataIngestion:
    def __init__(self, config:DataIngestionconfig):
        self.config=config

    #  """ Downlloading the file """   
    def dowload_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename,headers =request.urlretrieve(
                url=self.config.source_URL,
                filename=self.config.local_data_file)
            
            logger.info(f"{filename} dowload with following info ! {headers}")
        else:
            logger.info(f"File alredy exists")

    def extract_zip_file(self):
        unzip_path=self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)