# Conversor_lst_to_excel

Este código Python lê um arquivo de texto no formato `.lst`, extrai informações específicas de cada linha, e então salva esses dados em um arquivo Excel.  Vamos analisar passo a passo:

**Bibliotecas Utilizadas:**

* **`pandas`**: Usada para manipulação e análise de dados.  A principal função aqui é a criação de um DataFrame, que é uma estrutura de dados tabular semelhante a uma planilha, e a exportação deste DataFrame para um arquivo Excel.
* **`re`**:  Biblioteca de expressões regulares.  É usada para buscar padrões específicos dentro das linhas do arquivo `.lst`.  Expressões regulares são cruciais para extrair informações estruturadas de texto não estruturado.


**Funcionalidades do Código:**

1. **`processar_lst(arquivo_lst, arquivo_excel_saida)`**: Esta é a função principal que realiza todo o processamento. Ela recebe dois argumentos:
    * `arquivo_lst`: O caminho para o arquivo `.lst` de entrada.
    * `arquivo_excel_saida`: O caminho para o arquivo Excel de saída.

2. **Leitura do arquivo .lst**: O código abre o arquivo `.lst` usando `open()`.  A codificação `utf-7` e o tratamento de erros `errors="ignore"` sugerem que o arquivo pode conter caracteres especiais ou problemas de codificação. A versão atual do código utiliza `latin-1`, que geralmente é mais adequada para arquivos de texto com caracteres do alfabeto latino. O código lê todas as linhas do arquivo e as armazena na lista `lines`.

3. **Processamento de cada linha**: O código itera sobre cada linha da lista `lines`.
    * **Identificação do Estabelecimento**: Usa uma expressão regular (`re.search(r"Estabelecimento:\s+(\d+)", line)`) para encontrar o número do estabelecimento. Este número é armazenado na variável `estabelecimento`.
    * **Extração de dados**: Outra expressão regular (`re.match(...)`) é usada para capturar informações de cada evento em cada linha. A expressão regular identifica grupos de dados como código do evento, descrição, quantidades e valores, utilizando delimitadores de espaços. O código remove alguns caracteres indesejados da descrição.
    * **Armazenamento dos dados**: Os dados extraídos são adicionados à lista `dados` como uma lista de listas, onde cada lista interna representa uma linha do futuro arquivo Excel.

4. **Criação do DataFrame**:  Os dados da lista `dados` são usados para criar um DataFrame do pandas.  O código especifica o nome das colunas do DataFrame.

5. **Exportação para Excel**: O DataFrame é salvo como um arquivo Excel usando `df.to_excel()`.  O argumento `index=False` impede que o índice do DataFrame seja escrito no arquivo Excel.

6. **Saída para o console**: Imprime uma mensagem informando que o arquivo Excel foi gerado e seu nome.

Em resumo, este script automatiza a conversão de um arquivo `.lst` com um formato específico para um arquivo Excel mais organizado e fácil de usar para análise, utilizando expressões regulares para extrair informações relevantes.
