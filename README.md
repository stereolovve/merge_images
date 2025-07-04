1. Visão Geral
O Fichas.py automatiza a criação de planilhas de “fichas de acesso” para cada ponto registrado em uma base Excel. Ele:

Lê a planilha de entrada (Lista_050.xlsx).

Detecta IDs duplicados e, nesses casos, inclui o nome do ponto no nome do arquivo.

Copia um modelo (Ficha_050.xlsx) para uma nova ficha por ponto.

Preenche células específicas no modelo com os dados da linha correspondente.

Salva cada ficha dentro da pasta fichas/.

2. Pré-requisitos
Python 3.7+

Pacotes Python:

bash
Copy
Edit
pip install pandas openpyxl
Arquivos necessários no mesmo diretório do script:

Lista_050.xlsx (base de dados de entrada)

Ficha_050.xlsx (modelo de ficha)

Pasta de saída:

Crie uma subpasta fichas/ para receber os arquivos gerados.

3. Estrutura de Pastas
Copy
Edit
seu_projeto/
├── Fichas.py
├── Lista_050.xlsx
├── Ficha_050.xlsx
└── fichas/           ← será criada pelo usuário para saída
4. Instruções de Uso
Ajuste de paths (opcional)
Se desejar usar outro caminho para os arquivos de entrada ou modelo, altere as variáveis no início do script:

python
Copy
Edit
df = pd.read_excel(r"C:\caminho\para\Lista_050.xlsx")
shutil.copy("Ficha_050.xlsx", new_ficha)
Criação da pasta de saída
Certifique-se de que a pasta fichas/ exista:

bash
Copy
Edit
mkdir fichas
Execução
No terminal:

bash
Copy
Edit
python Fichas.py
Ele exibirá no console:

Quantos IDs duplicados foram encontrados.

Cada arquivo criado (Criado arquivo fichas/ID.xlsx ou ID_PONTO.xlsx).

Relatório final de total de linhas, arquivos criados e erros (se houver).

5. Lógica de IDs Duplicados
IDs únicos → nome do arquivo:

Copy
Edit
fichas/12345.xlsx
IDs duplicados → inclui ponto para diferenciar:

Copy
Edit
fichas/12345_P40-C01.xlsx
(onde / no nome do ponto é substituído por - para evitar erros de sistema de arquivos).
