import csv
import os

# Caminho do arquivo principal
caminho_arquivo_principal = r"C:\\Users\\kenne\Desktop\\Projetos\\python-ex1\\2023.csv"

# Nome do arquivo de saída
nome_arquivo_saida = "Disciplina.csv"

# Nome do arquivo de saída
nome_arquivo_saida2 = "Disciplina+Notas.csv"

# Caminho da pasta onde o arquivo de saída será salvo
caminho_pasta_saida = "C:\\Users\\kenne\\Desktop\\Projetos\\python-ex1"

# Verifica se a pasta de saída existe, e cria se necessário
if not os.path.exists(caminho_pasta_saida):
    os.makedirs(caminho_pasta_saida)

# Abre o arquivo principal para leitura
with open(caminho_arquivo_principal, "r", encoding="utf-8") as arquivo_principal:
    # Usa o Sniffer para detectar automaticamente o separador de colunas
    separador_colunas = csv.Sniffer().sniff(arquivo_principal.readline()).delimiter

    # Volta para o começo do arquivo para ler todos os dados
    arquivo_principal.seek(0)

    leitor_csv = csv.reader(arquivo_principal, delimiter=separador_colunas)

    # Abre o arquivo de saída para escrita
    with open(os.path.join(caminho_pasta_saida, nome_arquivo_saida), "w", encoding="utf-8", newline='') as arquivo_saida:
        escritor_csv = csv.writer(arquivo_saida, delimiter=";")

        # Escreve o cabeçalho do arquivo de saída
        escritor_csv.writerow(["Alunos", "Matricula"])

        # Escreve as duas primeiras colunas do arquivo principal no arquivo de saída
        for linha in leitor_csv:
            if len(linha) >= 2:
                escritor_csv.writerow([linha[0], linha[1]])

with open(caminho_arquivo_principal, "r", encoding="utf-8") as arquivo_principal:
    # Usa o Sniffer para detectar automaticamente o separador de colunas
    separador_colunas = csv.Sniffer().sniff(arquivo_principal.readline()).delimiter

    # Volta para o começo do arquivo para ler todos os dados
    arquivo_principal.seek(0)

    leitor_csv = csv.reader(arquivo_principal, delimiter=separador_colunas)

    # Abre o arquivo de saída para escrita
    with open(os.path.join(caminho_pasta_saida, nome_arquivo_saida2), "w", encoding="utf-8", newline='') as arquivo_saida:
        escritor_csv = csv.writer(arquivo_saida, delimiter=";")

        # Escreve o cabeçalho do arquivo de saída
        escritor_csv.writerow([ "Matricula","AVI","AVII","AVIII","Situação"])

        # Escreve as duas primeiras colunas do arquivo principal no arquivo de saída
        for linha in leitor_csv:
            if len(linha) >= 2:
                numero = linha[3]

                # Convertendo o número para uma string
                numero_str = str(numero)

                # Separando em três variáveis diferentes
                var1 = float(numero_str[:2] + "." + numero_str[3])
                var2 = float(numero_str[4:5] + "." + numero_str[6])
                var3 = float(numero_str[7:8] + "." + "0")

                # Calculando a média dos dois maiores valores
                maiores = [var1, var2, var3]
                maiores.sort(reverse=True)
                media = (maiores[0] + maiores[1]) / 2

                # Verificando se o aluno foi aprovado ou reprovado
                if media > 6:
                    situacao = "aprovado"
                else:
                    situacao = "reprovado"


                escritor_csv.writerow([linha[1], var1,var2,var3, situacao])

