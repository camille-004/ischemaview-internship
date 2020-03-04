import os
import numpy as np 
from PIL import Image

mtt_files_path = "/Users/camilledunning/Desktop/Code/iSchemaView/mtt_files_more_slices/"
tmax_files_path = "/Users/camilledunning/Desktop/Code/iSchemaView/tmax_files_more_slices/"

rmatrix_file = ""
gmatrix_file = ""
bmatrix_file = ""

def create_stacked_matrix(file_path, rmatrix_file, gmatrix_file, bmatrix_file):
    file_amount = len([i for i in os.listdir(file_path) if os.path.isfile(os.path.join(file_path, i))])

    img_sizes = []

    smallest_image = ""
    smallest_size = 10000000

    for file in os.listdir(file_path):
        img = Image.open(os.path.join(file_path, file))
        width, height = img.size
        current_image_size = width * height
        if current_image_size < smallest_size:
            smallest_size = current_image_size
            smallest_image = file

    smallest_image_path = file_path + smallest_image
    smallest_image = Image.open(smallest_image_path)
    smallest_image_height, smallest_image_width = smallest_image.size
    smallest_image_size = smallest_image_height * smallest_image_width

    rstacked_matrix = np.zeros((file_amount, smallest_image_size))
    gstacked_matrix = np.zeros((file_amount, smallest_image_size))
    bstacked_matrix = np.zeros((file_amount, smallest_image_size))

    counter = 0

    for counter, file in enumerate(os.listdir(file_path)):
        img = Image.open(os.path.join(file_path, file))
        resized_img = img.resize((smallest_image_height, smallest_image_width))
        new_img_array = np.array(resized_img.getdata()).reshape(smallest_image_height, smallest_image_width, 3)
        rstacked_matrix[counter, :] = new_img_array[:, :, 0].reshape((1, smallest_image_size)) / 255
        gstacked_matrix[counter, :] = new_img_array[:, :, 1].reshape((1, smallest_image_size)) / 255
        bstacked_matrix[counter, :] = new_img_array[:, :, 2].reshape((1, smallest_image_size)) / 255

    np.savetxt(rmatrix_file, rstacked_matrix)
    np.savetxt(gmatrix_file, gstacked_matrix)
    np.savetxt(bmatrix_file, bstacked_matrix)

create_stacked_matrix(tmax_files_path, "red_matrix_mtt_more_slices.txt", "green_matrix_mtt_more_slices.txt", "blue_matrix_mtt_more_slices.txt")