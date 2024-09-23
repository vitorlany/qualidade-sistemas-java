import csv
import numpy as np
import os

file_path = './ck_results/'
class_csv_file = '/class.csv'
repo_info_path = './repo_info.csv'
results_path = './final_results.csv'

cbo_index = 3
dit_index = 8
lcom_index = 11
loc_index = 34

def calc_metrics(array):
    mediana = np.median(array)
    media = np.mean(array)
    desvio_padrao = np.std(array)
    return mediana, media, desvio_padrao

def get_data_by_column_index(index, array):
    temp = []
    for line in array:
        temp.append(float(line[index]))
    return temp

# Extrai os dados brutos do arquivo class.csv
def extract_data(file_path):
    if (os.path.isfile(file_path) == False):
        return []
    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        csv_file_reader = csv.reader(file)

        data = []
        for line in csv_file_reader:
            data.append(line)
        if (len(data) > 0):
            data.pop(0)
        return data

def generate_metrics(index, data):
    if (len(data) == 0):
        return 0, 0, 0
    values = get_data_by_column_index(index, data)
    mediana, media, desvio_padrao = calc_metrics(values)
    return mediana, media, desvio_padrao

def get_repos_info():
    data = []
    with open(repo_info_path, mode='r', newline='', encoding='utf-8') as file:
        csv_file_reader = csv.reader(file)

        for line in csv_file_reader:
            data.append(line)
        data.pop(0)

    return data

# Adiciona as métricas calculadas ao arquivo CSV
def add_data_to_csv(new_data):
    header = ["repo_name", "created_at", "age", "releases", "stars", "cbo_mediana", "cbo_media", "cbo_desvio_padrao", "dit_mediana", "dit_media", "dit_desvio_padrao", "lcom_mediana", "lcom_media", "lcom_desvio_padrao", "loc_soma"]
    data = get_repos_info()

    for i in range(len(data)):
        data[i].append(new_data[i][0])
        data[i].append(new_data[i][1])
        data[i].append(new_data[i][2])
        data[i].append(new_data[i][3])
        data[i].append(new_data[i][4])
        data[i].append(new_data[i][5])
        data[i].append(new_data[i][6])
        data[i].append(new_data[i][7])
        data[i].append(new_data[i][8])
        data[i].append(new_data[i][9])

    with open(results_path, mode='w', newline='', encoding='utf-8') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(header)
        csv_writer.writerows(data)

# Iterar sobre os repositórios coletados e calcular as métricas
def it_repos():
    data = get_repos_info()
    new_data = []
    for line in data:
        repo_name = line[0]
        path = file_path + repo_name + class_csv_file
        data = extract_data(path)

        cbo_mediana, cbo_media, cbo_desvio_padrao = generate_metrics(cbo_index, data)
        dit_mediana, dit_media, dit_desvio_padrao = generate_metrics(dit_index, data)
        lcom_mediana, lcom_media, lcom_desvio_padrao = generate_metrics(lcom_index, data)
        loc_soma = sum(get_data_by_column_index(loc_index, data))

        new_data.append([cbo_mediana, cbo_media, cbo_desvio_padrao, dit_mediana, dit_media, dit_desvio_padrao, lcom_mediana, lcom_media, lcom_desvio_padrao, loc_soma])
    return new_data
    
# Coleta de métricas sumarizadas
if __name__ == "__main__":
    
    new_data = it_repos()
    add_data_to_csv(new_data)
