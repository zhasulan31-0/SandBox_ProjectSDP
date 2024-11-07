class Material:
    def __init__(self, name, color, gravity):
        self.name = name
        self.color = color
        self.gravity = gravity

    def interact(self, other_material):
        """Метод взаимодействия по умолчанию, который можно переопределить в подклассах"""
        return None


class Sand(Material):
    def __init__(self):
        super().__init__("sand", "yellow", 2)

    def interact(self, other_material):
        if other_material.name == 'lava':
            return Glass()
        return None


class Water(Material):
    def __init__(self):
        super().__init__("water", "blue", 3)

    def interact(self, other_material):
        if other_material.name == 'lava':
            return Obsidian()
        if other_material.name == 'dirt':
            return Mud()
        return None


class Lava(Material):
    def __init__(self):
        super().__init__("lava", "red", 1)

    def interact(self, other_material):
        if other_material.name == 'water':
            return Obsidian()
        if other_material.name == 'sand':
            return Glass()
        return None
class Dirt(Material):
    def __init__(self):
        super().__init__("dirt", "brown", 2)
    def interact(self, other_material):
        if other_material.name == 'water':
            return Mud()
        return None



class Mud(Material):
    def __init__(self):
        super().__init__("mud", "gray", 2)


class Obsidian(Material):
    def __init__(self):
        super().__init__("obsidian", "black", 0)


class Glass(Material):
    def __init__(self):
        super().__init__("glass", "lightblue", 0)

class MaterialFactory:
    @staticmethod
    def create_material(material_type):
        if material_type == 'sand':
            return Sand()
        elif material_type == 'water':
            return Water()
        elif material_type == 'lava':
            return Lava()
        elif material_type == 'dirt':
            return Dirt()
        else:
            raise ValueError(f"Unknown material type: {material_type}")
