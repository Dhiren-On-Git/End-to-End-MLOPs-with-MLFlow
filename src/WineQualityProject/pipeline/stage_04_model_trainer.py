from WineQualityProject.config.configuration import ConfigurationManager
from WineQualityProject.components.model_trainer import ModelTrainer
from WineQualityProject import logger
from pathlib import Path

STAGE_NAME = " Model Training Stage"
STAGE_STATUS_FLAG = False  

class ModelTrainerTrainingPipeline:
    def __init__(self) -> None:
        pass
    
    def main(self):
        # Pipeline for Data Transformation
        
        try:
            config = ConfigurationManager()
            model_trainer_config = config.get_model_trainer_config()
            model_trainer_config = ModelTrainer(config=model_trainer_config)
            model_trainer_config.train()
        except Exception as e:
            raise e
            
        
if __name__ == '__main__':
    if STAGE_STATUS_FLAG == True:
        try:
            logger.info(f'>>>>>stage {STAGE_NAME} started <<<<< ')
            obj = ModelTrainerTrainingPipeline()
            obj.main()
            logger.info(f'>>>>>stage {STAGE_NAME} completed<<<<<\n\nx=========x')
        except Exception as e:
            logger.exception(e)
            raise e
    else:
        logger.info(f'Your data schema is not valid!!! Correct the data before transforming the data!')
        