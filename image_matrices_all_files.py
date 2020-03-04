import os
import numpy as np 
from PIL import Image

mtt_files_path = "/Users/camilledunning/Desktop/Code/iSchemaView/mtt_files"
mtt_files_amount = len([mtt for mtt in os.listdir(mtt_files_path) if os.path.isfile(os.path.join(mtt_files_path, mtt))])

img_sizes = []

smallest_image = ""
smallest_size = 10000000

for mtt in os.listdir(mtt_files_path):
    img = Image.open(os.path.join(mtt_files_path, mtt))
    width, height = img.size
    current_image_size = width * height
    if current_image_size < smallest_size:
        smallest_size = current_image_size
        smallest_image = mtt

smallest_image_path = "/Users/camilledunning/Desktop/Code/iSchemaView/mtt_files/" + smallest_image
smallest_image = Image.open(smallest_image_path)
smallest_image_height, smallest_image_width = smallest_image.size
smallest_image_size = smallest_image_height * smallest_image_width

rstacked_matrix = np.zeros((mtt_files_amount, smallest_image_size))
gstacked_matrix = np.zeros((mtt_files_amount, smallest_image_size))
bstacked_matrix = np.zeros((mtt_files_amount, smallest_image_size))

counter = 0

for counter, mtt in enumerate(os.listdir(mtt_files_path)):
    img = Image.open(os.path.join(mtt_files_path, mtt))
    resized_img = img.resize((smallest_image_height, smallest_image_width))
    new_img_array = np.array(resized_img.getdata()).reshape(smallest_image_height, smallest_image_width, 3)
    rstacked_matrix[counter, :] = new_img_array[:, :, 0].reshape((1, smallest_image_size)) / 255
    gstacked_matrix[counter, :] = new_img_array[:, :, 1].reshape((1, smallest_image_size)) / 255
    bstacked_matrix[counter, :] = new_img_array[:, :, 2].reshape((1, smallest_image_size)) / 255