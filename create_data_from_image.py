import os
import cv2
import numpy as np
import pandas as pd
from PIL import Image

PIXEL = 256
# Function to load and process images
def load_images(img_path):
    img = img_path
    img = cv2.resize(img, (PIXEL, PIXEL))  # Resize images to a common size
    img = np.array(img) / 255.0  # Normalize pixel values
    img = img.reshape(1, PIXEL, PIXEL, 1)
    return img