import time

from tqdm import tqdm  # barra de progresso

NUMERO_DE_LINHAS = 1_000_000_000


def get_data_with_txt(path):

    station_data = dict()
    with open(path_do_csv, 'rb') as file:
        for line in tqdm(file, colour="CYAN", total=NUMERO_DE_LINHAS, desc="Lendo os dados",
                         bar_format='{l_bar}{bar:20}{r_bar}{bar:-20b}', unit='rows', unit_scale=True):
            row = line.split(b";")
            nome_da_station, temperatura_str = row[:2]
            temperatura = float(temperatura_str)

            if nome_da_station not in station_data:
                station_data[nome_da_station] = [
                    temperatura,
                    temperatura,
                    temperatura,
                    1,
                ]  # min, max, sum, count
            else:
                station = station_data[nome_da_station]
                if temperatura < station[0]:
                    station[0] = temperatura
                if temperatura > station[1]:
                    station[1] = temperatura
                station[2] += temperatura
                station[3] += 1

    return station_data


def processar_temperaturas(path_do_csv):
    station_data = get_data_with_txt(path_do_csv)

    print("Dados carregados. Calculando estatísticas...")

    # calculando min, média e max para cada estação
    results = {}
    for station_data in station_data.items():
        station, stats = station_data  # min, max, sum, count
        min_temp = stats[0]
        mean_temp = stats[2] / stats[3]
        max_temp = stats[1]
        results[station] = (min_temp, mean_temp, max_temp)

    print("Estatística calculada. Ordenando...")
    # ordenando os resultados pelo nome da estação
    sorted_results = dict(sorted(results.items()))

    # formatando os resultados para exibição
    formatted_results = {station: f"{min_temp:.1f}/{mean_temp:.1f}/{max_temp:.1f}"
                         for station, (min_temp, mean_temp, max_temp) in sorted_results.items()}

    return formatted_results


if __name__ == "__main__":
    try:
        # Your main code block here
        path_do_csv = "measurements.txt"

        print("Iniciando o processamento do arquivo.")
        start_time = time.time()  # Tempo de início

        resultados = processar_temperaturas(path_do_csv)

        end_time = time.time()  # Tempo de término

        for station, metrics in resultados.items():
            print(station, metrics, sep=': ')

        print(f"\nProcessamento concluído em {end_time - start_time:.2f} segundos.")
    except KeyboardInterrupt:
        print("\nOperation cancelled by user. Exiting gracefully...")
