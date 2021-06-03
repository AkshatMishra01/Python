import numpy as np
import numbers
print("lets do neural networking" )
input_matrix = np.array([2,4,1,7,8])
weights_of_matrices = np.array([4,3,5,6,9])
x = np.array([1,1,1])
for val in input_matrix:
    x = val * weights_of_matrices
output_dot_product = input_matrix * weights_of_matrices
print(output_dot_product)
print(x)    







