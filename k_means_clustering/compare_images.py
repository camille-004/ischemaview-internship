import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image   
import numpy as np
import glob
import os

aqua_images = "/Users/camilledunning/Desktop/Code/iSchemaView/test_clustered_images/test_dataset_clustering/aqua_cluster"
aqua_image = glob.glob(aqua_images + '/*') 
aqua_img_array = np.array([np.array(Image.open(img).convert('RGB')) for img in aqua_image])

green_images = "/Users/camilledunning/Desktop/Code/iSchemaView/test_clustered_images/test_dataset_clustering/green_cluster"
green_image = glob.glob(green_images + '/*') 
green_img_array = np.array([np.array(Image.open(img).convert('RGB')) for img in green_image])

red_images = "/Users/camilledunning/Desktop/Code/iSchemaView/test_clustered_images/test_dataset_clustering/red_cluster"
red_image = glob.glob(red_images + '/*') 
red_img_array = np.array([np.array(Image.open(img).convert('RGB')) for img in red_image])

purple_images = "/Users/camilledunning/Desktop/Code/iSchemaView/test_clustered_images/test_dataset_clustering/purple_cluster"
purple_image = glob.glob(purple_images + '/*') 
purple_img_array = np.array([np.array(Image.open(img).convert('RGB')) for img in purple_image])

fig = plt.figure() 
for i in range(2):
	ax1 = plt.subplot(1, 2, i + 1)
	plt.xticks([])
	plt.yticks([])
	ax1.imshow(aqua_img_array[i])

ax2 = plt.subplot(1, 2, 2)
plt.xticks([])
plt.yticks([])
ax2.imshow(green_img_array[0])

plt.show()