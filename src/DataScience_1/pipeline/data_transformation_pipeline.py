from src.DataScience_1.config.configuration import ConfigurationManager
from src.DataScience_1.components.data_transformation import DataTransformation
from src.DataScience_1 import logger

STAGE_NAME="Data Transformation Stage"

class DataTrasformationTrainingPipeline:
    def __init__(self):
        pass
    def initiate_data_Trasformation(self):
        config=ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config=data_transformation_config)
        data_transformation.train_test_spliting()

if __name__ == '__main__':
    try:
        logger.info(f'>>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<<<')
        obj=DataTrasformationTrainingPipeline()
        obj.initiate_data_Trasformation()
        logger.info(f'>>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<<<<')
    except Exception as e:
        logger.exception(e)
        raise e 
