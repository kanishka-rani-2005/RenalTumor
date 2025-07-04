from src.KidneyDiseaseClassifier import logger
from src.KidneyDiseaseClassifier.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from src.KidneyDiseaseClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelPipeline

STAGE_NAME='Prepare Base Model Stage'


if __name__=="__main__":
    pass
    # try:
    #     logger.info(f'>>>> stage {STAGE_NAME} started <<<<<<<<<')
    #     obj=DataIngestionPipeline()
    #     obj.main()
    #     logger.info(f">>>> stage {STAGE_NAME} completed <<<<<<<<")
    # except Exception as e:
    #     logger.error(f"ERROR !! {e}")
    #     raise e
    
    # try:
    #     logger.info(f'>>>> stage {STAGE_NAME} started <<<<<<<<<')
    #     obj=PrepareBaseModelPipeline()
    #     obj.main()
    #     logger.info(f">>>> stage {STAGE_NAME} completed <<<<<<<<")
    # except Exception as e:
    #     logger.error(f"ERROR !! {e}")
    #     raise e


    # try:
    #     config = ConfigurationManager()
    #     training_config = config.get_training_config()
    #     training = Training(config=training_config)
    #     training.get_base_model()
    #     training.train_valid_generator()
    #     training.train()
        
        
    # except Exception as e:
    #     raise e
    
    


    