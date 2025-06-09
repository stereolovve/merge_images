import os
from typing import List, Dict
from PIL import Image
import re


def merge_images(output_path: str, image_paths: List[str]) -> None:
    """Merge 4 imagens para um mosaico 2x2."""
    if len(image_paths) != 4:
        raise ValueError("Necessário 4 imagens")

    images = [Image.open(p) for p in image_paths]
    max_w = max(img.width for img in images)
    max_h = max(img.height for img in images)
    images = [img.resize((max_w, max_h)) for img in images]

    mosaic = Image.new("RGB", (max_w * 2, max_h * 2))
    mosaic.paste(images[0], (0, 0))
    mosaic.paste(images[1], (max_w, 0))
    mosaic.paste(images[2], (0, max_h))
    mosaic.paste(images[3], (max_w, max_h))

    mosaic.save(output_path)


def get_ponto_number(filename: str) -> str:
    """Extrair o número do Ponto do nome do arquivo."""
    match = re.search(r'Ponto (\d+)', filename)
    return match.group(1) if match else None


def process_folder(folder_path: str, output_dir: str) -> None:
    """Processar todas as imagens na pasta e criar mosaicos."""
    # Agrupar imagens por número do Ponto
    ponto_groups: Dict[str, List[str]] = {}
    
    image_files = [f for f in os.listdir(folder_path) 
                  if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    
    # Agrupar imagens por número do Ponto
    for filename in image_files:
        ponto_num = get_ponto_number(filename)
        if ponto_num:
            if ponto_num not in ponto_groups:
                ponto_groups[ponto_num] = []
            ponto_groups[ponto_num].append(os.path.join(folder_path, filename))
    
    # Processar cada grupo
    for ponto_num, images in ponto_groups.items():
        if len(images) == 4:
            # Ordenar imagens para garantir ordem consistente
            images.sort()
            mosaic_path = os.path.join(output_dir, f"Ponto {ponto_num}_Mosaico.jpg")
            try:
                merge_images(mosaic_path, images)
                print(f"Mosaico criado com sucesso: {mosaic_path}")
            except Exception as e:
                print(f"Erro ao criar mosaico para Ponto {ponto_num}: {str(e)}")
        else:
            print(f"Ponto {ponto_num} tem {len(images)} imagens (precisa de 4)")


def main():
    folder_path = r"C:\Users\lucas.melo\merge_images\prints"
    output_dir = r"C:\Users\lucas.melo\merge_images\mosaicos"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    process_folder(folder_path, output_dir)


if __name__ == "__main__":
    main()
