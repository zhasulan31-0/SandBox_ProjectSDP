import tkinter as tk
from material import MaterialFactory
from gravity_handler import GravityHandler
import time

WIDTH, HEIGHT = 400, 400
CELL_SIZE = 10
MATERIALS = ['sand', 'water', 'lava', 'dirt']


class SandBoxApp:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)
        self.canvas.pack()

        self.panel = tk.Frame(root)
        self.panel.pack(side="top", fill="x")

        self.material_label = tk.Label(self.panel, text="Текущий материал: sand")
        self.material_label.pack(side="left")

        self.switch_button = tk.Button(self.panel, text="Переключить материал", command=self.switch_material)
        self.switch_button.pack(side="left")

        self.grid = [[None for _ in range(WIDTH // CELL_SIZE)] for _ in range(HEIGHT // CELL_SIZE)]
        self.material = 'sand'
        self.gravity_handler = GravityHandler(self.grid, CELL_SIZE, HEIGHT // CELL_SIZE)
        self.last_physics_update = time.time()
        self.physics_interval = 0.1

        self.canvas.bind('<Button-1>', self.place_material)
        self.canvas.bind('<Button-3>', self.switch_material)

        self.update_grid()
        self.update_canvas()
        self.update_physics()

    def update_canvas(self):
        self.canvas.delete("all")
        self.update_grid()
        self.root.after(50, self.update_canvas)

    def update_physics(self):
        if time.time() - self.last_physics_update >= self.physics_interval:
            self.last_physics_update = time.time()
            self.gravity_handler.apply_gravity()
            self.update_grid()
        self.root.after(100, self.update_physics)

    def place_material(self, event):
        x = event.x // CELL_SIZE
        y = event.y // CELL_SIZE
        if 0 <= x < WIDTH // CELL_SIZE and 0 <= y < HEIGHT // CELL_SIZE:
            self.grid[y][x] = MaterialFactory.create_material(self.material)

    def switch_material(self):
        current_index = MATERIALS.index(self.material)
        self.material = MATERIALS[(current_index + 1) % len(MATERIALS)]
        self.material_label.config(text=f"Текущий материал: {self.material}")

    def update_grid(self):
        for y in range(HEIGHT // CELL_SIZE):
            for x in range(WIDTH // CELL_SIZE):
                material = self.grid[y][x]
                color = material.color if material else 'white'
                self.canvas.create_rectangle(x * CELL_SIZE, y * CELL_SIZE,
                                             (x + 1) * CELL_SIZE, (y + 1) * CELL_SIZE,
                                             fill=color, outline='black')


def main():
    root = tk.Tk()
    app = SandBoxApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
