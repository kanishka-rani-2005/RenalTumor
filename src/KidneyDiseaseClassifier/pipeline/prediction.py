import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os 



class PredictionPipeline:
    def __init__(self,filename):
        self.filename=filename

    def predict(self):
        # Load the model
        model = load_model(os.path.join('model', 'model.keras'))

        # Load and preprocess the image
        img_path = self.filename
        img = image.load_img(img_path, target_size=(224, 224))
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        result = np.argmax(model.predict(img_array))

        print(result)

        # Map the result to class names
        class_names = ['Cyst', 'Normal', 'Stone', 'Tumor']
        if result < len(class_names):
            predicted_class = class_names[result]
        else:
            predicted_class = "Unknown"
        print(f"Predicted class: {predicted_class}")
        return [{ "image" : predicted_class}]