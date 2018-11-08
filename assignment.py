import pandas as pd 
import matplotlib as plt
import numpy as np
from repair import remove_dollar_sign

def num_missing_values(df):
    print(df.apply(lambda x: sum(x.isnull()), axis=0))

if __name__ == "__main__":
    #remove_dollar_sign("./Dataset/googleplaystore.csv", "./Dataset/cleanedDataset.csv")
    
    df = pd.read_csv("./Dataset/cleanedDataset.csv")
    print(df.head(10))upy