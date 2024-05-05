import random
from PIL import Image, ImageDraw

def generate_infinite_rainbow_image():
    rainbow_colors = [(255, 0, 0), (255, 165, 0), (255, 255, 0), (0, 128, 0), (0, 0, 255), (75, 0, 130), (238, 130, 238)]
    image_size = (1000, 1000)  # Размер изображения
    image = Image.new('RGB', image_size)
    draw = ImageDraw.Draw(image)

    while True:
        x, y = random.randint(0, image_size[0]), random.randint(0, image_size[1])
        color = random.choice(rainbow_colors)
        draw.point((x, y), fill=color)
        image.show()

# Пример использования
generate_infinite_rainbow_image()
