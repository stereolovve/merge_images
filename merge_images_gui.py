import os
from typing import List
from PIL import Image
import flet as ft


def merge_images(output_path: str, image_paths: List[str]) -> None:
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


def main(page: ft.Page) -> None:
    page.title = "Merge Images"
    selected_images: List[str] = []
    dropdowns: List[ft.Dropdown] = []

    def update_dropdowns() -> None:
        options = [ft.dropdown.Option(key=path, text=os.path.basename(path)) for path in selected_images]
        for i, dd in enumerate(dropdowns):
            dd.options = options
            dd.value = selected_images[i] if i < len(selected_images) else None
            dd.update()

    def pick_result(e: ft.FilePickerResultEvent) -> None:
        if e.files:
            del selected_images[:]
            selected_images.extend([f.path for f in e.files][:4])
            info.value = "\n".join(os.path.basename(p) for p in selected_images)
        else:
            selected_images.clear()
            info.value = "Nenhuma imagem selecionada"
        info.update()
        update_dropdowns()

    file_picker = ft.FilePicker(on_result=pick_result)
    page.overlay.append(file_picker)

    pick_button = ft.ElevatedButton(
        "Selecionar imagens",
        on_click=lambda _: file_picker.pick_files(allow_multiple=True),
    )
    info = ft.Text("Selecione até 4 imagens.")

    for i in range(4):
        dd = ft.Dropdown(label=f"Posição {i + 1}")
        dropdowns.append(dd)

    def merge_click(e: ft.ControlEvent) -> None:
        if len(selected_images) != 4:
            page.dialog = ft.AlertDialog(title=ft.Text("Selecione 4 imagens primeiro"))
            page.dialog.open = True
            page.update()
            return
        ordered = [dd.value for dd in dropdowns]
        if None in ordered or len(set(ordered)) != 4:
            page.dialog = ft.AlertDialog(title=ft.Text("Escolha uma imagem diferente para cada posição"))
            page.dialog.open = True
            page.update()
            return
        output_path = "mosaico.jpg"
        merge_images(output_path, ordered)
        page.dialog = ft.AlertDialog(title=ft.Text(f"Mosaico salvo em {output_path}"))
        page.dialog.open = True
        page.update()

    merge_button = ft.ElevatedButton("Gerar mosaico", on_click=merge_click)

    page.add(pick_button, info, *dropdowns, merge_button)


if __name__ == "__main__":
    ft.app(target=main)
