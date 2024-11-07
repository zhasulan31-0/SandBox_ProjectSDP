import tkinter as tk


class SandboxView:
    def __init__(self, root, sandbox):
        self.sandbox = sandbox
        self.canvas = tk.Canvas(root, width=sandbox.width, height=sandbox.height, bg='black')
        self.canvas.pack()

    def draw(self):
        self.canvas.delete('all')
        for y in range(self.sandbox.height):
            for x in range(self.sandbox.width):
                material = self.sandbox.field[y][x]
                if material:
                    color = self.sandbox.materials[material]['color']
                    self.canvas.create_rectangle(x, y, x + 1, y + 1, outline=color, fill=color)
