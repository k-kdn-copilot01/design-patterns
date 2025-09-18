class Meal:
    def __init__(self):
        self.items = []

    def add_item(self, item: str):
        self.items.append(item)

    def show_meal(self):
        print("Meal includes:", ", ".join(self.items))
