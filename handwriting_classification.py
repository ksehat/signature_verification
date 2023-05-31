import tensorflow as tf
from keras.preprocessing.image import ImageDataGenerator
import keras
from keras.layers import Dense, Conv2D
import matplotlib.pyplot as plt
import numpy as np
import os
import re
from PIL import Image

images_path = 'C:\Project\signature_verification\data'
os.chdir(images_path)
with open(f'labels.txt', 'r') as f:
    # Read the contents of the file
    file_contents = f.read()

# Convert the file contents to a list
output_data_list = list(map(str, file_contents.split('\n')))

datagen = ImageDataGenerator(
    rotation_range=40,
    width_shift_range=0.2,
    height_shift_range=0.2,
    brightness_range=None,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    vertical_flip=True,
)

data_generator = datagen.flow_from_directory(
    '/path/to/data/directory',
    target_size=(256, 256),
    batch_size=32,
    shuffle=True,
    seed=10,
)
