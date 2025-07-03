from src.KidneyDiseaseClassifier.config.configuration import ConfigurationManager
from src.KidneyDiseaseClassifier import logger
from src.KidneyDiseaseClassifier.components.data_ingestion import DataIngestion

STAGE_NAME='Data Ingestion Stage'

class DataIngestionPipeline:
    def __init__(self):
        pass
    def main(self):
        try:
            config=ConfigurationManager()
            data_ingestion_config=config.get_data_ingestion_config()
            data_ingestion=DataIngestion(config=data_ingestion_config)
            data_ingestion.download_file()
            data_ingestion.extract_zip_file()
            logger.info('Data Ingestion Complete !!!')
        except Exception as e:
            logger.error(f"ERROR !! {e}")
            raise e
        

if __name__=="__main__":
    try:
        logger.info(f'>>>> stage {STAGE_NAME} started <<<<<<<<<')
        obj=DataIngestionPipeline()
        obj.main()
        logger.info(f">>>> stage {STAGE_NAME} completed <<<<<<<<")
    except Exception as e:
        logger.error(f"ERROR !! {e}")
        raise e