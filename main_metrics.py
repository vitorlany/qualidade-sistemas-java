import csv
import numpy as np

file_path = './ck_results/--/class.csv'

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

def extract_data(file_path):
    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        csv_file_reader = csv.reader(file)

        data = []
        for line in csv_file_reader:
            data.append(line)
        data.pop(0)
        return data

def generate_metrics(index, data):
    values = get_data_by_column_index(index, data)
    mediana, media, desvio_padrao = calc_metrics(values)
    return mediana, media, desvio_padrao

if __name__ == "__main__":
    data = extract_data(file_path)

    cbo_index = 3
    dit_index = 8
    lcom_index = 11

    cbo_mediana, cbo_media, cbo_desvio_padrao = generate_metrics(cbo_index, data)
    dit_mediana, dit_media, dit_desvio_padrao = generate_metrics(dit_index, data)
    lcom_mediana, lcom_media, lcom_desvio_padrao = generate_metrics(lcom_index, data)

    print(f'CBO: Mediana: {cbo_mediana}, Média: {cbo_media}, Desvio Padrão: {cbo_desvio_padrao}')
    print(f'DIT: Mediana: {dit_mediana}, Média: {dit_media}, Desvio Padrão: {dit_desvio_padrao}')
    print(f'LCOM: Mediana: {lcom_mediana}, Média: {lcom_media}, Desvio Padrão: {lcom_desvio_padrao}')
    
