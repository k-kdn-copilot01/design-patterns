class MealDirector:
    def __init__(self, builder):
        self._builder = builder

    def construct_meal(self):
        self._builder.add_drink()
        self._builder.add_main_course()
        self._builder.add_dessert()
