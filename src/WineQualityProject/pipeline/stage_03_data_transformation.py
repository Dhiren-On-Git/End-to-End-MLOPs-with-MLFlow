from WineQualityProject.config.configuration import ConfigurationManager
from WineQualityProject.components.data_transformation import DataTransformation
from WineQualityProject import logger

STAGE_NAME = " Data Transformation Stage"

class DataTransformationTrainingPipeline:
    def __init__(self) -> None:
        pass
    
    def main(self):
        # Pipeline for Data Transformation
        try:
            config = ConfigurationManager()
            data_transformation_config = config.get_data_transformation_config()
            data_transformation = DataTransformation(config=data_transformation_config)
            data_transformation.train_test_spliting()
        except Exception as e:
            raise e
        
if __name__ == '__main__':
    try:
        logger.info(f'>>>>>stage {STAGE_NAME} started <<<<< ')
        obj = DataTransformationTrainingPipeline()
        obj.main()
        logger.info(f'>>>>>stage {STAGE_NAME} completed<<<<<\n\nx=========x')
    except Exception as e:
        logger.exception(e)
        raise e