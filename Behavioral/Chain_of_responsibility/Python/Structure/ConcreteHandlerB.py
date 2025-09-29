from Handler import Handler


class ConcreteHandlerB(Handler):
    """
    Concrete Handler B handles requests that start with 'B'.
    Otherwise, it passes the request to the next handler in the chain.
    """
    
    def handle(self, request: str) -> str:
        if request.startswith('B'):
            return f"ConcreteHandlerB: I'll handle the request '{request}'"
        else:
            print(f"ConcreteHandlerB: I can't handle '{request}', passing to next handler")
            return super().handle(request)
