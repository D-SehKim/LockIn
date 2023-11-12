import os
import cv2
import numpy as np
import pandas as pd
from PIL import Image

# Function to load and process images
def load_images(img_path):
    data = []
    img = img_path
    if img is None:
        print("Error: Unable to load the image.")
    else:
        # img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
        img = cv2.resize(img, (96, 96))  # Resize images to a common size
        img = np.array(img) / 255.0  # Normalize pixel values
        img = img.reshape(1, 96, 96, 1)
        data.append([img])
    return data