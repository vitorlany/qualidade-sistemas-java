from quality import *
from summary import *
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

if __name__ == "__main__":
    dataframe = pd.read_csv("final_results.csv")
    dataframe = dataframe.sort_values(by='loc_soma')

    dataframe = dataframe[dataframe['cbo_media'] != 0]

    summary(dataframe)

    quality_created_at(dataframe)
    quality_releases(dataframe)
    quality_stars(dataframe)
    quality_loc(dataframe)

    quality_created_at_aggregate(dataframe)
    quality_releases_aggregate(dataframe)
    quality_stars_aggregate(dataframe)
    quality_loc_aggregate(dataframe)
