import os
import math
import numpy as np 
from PIL import Image

mtt_files_path = "/Users/camilledunning/Desktop/Code/iSchemaView/mtt_files"
mtt_files_amount = len([mtt for mtt in os.listdir(mtt_files_path) if os.path.isfile(os.path.join(mtt_files_path, mtt))])

widths = []
heights = []

for mtt in os.listdir(mtt_files_path):
    img = Image.open(os.path.join(mtt_files_path, mtt))
    width, height = img.size
    widths.append(width)
    heights.append(height)

average_img_width = int(math.floor(sum(widths) / len(widths)))
average_img_height = int(math.floor(sum(heights) / len(heights)))
average_img_size = average_img_width * average_img_height

red_vectors = []
green_vectors = []
blue_vectors = []

rstacked_matrix = np.zeros((mtt_files_amount, average_img_size))
gstacked_matrix = np.zeros((mtt_files_amount, average_img_size))
bstacked_matrix = np.zeros((mtt_files_amount, average_img_size))

for mtt in os.listdir(mtt_files_path):
    img = Image.open(os.path.join(mtt_files_path, mtt))
    resized_img = img.resize((average_img_height, average_img_width))
    new_img_array = np.array(resized_img.getdata()).reshape(average_img_height, average_img_width, 3)
    red_vector = new_img_array[:, :, 0].reshape((1, average_img_size))
    green_vector = new_img_array[:, :, 1].reshape((1, average_img_size))
    blue_vector = new_img_array[:, :, 2].reshape((1, average_img_size))
    red_vectors.append(red_vector)
    green_vectors.append(green_vector)
    blue_vectors.append(blue_vector)

for i in range(mtt_files_amount):
    rstacked_matrix[i] = red_vectors[i] / 255 
    gstacked_matrix[i] = green_vectors[i] / 255
    bstacked_matrix[i] = blue_vectors[i] / 255

print(rstacked_matrix)