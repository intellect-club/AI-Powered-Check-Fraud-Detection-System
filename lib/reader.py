import os
import cv2
import numpy as np
from ultralytics import YOLO

signature_model = YOLO("models/signature_detection.pt")
text_model = YOLO("models/text_extraction.pt")

os.makedirs("results\\signatures", exist_ok=True)
os.makedirs("results\\texts", exist_ok=True)

def detect_and_crop(image_path, model, output_dir, label):
    image = cv2.imread(image_path)
    if image is None:
        print(f"Error loading {image_path}")
        return
    
    results = model(image)

    lowest_box = None
    lowest_y_min = -float('inf')

    for idx, box in enumerate(results[0].boxes.xyxy.cpu().numpy()):
        x_min, y_min, x_max, y_max = map(int, box)

        if y_min > lowest_y_min:
            lowest_y_min = y_min
            lowest_box = (x_min, y_min, x_max, y_max)

    if lowest_box:
        x_min, y_min, x_max, y_max = lowest_box
        cropped = image[y_min:y_max, x_min:x_max]

        filename = os.path.join(output_dir, f"{label}_lowest.png")
        cv2.imwrite(filename, cropped)
        print(f"Saved: {filename}")

        return filename
    else:
        print("No boxes detected.")
        return None

def process_image(image_path):
    print(f"Processing: {image_path}")
    
    signature = detect_and_crop(image_path, signature_model, "results\\signatures", "signature")
    
    text = detect_and_crop(image_path, text_model, "results\\texts", "text")

    return({"text":text, 'signature':signature})