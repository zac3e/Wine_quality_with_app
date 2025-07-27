from src.DataScience_1.config.configuration import ConfigurationManager
from src.DataScience_1.components.data_model_trainer import ModelTrainer
from src.DataScience_1 import logger

STAGE_NAME="Data Model Trainer Stage"

class DataModelTrainerTrainingPipeline:
    def __init__(self):
        pass
    def initiate_data_Model_trainer(self):
        config=ConfigurationManager()
        data_modelTrainer_config = config.get_model_trainer_config()
        data_modelTrainer = ModelTrainer(config=data_modelTrainer_config)
        data_modelTrainer.train()

if __name__ == '__main__':
    try:
        logger.info(f'>>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<<<')
        obj=DataModelTrainerTrainingPipeline()
        obj.initiate_data_Model_trainer()
        logger.info(f'>>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<<<<')
    except Exception as e:
        logger.exception(e)
        raise e 