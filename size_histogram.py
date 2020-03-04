import os
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

mtt_files_path = "/Users/camilledunning/Desktop/Code/iSchemaView/mtt_files/"
img_sizes = []

for mtt in os.listdir(mtt_files_path):
    img = Image.open(os.path.join(mtt_files_path, mtt))
    width, height = img.size
    img_sizes.append(width * height)

plt.hist(img_sizes, bins=50)
plt.axis([0, 30000, 0, 45])
plt.xlabel('Image Sizes')
plt.ylabel('Number of Images')
plt.show()