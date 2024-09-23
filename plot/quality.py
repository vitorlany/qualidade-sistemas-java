import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def quality_created_at(dataframe):
    created_at = dataframe["created_at"]
    cbo_media = dataframe['cbo_media']
    dit_media = dataframe['dit_media']
    lcom_media = dataframe['lcom_media']

    plt.figure(figsize=(15, 6))

    # cbo_media
    plt.scatter(created_at, cbo_media, label='CBO Média', color='blue', marker='o')

    plt.title('CBO Média X Maturidade')
    plt.xlabel('created_at')
    plt.ylabel('CBO Média')

    plt.tight_layout()

    plt.savefig('graphs/cbo_media_maturidade.png')
    plt.clf()

    # dit_media
    plt.scatter(created_at, dit_media, label='DIT Média', color='blue')
    plt.title('DIT Média X Maturidade')
    plt.xlabel('created_at')
    plt.ylabel('DIT Média')
    plt.tight_layout()
    plt.savefig('graphs/dit_media_maturidade.png')
    plt.clf()

    # lcom_media
    plt.scatter(created_at, lcom_media, label='LCOM Média', color='blue')
    plt.title('LCOM Média X Maturidade')
    plt.xlabel('created_at')
    plt.ylabel('LCOM Média')
    plt.tight_layout()
    plt.savefig('graphs/lcom_media_maturidade.png')
    plt.clf()

def quality_loc(dataframe):
    loc_soma = dataframe["loc_soma"]
    cbo_media = dataframe['cbo_media']
    dit_media = dataframe['dit_media']
    lcom_media = dataframe['lcom_media']

    plt.figure(figsize=(15, 6))

    # cbo_media
    plt.scatter(loc_soma, cbo_media, label='CBO Média', color='blue', marker='o')

    plt.title('CBO Média X tamanho')
    plt.xlabel('loc')
    plt.ylabel('CBO Média')

    plt.tight_layout()

    plt.savefig('graphs/cbo_media_tamanho.png')
    plt.clf()

    # dit_media
    plt.scatter(loc_soma, dit_media, label='DIT Média', color='blue')
    plt.title('DIT Média X tamanho')
    plt.xlabel('loc')
    plt.ylabel('DIT Média')
    plt.tight_layout()
    plt.savefig('graphs/dit_media_tamanho.png')
    plt.clf()

    # lcom_media
    plt.scatter(loc_soma, lcom_media, label='LCOM Média', color='blue')
    plt.title('LCOM Média X tamanho')
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

    plt.figure(figsize=(15, 6))

    # cbo_media
    plt.scatter(releases, cbo_media, label='CBO Média', color='blue', marker='o')

    plt.title('CBO Média X atividade')
    plt.xlabel('releases')
    plt.ylabel('CBO Média')

    plt.tight_layout()

    plt.savefig('graphs/cbo_media_releases.png')
    plt.clf()

    # dit_media
    plt.scatter(releases, dit_media, label='DIT Média', color='blue')
    plt.title('DIT Média X atividade')
    plt.xlabel('releases')
    plt.ylabel('DIT Média')
    plt.tight_layout()
    plt.savefig('graphs/dit_media_releases.png')
    plt.clf()

    # lcom_media
    plt.scatter(releases, lcom_media, label='LCOM Média', color='blue')
    plt.title('LCOM Média X atividade')
    plt.xlabel('releases')
    plt.ylabel('LCOM Média')
    plt.tight_layout()
    plt.savefig('graphs/lcom_media_releases.png')
    plt.clf()

def quality_stars(dataframe):
    stars = dataframe["stars"]
    cbo_media = dataframe['cbo_media']
    dit_media = dataframe['dit_media']
    lcom_media = dataframe['lcom_media']

    plt.figure(figsize=(15, 6))

    # cbo_media
    plt.scatter(stars, cbo_media, label='CBO Média', color='blue', marker='o')

    plt.title('CBO Média X popularidade')
    plt.xlabel('stars')
    plt.ylabel('CBO Média')

    plt.tight_layout()

    plt.savefig('graphs/cbo_media_stars.png')
    plt.clf()

    # dit_media
    plt.scatter(stars, dit_media, label='DIT Média', color='blue')
    plt.title('DIT Média X popularidade')
    plt.xlabel('stars')
    plt.ylabel('DIT Média')
    plt.tight_layout()
    plt.savefig('graphs/dit_media_stars.png')
    plt.clf()

    # lcom_media
    plt.scatter(stars, lcom_media, label='LCOM Média', color='blue')
    plt.title('LCOM Média X popularidade')
    plt.xlabel('stars')
    plt.ylabel('LCOM Média')
    plt.tight_layout()
    plt.savefig('graphs/lcom_media_stars.png')
    plt.clf()

def quality_loc_aggregate(dataframe):
    dataframe = dataframe.sort_values(by='loc_soma')

    cbo_media = dataframe['cbo_media']
    dit_media = dataframe['dit_media']
    lcom_media = dataframe['lcom_media']
    loc_soma = dataframe['loc_soma']

    plt.figure(figsize=(15, 6))

    fig, ax1 = plt.subplots(figsize=(15, 6))
    ax2 = ax1.twinx()
    ax3 = ax1.twinx()

    ax1.plot(loc_soma, cbo_media, label='CBO Média', color='blue')
    ax2.plot(loc_soma, dit_media, label='DIT Média', color='red')
    ax3.plot(loc_soma, lcom_media, label='LCOM Média', color='green')

    ax1.set_xlabel('loc')
    ax1.set_ylabel('CBO Média', color='blue')
    ax2.set_ylabel('DIT Média', color='red')
    ax3.set_ylabel('LCOM Média', color='green')

    ax1.tick_params(axis='y', labelcolor='blue')
    ax2.tick_params(axis='y', labelcolor='red')
    ax3.tick_params(axis='y', labelcolor='green')

    plt.title('CBO Média, DIT Média, LCOM Média X Tamanho')

    plt.tight_layout()
    plt.savefig('graphs/tamanho.png')
    plt.clf()

def quality_created_at_aggregate(dataframe):
    dataframe = dataframe.sort_values(by='created_at')

    cbo_media = dataframe['cbo_media']
    dit_media = dataframe['dit_media']
    lcom_media = dataframe['lcom_media']
    created_at = dataframe['created_at']

    plt.figure(figsize=(15, 6))

    fig, ax1 = plt.subplots(figsize=(15, 6))
    ax2 = ax1.twinx()
    ax3 = ax1.twinx()

    ax1.plot(created_at, cbo_media, label='CBO Média', color='blue')
    ax2.plot(created_at, dit_media, label='DIT Média', color='red')
    ax3.plot(created_at, lcom_media, label='LCOM Média', color='green')

    ax1.set_xlabel('created_at')
    ax1.set_ylabel('CBO Média', color='blue')
    ax2.set_ylabel('DIT Média', color='red')
    ax3.set_ylabel('LCOM Média', color='green')

    ax1.tick_params(axis='y', labelcolor='blue')
    ax2.tick_params(axis='y', labelcolor='red')
    ax3.tick_params(axis='y', labelcolor='green')

    plt.title('CBO Média, DIT Média, LCOM Média X Maturidade')

    plt.tight_layout()
    plt.savefig('graphs/maturidade.png')
    plt.clf()

def quality_stars_aggregate(dataframe):
    dataframe = dataframe.sort_values(by='stars')

    cbo_media = dataframe['cbo_media']
    dit_media = dataframe['dit_media']
    lcom_media = dataframe['lcom_media']
    stars = dataframe['stars']

    plt.figure(figsize=(15, 6))

    fig, ax1 = plt.subplots(figsize=(15, 6))
    ax2 = ax1.twinx()
    ax3 = ax1.twinx()

    ax1.plot(stars, cbo_media, label='CBO Média', color='blue')
    ax2.plot(stars, dit_media, label='DIT Média', color='red')
    ax3.plot(stars, lcom_media, label='LCOM Média', color='green')

    ax1.set_xlabel('stars')
    ax1.set_ylabel('CBO Média', color='blue')
    ax2.set_ylabel('DIT Média', color='red')
    ax3.set_ylabel('LCOM Média', color='green')

    ax1.tick_params(axis='y', labelcolor='blue')
    ax2.tick_params(axis='y', labelcolor='red')
    ax3.tick_params(axis='y', labelcolor='green')

    plt.title('CBO Média, DIT Média, LCOM Média X Popularidade')

    plt.tight_layout()
    plt.savefig('graphs/popularidade.png')
    plt.clf()

def quality_releases_aggregate(dataframe):
    dataframe = dataframe.sort_values(by='releases')

    cbo_media = dataframe['cbo_media']
    dit_media = dataframe['dit_media']
    lcom_media = dataframe['lcom_media']
    releases = dataframe['releases']

    plt.figure(figsize=(15, 6))

    fig, ax1 = plt.subplots(figsize=(15, 6))
    ax2 = ax1.twinx()
    ax3 = ax1.twinx()

    ax1.plot(releases, cbo_media, label='CBO Média', color='blue')
    ax2.plot(releases, dit_media, label='DIT Média', color='red')
    ax3.plot(releases, lcom_media, label='LCOM Média', color='green')

    ax1.set_xlabel('releases')
    ax1.set_ylabel('CBO Média', color='blue')
    ax2.set_ylabel('DIT Média', color='red')
    ax3.set_ylabel('LCOM Média', color='green')

    ax1.tick_params(axis='y', labelcolor='blue')
    ax2.tick_params(axis='y', labelcolor='red')
    ax3.tick_params(axis='y', labelcolor='green')

    plt.title('CBO Média, DIT Média, LCOM Média X Atividade')

    plt.tight_layout()
    plt.savefig('graphs/releases.png')
    plt.clf()