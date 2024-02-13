import csv
import sys
from collections import defaultdict

def parse_csv(file):
    reader = csv.reader(file)
    header = next(reader)
    data = list(reader)
    return header, data

def obter_modalidades(data):
    return sorted({row[8] for row in data})

def percentagem_aptos_inaptos(data):
    total_atletas = len(data)
    aptos = sum(1 for row in data if row[12] == "true")
    percentagem_aptos = (aptos / total_atletas) * 100
    percentagem_inaptos = 100 - percentagem_aptos
    return percentagem_aptos, percentagem_inaptos

def faixas_etarias(data):
    faixas_etarias = defaultdict(list)
    for row in data:
        idade = int(row[5])
        faixa = f'[{idade//5*5}-{idade//5*5+4}]'
        faixas_etarias[faixa].append((row[3], row[4]))
    return faixas_etarias

def main():
    header, data = parse_csv(sys.stdin)
    modalidades = obter_modalidades(data)
    percentagem_aptos, percentagem_inaptos = percentagem_aptos_inaptos(data)
    faixas_etaria = faixas_etarias(data)

    with open('results.txt', 'w', encoding='utf-8') as file:
        file.write("\n")
        file.write("Lista ordenada alfabeticamente das modalidades desportivas:\n")
        for modalidade in modalidades:
            file.write(f"- {modalidade}\n")
        file.write("\n")
        file.write(f"Percentagem de Atletas Aptos: {percentagem_aptos}%\n")
        file.write(f"Percentagem de Atletas Inaptos: {percentagem_inaptos}%\n")
        file.write("\n")
        idades = [int(row[5]) for row in data]
        file.write(f"Idade Mínima: {min(idades)}\n")
        file.write(f"Idade Máxima: {max(idades)}\n") 
        file.write("\n")
        for faixa, nomes in faixas_etaria.items():
            file.write(f"\nFaixa etária {faixa}: {len(nomes)} atletas nesta faixa.\n")
            for primeiro_nome, ultimo_nome in nomes:
                file.write(f"{primeiro_nome} {ultimo_nome}\n")
        file.write("\n")

if __name__ == "__main__":
    main()
