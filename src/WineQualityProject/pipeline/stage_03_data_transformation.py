from WineQualityProject.config.configuration import ConfigurationManager
from WineQualityProject.components.data_transformation import DataTransformation
from WineQualityProject import logger
from pathlib import Path

STAGE_NAME = " Data Transformation Stage"
STAGE_STATUS_FLAG = False  

class DataTransformationTrainingPipeline:
    def __init__(self) -> None:
        pass
    
    def main(self):
        # Pipeline for Data Transformation
        with open(Path('artifacts\data_validation\status.txt')) as f:
            status = f.read().split(" ")[-1]
        try:
            if status == "True":
                STAGE_STATUS_FLAG = True                
                config = ConfigurationManager()
                data_transformation_config = config.get_data_transformation_config()
                data_transformation = DataTransformation(config=data_transformation_config)
                data_transformation.train_test_spliting()
            else:
                raise Exception("Your data schema is not valid! Data Transformation is not Possible!")
        except Exception as e:
            print(e)
            
        
if __name__ == '__main__':
    if STAGE_STATUS_FLAG == True:
        try:
            logger.info(f'>>>>>stage {STAGE_NAME} started <<<<< ')
            obj = DataTransformationTrainingPipeline()
            obj.main()
            logger.info(f'>>>>>stage {STAGE_NAME} completed<<<<<\n\nx=========x')
        except Exception as e:
            logger.exception(e)
            raise e
    else:
        logger.info(f'Your data schema is not valid!!! Correct the data before transforming the data!')
        