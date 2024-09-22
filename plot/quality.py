import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def quality_created_at(dataframe):
    created_at = dataframe["created_at"]
    cbo_media = dataframe['cbo_media']
    dit_media = dataframe['dit_media']
    lcom_media = dataframe['lcom_media']
    loc_soma = dataframe['loc_soma']

    plt.figure(figsize=(10, 6))

    # cbo_media
    plt.scatter(created_at, cbo_media, label='CBO Média', color='blue', marker='o', s=30)

    plt.title('CBO Média X maturidade')
    plt.xlabel('created_at')
    plt.ylabel('CBO Média')

    plt.tight_layout()

    plt.savefig('graphs/cbo_media_maturidade.png')
    plt.clf()

    # dit_media
    plt.scatter(created_at, dit_media, label='DIT Média', color='blue', marker='o', s=30)
    plt.title('DIT Média X maturidade')
    plt.xlabel('created_at')
    plt.ylabel('DIT Média')
    plt.tight_layout()
    plt.savefig('graphs/dit_media_maturidade.png')
    plt.clf()

    # lcom_media
    plt.scatter(created_at, lcom_media, label='LCOM Média', color='blue', marker='o', s=30)
    plt.title('LCOM Média X maturidade')
    plt.xlabel('created_at')
    plt.ylabel('LCOM Média')
    plt.tight_layout()
    plt.savefig('graphs/lcom_media_maturidade.png')
    plt.clf()

def quality_loc(dataframe):
    cbo_media = dataframe['cbo_media']
    dit_media = dataframe['dit_media']
    lcom_media = dataframe['lcom_media']
    loc_soma = dataframe['loc_soma']

    plt.figure(figsize=(10, 6))

    # cbo_media
    plt.scatter(loc_soma, cbo_media, label='CBO Média', color='blue', marker='o', s=30)

    plt.title('CBO Média X Tamanho')
    plt.xlabel('loc')
    plt.ylabel('CBO Média')

    plt.tight_layout()

    plt.savefig('graphs/cbo_media_tamanho.png')
    plt.clf()

    # dit_media
    plt.scatter(loc_soma, dit_media, label='DIT Média', color='blue', marker='o', s=30)
    plt.title('DIT Média X maturidade')
    plt.xlabel('loc')
    plt.ylabel('DIT Média')
    plt.tight_layout()
    plt.savefig('graphs/dit_media_tamanho.png')
    plt.clf()

    # lcom_media
    plt.scatter(loc_soma, lcom_media, label='LCOM Média', color='blue', marker='o', s=30)
    plt.title('LCOM Média X maturidade')
    plt.xlabel('loc')
    plt.ylabel('LCOM Média')
    plt.tight_layout()
    plt.savefig('graphs/lcom_media_tamanho.png')
    plt.clf()

def quality_releases(dataframe):
    cbo_media = dataframe['cbo_media']
    dit_media = dataframe['dit_media']
    lcom_media = dataframe['lcom_media']
    releases = dataframe['releases']

    plt.figure(figsize=(10, 6))

    # cbo_media
    plt.scatter(releases, cbo_media, label='CBO Média', color='blue', marker='o', s=30)

    plt.title('CBO Média X maturidade')
    plt.xlabel('releases')
    plt.ylabel('CBO Média')

    plt.tight_layout()

    plt.savefig('graphs/cbo_media_releases.png')
    plt.clf()

    # dit_media
    plt.scatter(releases, dit_media, label='DIT Média', color='blue', marker='o', s=30)
    plt.title('DIT Média X maturidade')
    plt.xlabel('releases')
    plt.ylabel('DIT Média')
    plt.tight_layout()
    plt.savefig('graphs/dit_media_releases.png')
    plt.clf()

    # lcom_media
    plt.scatter(releases, lcom_media, label='LCOM Média', color='blue', marker='o', s=30)
    plt.title('LCOM Média X maturidade')
    plt.xlabel('created_at')
    plt.ylabel('LCOM Média')
    plt.tight_layout()
    plt.savefig('graphs/lcom_media_releases.png')
    plt.clf()

def quality_stars(dataframe):
    stars = dataframe["stars"]
    cbo_media = dataframe['cbo_media']
    dit_media = dataframe['dit_media']
    lcom_media = dataframe['lcom_media']

    plt.figure(figsize=(10, 6))

    # cbo_media
    plt.scatter(stars, cbo_media, label='CBO Média', color='blue', marker='o', s=30)

    plt.title('CBO Média X maturidade')
    plt.xlabel('stars')
    plt.ylabel('CBO Média')

    plt.tight_layout()

    plt.savefig('graphs/cbo_media_stars.png')
    plt.clf()

    # dit_media
    plt.scatter(stars, dit_media, label='DIT Média', color='blue', marker='o', s=30)
    plt.title('DIT Média X maturidade')
    plt.xlabel('stars')
    plt.ylabel('DIT Média')
    plt.tight_layout()
    plt.savefig('graphs/dit_media_stars.png')
    plt.clf()

    # lcom_media
    plt.scatter(stars, lcom_media, label='LCOM Média', color='blue', marker='o', s=30)
    plt.title('LCOM Média X maturidade')
    plt.xlabel('stars')
    plt.ylabel('LCOM Média')
    plt.tight_layout()
    plt.savefig('graphs/lcom_media_stars.png')
    plt.clf()
    