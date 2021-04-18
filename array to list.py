import numpy as np
def data_processing():
    x = np.array([[1, 2, 4], [3, 4], [1,2,3,4,5,6,7]])
    y = sum(x.tolist(),[])
    print(np.array(y))
data_processing()
