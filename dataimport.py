import numpy as np
import pandas as pd

class ExtractData:
    def __init__(self,path):
        try:
            data = pd.read_csv(source,header=0)
            np.array(data) 
            input_data = pd.Series(data)
            print((input_data))
        except Exception:
            print("An Exception occurred")

i = input("Enter the source path:")
obj = ExtractData(i)
