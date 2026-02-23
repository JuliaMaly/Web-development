from abc import ABC, abstractmethod

class Transport(ABC):
    @abstractmethod
    def deliver(self):
        pass


class Truck(Transport):
    def deliver(self):
        return "Delivery by land in a box."


class Ship(Transport):
    def deliver(self):
        return "Delivery by sea in a container."


class Logistics(ABC):
    @abstractmethod
    def create_transport(self) -> Transport:
        pass

    def plan_delivery(self):
        transport = self.create_transport()
        return transport.deliver()


class RoadLogistics(Logistics):
    def create_transport(self):
        return Truck()


class SeaLogistics(Logistics):
    def create_transport(self):
        return Ship()


if __name__ == "__main__":
    logistics = RoadLogistics()
    print(logistics.plan_delivery())

    logistics = SeaLogistics()
    print(logistics.plan_delivery())