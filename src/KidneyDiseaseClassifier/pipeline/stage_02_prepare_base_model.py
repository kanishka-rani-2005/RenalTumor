from src.KidneyDiseaseClassifier.config.configuration import ConfigurationManager
from src.KidneyDiseaseClassifier import logger
from src.KidneyDiseaseClassifier.components.prepare_base_model import PrepareBaseModel

STAGE_NAME='Prepare Base Model Stage'



class PrepareBaseModelPipeline:
    def __init__(self):
        pass
    def main(self):
        try:
            config=ConfigurationManager()
            get_prepare_base_model_config=config.get_prepare_base_model_config()
            preparebasemodel=PrepareBaseModel(config=get_prepare_base_model_config)
            preparebasemodel.get_base_model()
            preparebasemodel.update_base_model()
            logger.info('Prepare Base Model Complete !!!')
        except Exception as e:
            logger.error(f"ERROR !! {e}")
            raise e
        

if __name__=="__main__":
    try:
        logger.info(f'>>>> stage {STAGE_NAME} started <<<<<<<<<')
        obj=PrepareBaseModelPipeline()
        obj.main()
        logger.info(f">>>> stage {STAGE_NAME} completed <<<<<<<<")
    except Exception as e:
        logger.error(f"ERROR !! {e}")
        raise e