# PEL218 - Exercício 01

Escolher qualquer corpus (conjunto de documentos) ou livro de at́e 100 MB em português e extrair as seguintes informações:

- Quantidade de palavras distintas;

- Histograma das palavras;

- Histograma de prefixos de tamanho (1,2,3,4 e 5)

- Histograma de sufixos de tamanho (1,2,3,4 e 5)

Você poderá utilizar qualquer linguagem de programação (inclusive shell).

## Relatório
Para esta atividade foi escolhido um conjunto de notícias do jornal A Folha de São Paulo contendo aproximadamente 30 mil artigos.

Para iniciar a análise foi necessário preparar o corpus. Esta preparação incluiu os seguintes passos:

1. Remover os caracteres especiais e pontuação;

2. Transformar todos os caracteres para minúscula;

3. Remover quebras de linha;

4. Remover espaços duplicados.

Após esta preparação o corpus continha 14.779.320 de palavras, porém muitas delas repetidas quando removemos as repetições pudemos identificar 184.462 palavras únicas.

### Frequência de palavras
Analisando o corpus pela frequência de palavras temos a lista abaixo com as 25 mais frequentes:

![alt text](https://raw.githubusercontent.com/gbodra/mestrado-ia-pel218-trabalho01/main/images/frequent_words.png "Top 25")

### Prefixos

Prefixo de tamanho 1

![alt text](https://raw.githubusercontent.com/gbodra/mestrado-ia-pel218-trabalho01/main/images/prefix_1.png "Prefixo 1")

Prefixo de tamanho 2

![alt text](https://raw.githubusercontent.com/gbodra/mestrado-ia-pel218-trabalho01/main/images/prefix_2.png "Prefixo 2")

Prefixo de tamanho 3

![alt text](https://raw.githubusercontent.com/gbodra/mestrado-ia-pel218-trabalho01/main/images/prefix_3.png "Prefixo 3")

Prefixo de tamanho 4

![alt text](https://raw.githubusercontent.com/gbodra/mestrado-ia-pel218-trabalho01/main/images/prefix_4.png "Prefixo 4")

Prefixo de tamanho 5

![alt text](https://raw.githubusercontent.com/gbodra/mestrado-ia-pel218-trabalho01/main/images/prefix_5.png "Prefixo 5")

### Sufixos

Sufixo de tamanho 1

![alt text](https://raw.githubusercontent.com/gbodra/mestrado-ia-pel218-trabalho01/main/images/suffix_1.png "Sufix 1")

Sufixo de tamanho 2

![alt text](https://raw.githubusercontent.com/gbodra/mestrado-ia-pel218-trabalho01/main/images/suffix_2.png "Sufix 2")

Sufixo de tamanho 3

![alt text](https://raw.githubusercontent.com/gbodra/mestrado-ia-pel218-trabalho01/main/images/suffix_3.png "Sufix 3")

Sufixo de tamanho 4

![alt text](https://raw.githubusercontent.com/gbodra/mestrado-ia-pel218-trabalho01/main/images/suffix_4.png "Sufix 4")

Sufixo de tamanho 5

![alt text](https://raw.githubusercontent.com/gbodra/mestrado-ia-pel218-trabalho01/main/images/suffix_5.png "Sufix 5")