class Product:
    def __init__(self):
        self.parts = []

    def add(self, part: str):
        self.parts.append(part)

    def show(self):
        print("Product parts:", ", ".join(self.parts))
