class Director:
    def __init__(self, builder):
        self._builder = builder

    def construct(self):
        self._builder.build_part_a()
        self._builder.build_part_b()
