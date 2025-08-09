from src.DataScience_1.config.configuration import ConfigurationManager
from src.DataScience_1.components.data_model_evaluation import ModelEvaluation
from src.DataScience_1 import logger

STAGE_NAME="Data Model Evaliation Stage"

class DataModelEvaliationTrainingPipeline:
    def __init__(self):
        pass
    def initiate_data_Model_Evaliation(self):
        config=ConfigurationManager()
        data_modelEvaliation_config = config.get_model_evaluation_config()
        data_modelEvaliation = ModelEvaluation(config=data_modelEvaliation_config)
        data_modelEvaliation.log_into_mlflow()

if __name__ == '__main__':
    try:
        logger.info(f'>>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<<<')
        obj=DataModelEvaliationTrainingPipeline()
        obj.initiate_data_Model_Evaliation()
        logger.info(f'>>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<<<<')
    except Exception as e:
        logger.exception(e)
        raise e 