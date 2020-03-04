import matplotlib.pyplot as plt
import matplotlib.lines as mlines  
import numpy as np
import pandas as pd
import copy
import os

imgs = np.load('test_clustering_data.npy')

with open("/Users/camilledunning/Desktop/Code/iSchemaView/cluster_filenames_v1.txt", 'r') as text_file:
    data = text_file.readlines()

df = pd.DataFrame(imgs)

k = 4

colmap = {1: "r", 2: "g", 3: "b", 4: "c"}

np.random.seed(0)

# INITIALIZE CENTROIDS

centroids = {
    i+1: [np.random.randint(0, 25), np.random.randint(0, 25)]
    for i in range(k)
}

# ASSIGN DATAPOINTS TO CENTROIDS

def assign(df, centroids):
    for i in centroids.keys():
        # EUCLIDEAN DISTANCE
        df['distance_from_{}'.format(i)] = (
            np.sqrt(
                (df[0] - centroids[i][0]) ** 2
                + (df[1] - centroids[i][1]) ** 2
            )
        )
    centroid_distance_cols = ['distance_from_{}'.format(i) for i in centroids.keys()]
    df['closest'] = df.loc[:, centroid_distance_cols].idxmin(axis=1)
    df['closest'] = df['closest'].map(lambda x: int(x.lstrip('distance_from_')))
    df['color'] = df['closest'].map(lambda x: colmap[x])
    return df

df = assign(df, centroids)

# UPDATE CENTROIDS

old_centroids = copy.deepcopy(centroids)

def update(k):
    for i in centroids.keys():
        centroids[i][0] = np.mean(df[df['closest'] == i][0])
        centroids[i][1] = np.mean(df[df['closest'] == i][1])
    return k

centroids = update(centroids)

# REPEAT ASSIGNMENT

while True:
    closest_centroids = df['closest'].copy(deep=True)
    centroids = update(centroids)
    df = assign(df, centroids)
    if closest_centroids.equals(df['closest']):
        break

pd.set_option('display.max_rows', 500)
print(df)

# Plot results
fig = plt.figure(figsize=(5, 5))
plt.scatter(df[0], df[1], color=df['color'], alpha=0.5, edgecolor='k')

# Graph centroids and create legends
for i in centroids.keys():
    plt.scatter(*centroids[i], color=colmap[i])

plt.xlim(-32, 35)
plt.ylim(-20, 30)

plt.show()