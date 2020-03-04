import numpy as np
import os
import pandas as pd
from tempfile import TemporaryFile

outfile = TemporaryFile()
imgs = np.load('./cnn_auto_train_100_comps.npy')

with open('/Users/camilledunning/Desktop/Code/iSchemaView/cluster_filenames_v1.txt', 'r') as text_file:
    data = text_file.readlines()

df = pd.DataFrame(imgs)
# 639, 783, 98, 420, 662, 137, 524, 632
df2 = pd.DataFrame([df.iloc[5],
					df.iloc[98],
					df.iloc[167],
					df.iloc[272],
					df.iloc[346], 
					df.iloc[258],
					df.iloc[185], 
					df.iloc[79],  
					df.iloc[155],
					df.iloc[69], 
					df.iloc[16], 
					df.iloc[524], 								
					df.iloc[886],
					df.iloc[823],
					df.iloc[792]])

x = df2.to_numpy()
np.save("test_clustering_data", x)