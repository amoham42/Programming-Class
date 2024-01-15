import tkinter as tk
from PIL import Image, ImageDraw
import cv2
import numpy as np  # Import NumPy for array conversion

class CanvasApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Canvas Drawing App")

        self.canvas_size = 28
        self.zoom_factor = 10
        canvas_width = self.canvas_size * self.zoom_factor
        canvas_height = self.canvas_size * self.zoom_factor
        self.canvas = tk.Canvas(root, bg="white", width=canvas_width, height=canvas_height)
        self.canvas.pack(expand=tk.YES, fill=tk.BOTH)
        save_button = tk.Button(root, text="Save", command=self.save_canvas)
        save_button.pack(side=tk.BOTTOM)
        self.im = Image.new("RGB", (canvas_width, canvas_height), color="white")
        self.drawing_image = ImageDraw.Draw(self.im)
        self.canvas.bind("<B1-Motion>", self.draw_square)

    def draw_square(self, event):
        x = event.x // self.zoom_factor
        y = event.y // self.zoom_factor

        x1, y1 = x * self.zoom_factor, y * self.zoom_factor
        x2, y2 = x1 + self.zoom_factor, y1 + self.zoom_factor
        self.canvas.create_rectangle(x1, y1, x2, y2, fill="black", outline="black")
        self.drawing_image.rectangle([x1, y1, x2, y2], fill="black")

    def save_canvas(self):

        img_array = np.array(self.im)
        resized_img = cv2.resize(img_array, (self.canvas_size, self.canvas_size))
        cv2.imwrite("digit.png", resized_img)


if __name__ == "__main__":
    root = tk.Tk()
    app = CanvasApp(root)
    root.mainloop()
