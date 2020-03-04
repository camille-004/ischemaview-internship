import numpy as np
import os
import pandas as pd

imgs = np.load('./cnn_auto_train_100_comps.npy')

with open("/Users/camilledunning/Desktop/Code/iSchemaView/cluster_filenames_v1.txt", 'r') as text_file:
    data = text_file.readlines()

df = pd.DataFrame(imgs)

print(data)