from WineQualityProject.config.configuration import ConfigurationManager
from WineQualityProject.components.data_validation import DataValiadtion
from WineQualityProject import logger

STAGE_NAME = " Data Validation Stage"

class DataValidationTrainingPipeline:
    def __init__(self) -> None:
        pass
    
    def main(self):
        # Pipeline for Data Ingestion
        try:
            config = ConfigurationManager()
            data_validation_config = config.get_data_validation_config()
            # print("configuration path: ",data_validation_config.config)
            data_validation = DataValiadtion(config=data_validation_config)
            data_validation.validate_all_columns()
        except Exception as e:
            raise e
        
if __name__ == '__main__':
    try:
        logger.info(f'>>>>>stage {STAGE_NAME} started <<<<< ')
        obj = DataValidationTrainingPipeline()
        obj.main()
        logger.info(f'>>>>>stage {STAGE_NAME} completed<<<<<\n\nx=========x')
    except Exception as e:
        logger.exception(e)
        raise e