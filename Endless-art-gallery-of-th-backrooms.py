import random

def generate_image(width, height, colors):
  """Генерирует случайное изображение с заданными размерами и цветами.

  Args:
    width: Ширина изображения в пикселях.
    height: Высота изображения в пикселях.
    colors: Список цветов, которые будут использоваться в изображении.

  Returns:
    Массив пикселей, представляющий изображение.
  """

  image = []
  for _ in range(height):
    row = []
    for _ in range(width):
      row.append(random.choice(colors))
    image.append(row)
  return image


def save_image(image, filename):
  """Сохраняет изображение в файл.

  Args:
    image: Массив пикселей, представляющий изображение.
    filename: Имя файла, в который будет сохранено изображение.
  """

  with open(filename, "w") as f:
    for row in image:
      for pixel in row:
        f.write(pixel)
      f.write("\n")


def main():
  """Точка входа в программу."""

  # Получаем номер этажа, номер полки и номер картины на этой полке.
  floor = int(input("Введите номер этажа: "))
  shelf = int(input("Введите номер полки: "))
  picture = int(input("Введите номер картины на этой полке: "))

  # Генерируем изображение.
  image = generate_image(floor, shelf, ["0", "1"])

  # Сохраняем изображение в файл.
  filename = "image_{}_{}_{}.txt".format(floor, shelf, picture)
  save_image(image, filename)

  # Выводим сообщение об успешном сохранении изображения.
  print("Изображение успешно сохранено в файл {}.".format(filename))


if __name__ == "__main__":
  main()
