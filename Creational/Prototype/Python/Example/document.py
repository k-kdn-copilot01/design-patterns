import copy

class Document:
    def __init__(self, title: str, content: str):
        self.title = title
        self.content = content

    def clone(self):
        # deep copy to ensure independence
        return copy.deepcopy(self)

    def __str__(self):
        return f"Document(title='{self.title}', content='{self.content}')"
