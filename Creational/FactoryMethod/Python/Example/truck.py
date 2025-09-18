from transport import Transport

class Truck(Transport):
    def deliver(self) -> str:
        return "Deliver by land in a truck"
