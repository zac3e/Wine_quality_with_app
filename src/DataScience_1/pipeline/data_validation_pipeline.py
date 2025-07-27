from src.DataScience_1.config.configuration import ConfigurationManager
from src.DataScience_1.components.data_validation import DataValidation
from src.DataScience_1 import logger

STAGE_NAME="Data Validation Stage"

class DataValidationTrainingPipeline:
    def __init__(self):
        pass
    def initiate_data_validation(self):
        config=ConfigurationManager()
        Data_validation_config=config.get_data_validation_config()
        Data_validation=DataValidation(config=Data_validation_config)
        Data_validation.validate_all_columns()

if __name__ == '__main__':
    try:
        logger.info(f'>>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<<<')
        obj=DataValidationTrainingPipeline()
        obj.initiate_data_validation()
        logger.info(f'>>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<<<<')
    except Exception as e:
        logger.exception(e)
        raise e 
