class Client:
    def __init__(self, prototype):
        self.prototype = prototype

    def make_copy(self):
        return self.prototype.clone()
