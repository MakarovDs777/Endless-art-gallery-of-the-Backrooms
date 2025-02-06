import random
from PIL import Image, ImageDraw, ImageTk
import tkinter as tk

class InfiniteNoiseImage:
    def __init__(self):
        self.image_size = (800, 600)  # Размер изображения
        self.x, self.y = 0, 0  # Начальные координаты
        self.seed = random.randint(0, 10000)  # Случайный сид
        self.is_moving = False

        self.root = tk.Tk()
        self.root.title("Infinite Noise Image")

        self.canvas = tk.Canvas(self.root, width=self.image_size[0], height=self.image_size[1])
        self.canvas.pack()

        # Метка для отображения координат
        self.coordinates_label = tk.Label(self.root, text=f"Координаты - X: {self.x}, Y: {self.y}, Seed: {self.seed}")
        self.coordinates_label.pack()

        # Поле ввода скорости обновления
        tk.Label(self.root, text="Скорость обновления (мс):").pack(side="top", anchor="w")
        self.speed_entry = tk.Entry(self.root)
        self.speed_entry.pack(side="left", anchor="w")
        self.speed_entry.insert(0, "1000")  # Значение по умолчанию

        # Панель с кнопками
        buttons_frame = tk.Frame(self.root)
        buttons_frame.pack(side="top", anchor="ne")  # Выравнивание по правому верхнему углу

        self.update_button = tk.Button(buttons_frame, text="Сгенерировать изображение", command=self.update_image)
        self.update_button.pack(side="left", anchor="ne")

        self.move_button = tk.Button(buttons_frame, text="Авто-обновление", command=self.toggle_auto_move)
        self.move_button.pack(side="left", anchor="ne")

        # Добавляем кнопки для перемещения в одной строке
        move_buttons_frame = tk.Frame(buttons_frame)
        move_buttons_frame.pack(side="left", anchor="ne")

        left_button = tk.Button(move_buttons_frame, text="←", command=self.move_left)
        left_button.pack(side="left", anchor="ne")

        up_button = tk.Button(move_buttons_frame, text="↑", command=self.move_up)
        up_button.pack(side="left", anchor="ne")

        down_button = tk.Button(move_buttons_frame, text="↓", command=self.move_down)
        down_button.pack(side="left", anchor="ne")

        right_button = tk.Button(move_buttons_frame, text="→", command=self.move_right)
        right_button.pack(side="left", anchor="ne")

        self.image = Image.new('RGB', self.image_size)

        self.root.mainloop()

    def generate_noise(self):
        for x in range(self.image_size[0]):
            for y in range(self.image_size[1]):
                # Генерация случайного цвета для каждой точки изображения
                r = random.randint(0, 255)
                g = random.randint(0, 255)
                b = random.randint(0, 255)
                self.image.putpixel((x, y), (r, g, b))

    def update_image(self):
        self.generate_noise()
        self.update_canvas()
        self.update_coordinates_display()  # Обновить отображение координат

    def update_canvas(self):
        image_tk = ImageTk.PhotoImage(self.image)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=image_tk)
        self.canvas.image = image_tk  # Сохранение ссылки на изображение

    def update_coordinates_display(self):
        self.coordinates_label.config(text=f"Координаты - X: {self.x}, Y: {self.y}, Seed: {self.seed}")

    def toggle_auto_move(self):
        if self.is_moving:
            self.is_moving = False
            self.move_button.config(text="Авто-обновление")
        else:
            self.is_moving = True
            self.move_button.config(text="Остановить обновление")
            self.auto_move()

    def auto_move(self):
        if self.is_moving:
            self.update_image()  # Обновить изображение цветного шума
            speed = int(self.speed_entry.get()) if self.speed_entry.get().isdigit() else 1000
            self.root.after(speed, self.auto_move)  # Обновление через `speed` мс

    def move_left(self):
        self.x -= 1
        self.update_image()

    def move_right(self):
        self.x += 1
        self.update_image()

    def move_up(self):
        self.y += 1
        self.update_image()

    def move_down(self):
        self.y -= 1
        self.update_image()

# Пример использования
InfiniteNoiseImage()
