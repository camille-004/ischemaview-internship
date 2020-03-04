import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

'''single_image = "/Users/camilledunning/Desktop/Code/iSchemaView/mtt_files/106c_426_4764_mtt_1.jpg"
single_image2 = "/Users/camilledunning/Desktop/Code/iSchemaView/mtt_files/106c_427_4776_mtt_13.jpg"

image_array = plt.imread(single_image)
image_array2 = plt.imread(single_image2)'''

image1 = Image.open("/Users/camilledunning/Desktop/Code/iSchemaView/images/mtt_files/106c_426_4764_mtt_1.jpg")
image2 = Image.open("/Users/camilledunning/Desktop/Code/iSchemaView/images/mtt_files/106c_427_4776_mtt_13.jpg")

height, width, = image1.size
# height2, width2, channels2 = image_array2.shape
resized_img2 = image2.resize((height, width))
resized_array = np.array(image1.getdata()).reshape(image1.size[0], image1.size[1], 3)
resized_array2 = np.array(resized_img2.getdata()).reshape(resized_img2.size[0], resized_img2.size[1], 3)
print(resized_array.shape)
print(resized_array2.shape)

# resized_img2.show()
# image1.show()

print(type(image1))
# input("stop")
# image_array_resized = plt.imread(resized_img2)

r_matrix = []
g_matrix = []
b_matrix = []

r_matrix2 = []
g_matrix2 = []
b_matrix2 = []

for i in range(resized_array.shape[0]):
	for j in range(resized_array.shape[1]):
		r_matrix.append(resized_array[i][j][0])
		g_matrix.append(resized_array[i][j][1])
		b_matrix.append(resized_array[i][j][2])

for i in range(resized_array2.shape[0]):
	for j in range(resized_array2.shape[1]):
		r_matrix2.append(resized_array2[i][j][0])
		g_matrix2.append(resized_array2[i][j][1])
		b_matrix2.append(resized_array2[i][j][2])

stacked_matrix = np.zeros((2, len(r_matrix)))

for i in range(2):
	for j in range(len(r_matrix)):
		stacked_matrix[0][j] = r_matrix[j]
		stacked_matrix[1][j] = r_matrix2[j]

print(stacked_matrix)
'''

Initialize a list of all sizes of mtt images (get sizes initially by iterating through the mtt files list and appending the sizes)
Find minimum value in the list to get the smallest mtt image **by area of image in pixels (use height * width)
Initialize stacked_matrix1, ...2, ...3 to np.zeros((however many mtt images there are), size of the smallest mtt image)
Loop over all mtt images -->
	load image
	Resize that image to the smallest image
	change to np.array
	extract each channel into separate arrays, shortcut: image[:, :, 0]

	red_vector = image[:, :, 0].reshape((1, size of image)) ...

	reshape each 2d (of rows and columns) array into one row vector --> (1 x the area/size of the image)
	add those vectors to their respective stack matrices
 
'''