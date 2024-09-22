from quality import *
from summary import *
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

if __name__ == "__main__":
    dataframe = pd.read_csv("final_results.csv")
    dataframe = dataframe.sort_values(by='age')

    quality_created_at(dataframe)
    quality_releases(dataframe)
    quality_stars(dataframe)
    quality_loc(dataframe)
    summary(dataframe)

