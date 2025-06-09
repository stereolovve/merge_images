# merge_images

Script para mesclar 4 imagens em um mosaico, útil para relatórios da ANTT.

## Dependências

- Python 3
- [Pillow](https://python-pillow.org/)
- [Flet](https://flet.dev/)

Instale as dependências com:

```bash
pip install Pillow flet
```

## Uso

### Mesclar imagens manualmente

Execute o script `merge_images.py` informando o caminho do arquivo de saída e as quatro imagens de entrada:

```bash
python merge_images.py mosaico.jpg imagem1.jpg imagem2.jpg imagem3.jpg imagem4.jpg
```

O arquivo `mosaico.jpg` será gerado contendo as quatro imagens dispostas em formato 2x2.

### Gerar mosaico a partir de uma pasta

Para criar o mosaico automaticamente de um ponto específico, informe a pasta com as imagens e o nome do ponto (prefixo dos arquivos). Por exemplo:

```bash
python merge_images_from_folder.py ./imagens "Ponto 001"
```

O resultado será salvo na mesma pasta com o nome `mosaico_Ponto_001.jpg`.

## Interface gráfica

Também é possível usar uma interface em [Flet](https://flet.dev/) para selecionar
as imagens e definir a posição de cada uma. Para iniciar a interface:

```bash
python merge_images_gui.py
```

Escolha até 4 imagens e utilize os dropdowns para definir onde cada uma será
colocada antes de gerar o mosaico.
