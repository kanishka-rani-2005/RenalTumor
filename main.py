# from src.KidneyDiseaseClassifier import logger
# from src.KidneyDiseaseClassifier.pipeline.stage_01_data_ingestion import DataIngestionPipeline
# from src.KidneyDiseaseClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelPipeline
# from src.KidneyDiseaseClassifier.pipeline.stage_03_model_trainer import ModelTrainerPipeline
# from src.KidneyDiseaseClassifier.pipeline.stage_04_model_evaluation import ModelEvaluationPipeline



# if __name__=="__main__":
#     pass
#     try:
#         STAGE_NAME='Data Ingestion Stage'

#         logger.info(f'>>>> stage {STAGE_NAME} started <<<<<<<<<')
#         obj=DataIngestionPipeline()
#         obj.main()
#         logger.info(f">>>> stage {STAGE_NAME} completed <<<<<<<<")
#     except Exception as e:
#         logger.error(f"ERROR !! {e}")
#         raise e
    
#     try:
#         STAGE_NAME='Prepare Base Model Stage'

#         logger.info(f'>>>> stage {STAGE_NAME} started <<<<<<<<<')
#         obj=PrepareBaseModelPipeline()
#         obj.main()
#         logger.info(f">>>> stage {STAGE_NAME} completed <<<<<<<<")
#     except Exception as e:
#         logger.error(f"ERROR !! {e}")
#         raise e


#     try:
#         STAGE_NAME='Model Training Stage'

#         logger.info(f'>>>> stage {STAGE_NAME} started <<<<<<<<<')
#         obj=ModelTrainerPipeline()
#         obj.main()
#         logger.info(f">>>> stage {STAGE_NAME} completed <<<<<<<<")
#     except Exception as e:
#         logger.error(f"ERROR !! {e}")
#         raise e
    


#     try:
#         STAGE_NAME='Model Evaluation Stage'

#         logger.info(f'>>>> stage {STAGE_NAME} started <<<<<<<<<')
#         obj=ModelEvaluationPipeline()
#         obj.main()
#         logger.info(f">>>> stage {STAGE_NAME} completed <<<<<<<<")
#     except Exception as e:
#         logger.error(f"ERROR !! {e}")
#         raise e    
    


    