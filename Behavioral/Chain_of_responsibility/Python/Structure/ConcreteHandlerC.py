from Handler import Handler


class ConcreteHandlerC(Handler):
    """
    Concrete Handler C handles requests that start with 'C'.
    Otherwise, it passes the request to the next handler in the chain.
    """
    
    def handle(self, request: str) -> str:
        if request.startswith('C'):
            return f"ConcreteHandlerC: I'll handle the request '{request}'"
        else:
            print(f"ConcreteHandlerC: I can't handle '{request}', passing to next handler")
            return super().handle(request)
