import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def summary(dataframe):
    cbo_media = dataframe['cbo_media']
    dit_media = dataframe['dit_media']
    lcom_media = dataframe['lcom_media']
    loc_soma = dataframe['loc_soma']

    plt.figure(figsize=(10, 6))

    # cbo_media
    plt.boxplot(cbo_media)

    plt.title('CBO Média')

    plt.tight_layout()

    plt.savefig('graphs/cbo_media.png')
    plt.clf()

    # dit_media
    plt.boxplot(dit_media)

    plt.title('DIT Média')

    plt.tight_layout()

    plt.savefig('graphs/dit_media.png')
    plt.clf()

    # lcom_media
    plt.boxplot(lcom_media)

    plt.title('LCOM Média')

    plt.tight_layout()

    plt.savefig('graphs/lcom_media.png')
    plt.clf()

    # loc_soma
    plt.boxplot(loc_soma)

    plt.title('LOC')

    plt.tight_layout()

    plt.savefig('graphs/loc_soma.png')
    plt.clf()