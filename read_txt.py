import numpy as np

matrix_path = "/Users/camilledunning/Desktop/Code/iSchemaView/red_matrix_tmax.txt"

data = np.loadtxt(matrix_path)

print(data.shape)