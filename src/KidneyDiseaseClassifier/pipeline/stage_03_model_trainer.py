from src.KidneyDiseaseClassifier.config.configuration import ConfigurationManager
from src.KidneyDiseaseClassifier import logger
from src.KidneyDiseaseClassifier.components.model_trainer import Training

STAGE_NAME='Model Training Stage'



class ModelTrainerPipeline:
    def __init__(self):
        pass
    def main(self):
        
        try:
            config = ConfigurationManager()
            training_config = config.get_training_config()
            training = Training(config=training_config)
            training.get_base_model()
            training.train_valid_generator()
            training.train()            
        except Exception as e:
            raise e
        

if __name__=="__main__":
    try:
        
        logger.info(f'>>>> stage {STAGE_NAME} started <<<<<<<<<')
        obj=ModelTrainerPipeline()
        obj.main()
        logger.info(f">>>> stage {STAGE_NAME} completed <<<<<<<<")
    except Exception as e:
        logger.error(f"ERROR !! {e}")
        raise e