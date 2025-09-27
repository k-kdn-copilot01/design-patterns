import copy

class DocumentPrototype:
    def __init__(self, title, content, tags=None):
        self.title = title
        self.content = content
        self.tags = tags if tags else []

    def clone(self, deep=False):
        if deep:
            return copy.deepcopy(self)
        return copy.copy(self)
