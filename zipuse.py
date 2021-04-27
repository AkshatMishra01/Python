import numpy as np 

arr1= np.array([1,2,3,4,5,6,7])
arr2 = np.array([8,9,10,11,12,13,14])

for num1, num2 in zip(arr1,arr2):
    print(arr1 * arr2)
