from src.DataScience_1 import logger
from src.DataScience_1.pipeline.data_ingestio_pipeline import DataIngestionTrainingPipeline
from src.DataScience_1.pipeline.data_validation_pipeline import DataValidationTrainingPipeline
from src.DataScience_1.pipeline.data_transformation_pipeline import DataTrasformationTrainingPipeline
from src.DataScience_1.pipeline.data_model_trainer_pipeline import DataModelTrainerTrainingPipeline
logger.info('Welcome to my ml pipeline projetc')


STAGE_NAME="Data Ingestion Stage"

try:
    logger.info(f'>>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<<<')
    obj=DataIngestionTrainingPipeline()
    obj.initiate_data_ingestion()
    logger.info(f'>>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<<<<')
except Exception as e:
    logger.exception(e)
    raise e 

STAGE_NAME="Data Validation Stage"

try:
    logger.info(f'>>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<<<')
    obj=DataValidationTrainingPipeline()
    obj.initiate_data_validation()
    logger.info(f'>>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<<<<')
except Exception as e:
    logger.exception(e)
    raise e 

STAGE_NAME="Data Trasformation Stage"

try:
    logger.info(f'>>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<<<')
    obj=DataTrasformationTrainingPipeline()
    obj.initiate_data_Trasformation()
    logger.info(f'>>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<<<<')
except Exception as e:
    logger.exception(e)
    raise e 

STAGE_NAME="Data Model Trainer Stage"
try:
    logger.info(f'>>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<<<')
    obj=DataModelTrainerTrainingPipeline()
    obj.initiate_data_Model_trainer()
    logger.info(f'>>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<<<<')
except Exception as e:
    logger.exception(e) 
    raise e 