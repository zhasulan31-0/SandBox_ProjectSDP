class GravityHandler:
    def __init__(self, grid, cell_size, height):
        self.grid = grid
        self.cell_size = cell_size
        self.height = height

    def apply_gravity(self):
        for y in range(self.height - 2, -1, -1):  # начинаем с предпоследнего ряда
            for x in range(len(self.grid[y])):
                material = self.grid[y][x]
                if material:
                    self.move_material(x, y, material)

    def move_material(self, x, y, material):
        gravity_strength = material.gravity
        if y + 1 < len(self.grid) and self.grid[y + 1][x] is None:
            self.grid[y + 1][x] = material
            self.grid[y][x] = None
        elif y + 1 < len(self.grid) and self.grid[y + 1][x] is not None:
            target_material = self.grid[y + 1][x]
            if self.handle_interaction(material, target_material, x, y + 1):
                self.grid[y][x] = None  # Исходный материал исчезает после взаимодействия
            elif gravity_strength > 1:
                for offset in range(1, gravity_strength + 1):
                    if y + offset < len(self.grid) and self.grid[y + offset][x] is None:
                        self.grid[y + offset][x] = material
                        self.grid[y][x] = None
                        break

    def handle_interaction(self, material, target_material, x, y):
        """Обработка взаимодействия между материалами, если возможно"""
        result = material.interact(target_material)
        if result:
            self.grid[y][x] = result  # Заменяем материал в сетке на результат взаимодействия
            return True
        return False
