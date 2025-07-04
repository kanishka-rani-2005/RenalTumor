from src.KidneyDiseaseClassifier import logger
from src.KidneyDiseaseClassifier.entity.config_entity import TrainingConfig
import tensorflow as tf
from pathlib import Path

tf.config.run_functions_eagerly(True)

class Training:
    def __init__(self, config: "TrainingConfig"):
        self.config = config
        self.model = tf.keras.models.load_model(self.config.updated_base_model_path)
        self.train_generator = None
        self.valid_generator = None

    def get_base_model(self):
        """Loads the updated base model from the specified path."""
        print("Loading the updated and compiled base model for training...")
        self.model = tf.keras.models.load_model(
            self.config.updated_base_model_path
        )

    def train_valid_generator(self):
        """Creates training and validation data generators."""
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

        if self.config.params_is_augmentation:
            train_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
                rotation_range=20,
                shear_range=0.1,
                zoom_range=0.2,
                horizontal_flip=True,
                **datagenerator_kwargs
            )
        else:
            train_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(**datagenerator_kwargs)

        self.train_generator = train_datagenerator.flow_from_directory(
            directory=self.config.training_data,
            subset="training",
            shuffle=True,
            **dataflow_kwargs
        )

    @staticmethod
    def _save_model(path: Path, model: tf.keras.Model):
        model.save(path)
        print(f"Final trained model saved to: {path}")

    def train(self):
        """Executes the final model training loop."""
        steps_per_epoch = self.train_generator.samples // self.train_generator.batch_size
        validation_steps = self.valid_generator.samples // self.valid_generator.batch_size

        print("--- Starting Final Model Training ---")
        self.model.compile(
            optimizer=tf.keras.optimizers.Adam(learning_rate=self.config.params_learning_rate),
            loss='categorical_crossentropy',
            metrics=['accuracy']
        )
        self.model.fit(
            self.train_generator,
            epochs=self.config.params_epochs,
            steps_per_epoch=steps_per_epoch,
            validation_data=self.valid_generator,
            validation_steps=validation_steps
        )

        self._save_model(
            path=self.config.trained_model_path,
            model=self.model
        )