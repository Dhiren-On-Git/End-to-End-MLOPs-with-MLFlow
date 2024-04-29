from WineQualityProject import logger
from WineQualityProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

logger.info('Welcome to our custom logging')

STAGE_NAME = " Data Ingestion Stage"

try:
        logger.info(f'>>>>>stage {STAGE_NAME} started <<<<< ')
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f'>>>>>stage {STAGE_NAME} completed<<<<<\n\nx=========x')
except Exception as e:
        logger.exception(e)
        raise e