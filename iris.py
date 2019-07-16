import numpy as np
from matplotlib import pyplot as plt
import pandas as pd



def read_dataset():
    return pd.read_csv('iris.csv'), pd.read_csv('iris_metadata.csv')

def merge_dfs(iris, metadata):
    ### complete here

def split_df(df, ratio):
    ### complete here

def truncate_non_toxics(df):
    ### complete here

def main():
    split_ratio = 0.7
    iris, metadata = read_dataset()
    ### complete here


main()




