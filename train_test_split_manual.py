import tensorflow as tf
from keras.preprocessing.image import ImageDataGenerator
import keras
from keras.layers import Dense, Conv2D
import matplotlib.pyplot as plt
import numpy as np
import os
import re
from PIL import Image
import shutil

shutil.copy(src, dst)
images_path = 'C:\Project\signature_verification\data'
os.chdir(images_path)
with open(f'labels.txt', 'r') as f:
    # Read the contents of the file
    file_contents = f.read()

output_data_list = list(map(str, file_contents.split('\n')))

os.mkdir('C:\Project\signature_verification/train_test_data')
os.mkdir('C:\Project\signature_verification/train_test_data/train_data')
os.mkdir('C:\Project\signature_verification/train_test_data/test_data')

src = 'C:\Project\signature_verification/train_test_data'
dst_train = 'C:\Project\signature_verification/train_test_data/train_data'
dst_test = 'C:\Project\signature_verification/train_test_data/test_data'


import os
import shutil
import sys
from sklearn.model_selection import train_test_split

# Set the path to the data directory
data_dir = '/path/to/data/directory'

# Load the image file names and labels from the text file
with open(os.path.join(data_dir, 'labels.txt'), 'r') as f:
    data = f.read().splitlines()
    file_names, labels = zip(*[line.split() for line in data])

# Get the train-test portion from the command-line arguments
train_test_portion = float(sys.argv[1])

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(file_names, labels, test_size=train_test_portion, random_state=42)

# Create the train_data and test_data directories
os.makedirs(os.path.join(data_dir, 'train_data'), exist_ok=True)
os.makedirs(os.path.join(data_dir, 'test_data'), exist_ok=True)

# Copy the training images to the train_data directory
for file_name in X_train:
    src = os.path.join(data_dir, file_name)
    dst = os.path.join(data_dir, 'train_data', file_name)
    shutil.copy(src, dst)

# Copy the test images to the test_data directory
for file_name in X_test:
    src = os.path.join(data_dir, file_name)
    dst = os.path.join(data_dir, 'test_data', file_name)
    shutil.copy(src, dst)

# Save the training labels to the train.txt file
with open(os.path.join(data_dir, 'train.txt'), 'w') as f:
    for label in y_train:
        f.write(f'{label}\n')

# Save the test labels to the test.txt file
with open(os.path.join(data_dir, 'test.txt'), 'w') as f:
    for label in y_test:
        f.write(f'{label}\n')



