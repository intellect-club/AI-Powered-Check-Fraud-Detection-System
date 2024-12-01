import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from .mock_db import *

img_height = 224
img_width = 224
threshold = 0.7
model_path = "models\\signature_matching.h5"

def preprocess_grayscale_to_rgb(image):

    if len(image.shape) == 2 or image.shape[-1] == 1:
        image = np.stack((image.squeeze(),) * 3, axis=-1)
    return image

def predict_signature(image_path, model, target_class, class_names, threshold=0.7):

    if target_class not in class_names:
        raise ValueError(f"Target class '{target_class}' not found in class names: {class_names}")

    target_class_index = class_names.index(target_class)

    image = load_img(image_path, target_size=(img_height, img_width), color_mode='grayscale')
    image = img_to_array(image)
    image = preprocess_grayscale_to_rgb(image) 
    image = image / 255.0
    image = np.expand_dims(image, axis=0) 

    predictions = model.predict(image)[0] 

    confidence = predictions[target_class_index]
    is_match = confidence >= threshold

    return {
        "Image Path": image_path,
        "Match": is_match,
        "Confidence": confidence,
        "Target Class": target_class
    }

def match_signature(image_path, target_class):
    print("Loading model...")
    model = load_model(model_path)

    print("Model loaded successfully.")

    print(f"Processing image at '{image_path}'...")
    result = predict_signature(image_path, model, target_class, class_names, threshold)

    return result