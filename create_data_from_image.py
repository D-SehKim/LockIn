import os
import cv2
import numpy as np
import pandas as pd
from PIL import Image

# Function to load and process images
def load_images(folder, label):
    data = []
    for filename in os.listdir(folder):
        img_path = os.path.join(folder, filename)
        img = cv2.imread(img_path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
        img = cv2.resize(img, (64, 64))  # Resize images to a common size
        img = np.array(img) / 255.0  # Normalize pixel values
        data.append([img, label])
    return data

# Define paths
closed_folder = '/kaggle/input/mrl-dataset/train/Closed_Eyes'
open_folder = '/kaggle/input/mrl-dataset/train/Open_Eyes'

# Load and process images
closed_data = load_images(closed_folder, 0)  # 0 represents closed eyes
open_data = load_images(open_folder, 1)  # 1 represents open eyes

# Combine data
all_data = closed_data + open_data
np.random.shuffle(all_data)

# Separate features and labels
X = np.array([item[0] for item in all_data])
y = np.array([item[1] for item in all_data])

# Flatten the features
X = X.reshape(X.shape[0], -1)

# Create a DataFrame
df = pd.DataFrame(X, columns=[f'pixel_{i}' for i in range(X.shape[1])])
df['label'] = y

# Save the DataFrame to a CSV file
df.to_csv('eye_data.csv', index=False)
