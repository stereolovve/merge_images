##1. Visão Geral
O Fichas.py automatiza a criação de planilhas de “fichas de acesso” para cada ponto registrado em uma base Excel. Ele:

Lê a planilha de entrada (Lista_050.xlsx).

Detecta IDs duplicados e, nesses casos, inclui o nome do ponto no nome do arquivo.

Copia um modelo (Ficha_050.xlsx) para uma nova ficha por ponto.

Preenche células específicas no modelo com os dados da linha correspondente.

Salva cada ficha dentro da pasta fichas/.

##2. Pré-requisitos
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

##3. Estrutura de Pastas
Copy
Edit
seu_projeto/
├── Fichas.py
├── Lista_050.xlsx
├── Ficha_050.xlsx
└── fichas/           ← será criada pelo usuário para saída

