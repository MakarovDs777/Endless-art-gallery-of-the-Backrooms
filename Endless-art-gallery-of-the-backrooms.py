import random
from PIL import Image

def generate_rainbow_image(shelf_number, shelf_position):
    rainbow_colors = [(255, 0, 0), (255, 165, 0), (255, 255, 0), (0, 128, 0), (0, 0, 255), (75, 0, 130), (238, 130, 238)]
    image_size = (shelf_position * 100, shelf_position * 100)
    new_image = Image.new('RGB', image_size)

    pixels = new_image.load()
    for i in range(image_size[0]):
        for j in range(image_size[1]):
            pixels[i, j] = random.choice(rainbow_colors)

    new_image.save(f"shelf_{shelf_number}_position_{shelf_position}_rainbow_image.png")

# Пример использования
generate_rainbow_image(1, 1)  # Генерирует радужное изображение для полки 1, позиция 1
generate_rainbow_image(1, 3)  # Создает радужное изображение для полки 1, позиция 3
