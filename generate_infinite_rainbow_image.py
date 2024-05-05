import random
from PIL import Image, ImageDraw, ImageTk
import tkinter as tk

def generate_infinite_rainbow_image():
    rainbow_colors = [(255, 0, 0), (255, 165, 0), (255, 255, 0), (0, 128, 0), (0, 0, 255), (75, 0, 130), (238, 130, 238)]
    image_size = (1000, 1000)  # Размер изображения
    image = Image.new('RGB', image_size)
    draw = ImageDraw.Draw(image)

    root = tk.Tk()
    root.title("Infinite Rainbow Image")

    canvas = tk.Canvas(root, width=image_size[0], height=image_size[1])
    canvas.pack()

    tk.Label(root, text="X:").pack(side="left")
    x_entry = tk.Entry(root)
    x_entry.pack(side="left")
    tk.Label(root, text="Y:").pack(side="left")
    y_entry = tk.Entry(root)
    y_entry.pack(side="left")
    tk.Label(root, text="Z:").pack(side="left")
    z_entry = tk.Entry(root)
    z_entry.pack(side="left")

    def update_coordinates():
        x = int(x_entry.get())
        y = int(y_entry.get())
        z = int(z_entry.get())
        draw.point((x, y), fill=rainbow_colors[z % len(rainbow_colors)])
        image_tk = ImageTk.PhotoImage(image)
        canvas.create_image(0, 0, anchor=tk.NW, image=image_tk)
        canvas.image = image_tk

    update_button = tk.Button(root, text="Enter", command=update_coordinates)
    update_button.pack()

    root.mainloop()

# Пример использования
generate_infinite_rainbow_image()
