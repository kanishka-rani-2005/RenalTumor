from src.KidneyDiseaseClassifier import logger
from src.KidneyDiseaseClassifier.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from src.KidneyDiseaseClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelPipeline

STAGE_NAME='Prepare Base Model Stage'


# if __name__=="__main__":
#     try:
#         logger.info(f'>>>> stage {STAGE_NAME} started <<<<<<<<<')
#         obj=DataIngestionPipeline()
#         obj.main()
#         logger.info(f">>>> stage {STAGE_NAME} completed <<<<<<<<")
#     except Exception as e:
#         logger.error(f"ERROR !! {e}")
#         raise e



if __name__=="__main__":
    try:
        logger.info(f'>>>> stage {STAGE_NAME} started <<<<<<<<<')
        obj=PrepareBaseModelPipeline()
        obj.main()
        logger.info(f">>>> stage {STAGE_NAME} completed <<<<<<<<")
    except Exception as e:
        logger.error(f"ERROR !! {e}")
        raise e