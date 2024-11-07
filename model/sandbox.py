class Sandbox:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.field = [[None for _ in range(width)] for _ in range(height)]
        self.materials = {
            'sand': {'color': 'yellow', 'gravity': 2},
            'dirt': {'color': 'brown', 'gravity': 2},
            'water': {'color': 'blue', 'gravity': 3},
            'lava': {'color': 'red', 'gravity': 1},
        }

    def drop_material(self, x, material):
        for y in range(self.height):
            if y == self.height - 1 or self.field[y + 1][x] is not None:
                self.field[y][x] = material
                break

    def apply_gravity(self):
        for y in range(self.height - 2, -1, -1):
            for x in range(self.width):
                if self.field[y][x]:
                    material = self.field[y][x]
                    gravity = self.materials[material]['gravity']
                    if y + gravity < self.height and self.field[y + gravity][x] is None:
                        self.field[y + gravity][x] = material
                        self.field[y][x] = None

    def get_field(self):
        return self.field
