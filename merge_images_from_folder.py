from pathlib import Path
from typing import List
import sys
from PIL import Image


def merge_images(output_path: Path, image_paths: List[Path]) -> None:
    if len(image_paths) != 4:
        raise ValueError("Sao necessarias 4 imagens")

    images = [Image.open(str(p)) for p in image_paths]
    max_w = max(img.width for img in images)
    max_h = max(img.height for img in images)
    images = [img.resize((max_w, max_h)) for img in images]

    mosaic = Image.new("RGB", (max_w * 2, max_h * 2))
    mosaic.paste(images[0], (0, 0))
    mosaic.paste(images[1], (max_w, 0))
    mosaic.paste(images[2], (0, max_h))
    mosaic.paste(images[3], (max_w, max_h))

    mosaic.save(str(output_path))
    print(f"Mosaico salvo em {output_path}")


def create_mosaic(folder: Path, point: str) -> None:
    imgs = sorted([p for p in folder.iterdir() if p.name.startswith(point)])
    if len(imgs) < 4:
        raise ValueError(f"Menos de 4 imagens encontradas para o ponto {point}")
    out_name = f"mosaico_{point.replace(' ', '_')}.jpg"
    merge_images(folder / out_name, imgs[:4])


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python merge_images_from_folder.py <pasta> <ponto>")
        sys.exit(1)
    folder = Path(sys.argv[1])
    point = sys.argv[2]
    if not folder.is_dir():
        print(f"Pasta nao encontrada: {folder}")
        sys.exit(1)
    create_mosaic(folder, point)
