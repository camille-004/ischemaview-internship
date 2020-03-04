from sklearn.cluster import KMeans  
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

imgs = np.load('test_clustering_data.npy')
df = pd.DataFrame(imgs)
print(df)

with open('/Users/camilledunning/Desktop/Code/iSchemaView/cluster_test_filesnames.txt', 'r') as text_file:
    data = text_file.readlines()

k = 4

kmeans = KMeans(n_clusters=k, random_state=0).fit(imgs)

plt.scatter(imgs[:,1], imgs[:,2], c=kmeans.labels_, cmap='rainbow', alpha = 0.8)
plt.scatter(kmeans.cluster_centers_[:,0] ,kmeans.cluster_centers_[:,1], color='black', alpha = 0.5)

plt.show()