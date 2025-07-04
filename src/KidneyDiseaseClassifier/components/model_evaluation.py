

from src.KidneyDiseaseClassifier.entity.config_entity import EvaluationConfig
import tensorflow as tf
from pathlib import Path

from src.KidneyDiseaseClassifier.utils.common import save_json
import mlflow
import mlflow.keras
from urllib.parse import urlparse

class Evaluation:
    def __init__(self,config:EvaluationConfig):
        self.config=config
    def train_valid_generator(self):
        datagenerator_kwargs = dict(
            rescale=1./255,
            validation_split=0.20
        )

        dataflow_kwargs = dict(
            target_size=self.config.params_image_size[:-1],
            batch_size=self.config.params_batch_size,
            class_mode='categorical'
        )

        valid_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(**datagenerator_kwargs)
        self.valid_generator = valid_datagenerator.flow_from_directory(
            directory=self.config.training_data,
            subset="validation",
            shuffle=False,
            **dataflow_kwargs
        )

      
       

    @staticmethod
    def load_model(path:Path)->tf.keras.Model:
        return tf.keras.models.load_model(path)
    

    def evaluation(self):
        self.model=self.load_model(self.config.path_of_model)
        self.train_valid_generator()
        self.score=self.model.evaluate(self.valid_generator)
        self.save_score()
        self.model.save("model.keras")

    
    def save_score(self):
        scores={'loss': self.score[0], 'accuracy':self.score[1]}
        save_json(path=Path("scores.json"),data=scores)

    def log_into_mlflow(self):
        mlflow.set_registry_uri(self.config.mlflow_url)
        tracking_url_type_score=urlparse(mlflow.get_tracking_uri()).scheme

        with mlflow.start_run():
            mlflow.log_params(self.config.all_params)
            mlflow.log_metrics(
                {
                    'loss':self.score[0],
                    'accuracy':self.score[1]
                }
            )
            if tracking_url_type_score != 'file':
            # Log the single model.keras file
                mlflow.log_artifact("model.keras", artifact_path="model")
            else:
                mlflow.log_artifact("model.keras", artifact_path="model")