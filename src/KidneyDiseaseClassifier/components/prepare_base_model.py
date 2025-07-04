import os 
from zipfile import ZipFile
import tensorflow as tf
import urllib.request as request
from src.KidneyDiseaseClassifier import logger
from src.KidneyDiseaseClassifier.entity.config_entity import PrepareBaseModelConfig
from pathlib import Path
from src.KidneyDiseaseClassifier.config.configuration import ConfigurationManager

class PrepareBaseModel:
    def __init__(self, config: "PrepareBaseModelConfig"): # Use the specific config class if you have one
        self.config = config
        self.model = None
        self.full_model = None

    def get_base_model(self):
        # logger.info("Downloading base VGG16 model...")
        print("Downloading base VGG16 model...")
        self.model = tf.keras.applications.vgg16.VGG16(
            input_shape=self.config.params_image_size,
            weights=self.config.params_weights,
            include_top=self.config.params_include_top
        )
        self.save_model(path=self.config.base_model_path, model=self.model)

# In your PrepareBaseModel class

    @staticmethod
    def prepare_full_model(model, classes, freeze_all, freeze_till, learning_rate):
        print("Preparing full model...")
        if freeze_all:
            print("Freezing all layers in the base model.")
            for layer in model.layers:
                layer.trainable = False
        elif (freeze_till is not None) and (freeze_till > 0):
            print(f"Freezing layers up to the last {freeze_till}.")
            for layer in model.layers[:-freeze_till]:
                layer.trainable = False

        flatten_in = tf.keras.layers.Flatten()(model.output)
        prediction = tf.keras.layers.Dense(
            units=classes,
            activation='softmax'
        )(flatten_in)

        full_model = tf.keras.models.Model(
            inputs=model.input,
            outputs=prediction
        )
        
        print("Compiling model...")
        full_model.compile(
            optimizer=tf.keras.optimizers.Adam(learning_rate=learning_rate),
            loss='categorical_crossentropy',
            metrics=['accuracy'] 
        )
        
        print("Model summary:")
        full_model.summary()
        return full_model
    def update_base_model(self):
        logger.info("Updating the base model...")
        print("Updating the base model...")
        self.full_model = self.prepare_full_model(
            model=self.model,
            classes=self.config.params_classes,
            freeze_all=True,
            freeze_till=None,
            learning_rate=self.config.params_learning_rate
        )
        self.save_model(path=self.config.updated_base_model_path, model=self.full_model)
        print(f"Updated model saved to: {self.config.updated_base_model_path}")

    @staticmethod
    def save_model(path: Path, model: tf.keras.Model):
        model.save(path)