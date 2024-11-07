class SandboxController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def handle_click(self, event):
        material = 'sand'  # Выбор материала
        self.model.drop_material(event.x, material)

    def update(self):
        self.model.apply_gravity()
        self.view.draw()
