import pandas as pd
import re

# Função para ler e processar o arquivo .lst
def processar_lst(arquivo_lst, arquivo_excel_saida):
    # Abrir o arquivo .lst
    with open(arquivo_lst, "r", encoding="latin-1", errors="ignore") as file:
        lines = file.readlines()

    # Variáveis para armazenar os dados
    estabelecimento = None
    dados = []

    # Processar cada linha do arquivo
    for line in lines:
        line = line.strip()

        # Capturar o número do estabelecimento
        match_estab = re.search(r"Estabelecimento:\s+(\d+)", line)
        if match_estab:
            estabelecimento = match_estab.group(1)
            continue  # Pula para a próxima linha após encontrar o estabelecimento

        # Capturar as linhas de dados (eventos)
        # Expressão regular aprimorada para lidar com caracteres especiais e espaços extras
        match_data = re.match(r"(\d+)\s+(.+?)\s+([\d\.,]+)\s+([\d\.,]+)\s+([\d\.,]+)\s+([\d\.,]+)\s+([\+\-\d\.,]+)", line)
        if match_data:
            descricao = match_data.group(2).strip()
            # Remove caracteres indesejados da descrição
            descricao = re.sub(r'[.,()\[\]{}]', '', descricao)
            descricao = ' '.join(descricao.split()) # remove espaços duplicados
            dados.append([
                estabelecimento,
                match_data.group(1),  # Código do evento
                descricao,  # Descrição (limpa)
                match_data.group(3),  # Quantidade mês 1
                match_data.group(4),  # Valor mês 1
                match_data.group(5),  # Quantidade mês 2
                match_data.group(6),  # Valor líquido mês 2
                match_data.group(7)   # Diferença
            ])

    # Criar DataFrame
    colunas = ["Estabelecimento", "Código", "Descrição", "Qtd 01/2025", "Valor 01/2025", "Qtd 02/2025", "Valor 02/2025", "Liq"]
    df = pd.DataFrame(dados, columns=colunas)

    # Salvar como arquivo Excel
    df.to_excel(arquivo_excel_saida, index=False)
    print(f"Arquivo Excel gerado: {arquivo_excel_saida}")

# Caminho do arquivo .lst e do arquivo Excel de saída
arquivo_lst = "esfp0003.lst"  # Substitua pelo caminho do seu arquivo .lst
arquivo_excel_saida = "esfp0003.xlsx"  # Caminho do arquivo Excel de saída

# Chamar a função para processar
processar_lst(arquivo_lst, arquivo_excel_saida)
