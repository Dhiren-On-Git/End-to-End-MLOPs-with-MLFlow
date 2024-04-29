from WineQualityProject.config.configuration import ConfigurationManager
from WineQualityProject.components.data_ingestion import DataIngestion
from WineQualityProject import logger

STAGE_NAME = " Data Ingestion Stage"

class DataIngestionTrainingPipeline:
    def __init__(self) -> None:
        pass
    
    def main(self):
        # Pipeline for Data Ingestion
        try:
            config = ConfigurationManager()
            data_ingestion_config = config.get_data_ingestion_config()
            data_ingestion = DataIngestion(config=data_ingestion_config)
            data_ingestion.download_file()
            data_ingestion.extract_zip_file()
        except Exception as e:
            raise e
        
if __name__ == '__main__':
    try:
        logger.info(f'>>>>>stage {STAGE_NAME} started <<<<< ')
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f'>>>>>stage {STAGE_NAME} completed<<<<<\n\nx=========x')
    except Exception as e:
        logger.exception(e)
        raise e
        
        


