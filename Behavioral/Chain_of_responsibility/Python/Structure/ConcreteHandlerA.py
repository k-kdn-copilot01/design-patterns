from Handler import Handler


class ConcreteHandlerA(Handler):
    """
    Concrete Handler A handles requests that start with 'A'.
    Otherwise, it passes the request to the next handler in the chain.
    """
    
    def handle(self, request: str) -> str:
        if request.startswith('A'):
            return f"ConcreteHandlerA: I'll handle the request '{request}'"
        else:
            print(f"ConcreteHandlerA: I can't handle '{request}', passing to next handler")
            return super().handle(request)
