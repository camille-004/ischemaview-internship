import scipy.ndimage
import matplotlib.pyplot as plt

single_image = "/Users/camilledunning/Desktop/Code/iSchemaView/images/mtt_files/1923013_6333_mtt_8.jpg"

image_array = plt.imread(single_image)

height, width, channels = image_array.shape

image_array2 = image_array.reshape(height, width, channels)

single_image2 = plt.imshow(image_array2)
plt.show()

print(image_array.shape)
print(image_array2.shape)