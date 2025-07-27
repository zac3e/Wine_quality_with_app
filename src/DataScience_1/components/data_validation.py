import os 
import urllib.request as request 
from src.DataScience_1 import logger
import zipfile
from src.DataScience_1.entity.config_entity import (DataValidationConfig)
import pandas as pd 

class DataValidation:
    def __init__ (self, config:DataValidationConfig):
        self.config=config

    def validate_all_columns(self)->bool:
        try:
            validation_status=None

            data=pd.read_csv(self.config.unzip_data_dir)
            all_columns=list(data.columns)
            all_schema=self.config.all_schema.keys()


            for columns in all_columns:
                if columns not in all_schema:
                    validation_status=False
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f'Validation status :{validation_status}')
                else:
                    validation_status=True
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f'Validation status :{validation_status}')

            return validation_status

        except Exception as e:
            raise e     