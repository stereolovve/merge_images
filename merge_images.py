import sys
from PIL import Image


def merge_images(output_path, image_paths):
    if len(image_paths) != 4:
        raise ValueError("Four image paths are required")

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
    print(f"Saved mosaic to {output_path}")


if __name__ == "__main__":
    if len(sys.argv) != 6:
        print("Usage: python merge_images.py output_image img1 img2 img3 img4")
        sys.exit(1)

    output = sys.argv[1]
    inputs = sys.argv[2:]
    merge_images(output, inputs)
