import os
import cv2
import numpy as np
import pandas as pd
from PIL import Image

# Function to load and process images
def load_images(img_path):
    data = []
    img = cv2.imread(img_path)
    if img is None:
        print("Error: Unable to load the image.")
    else:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
        img = cv2.resize(img, (64, 64))  # Resize images to a common size
        img = np.array(img) / 255.0  # Normalize pixel values
        img = img.reshape(1, 64, 64, 1)
        data.append([img])
    return data