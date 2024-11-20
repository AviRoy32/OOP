class vehicle:
    def __init__(self,name,price):
        self.name=name
        self.price=price

    def __repr__(self) -> str:
       return f'{self.name} {self.price}'

    def move(self):
        pass

class bus(vehicle):
    def __init__(self, name, price,seat):
        self.seat=seat
        super().__init__(name, price)

    def __repr__(self) -> str:
        return super().__repr__()

class truck(vehicle):
    def __init__(self, name, price,weight):
        self.weight=weight
        super().__init__(name, price)

class PickUpTruck(truck):
    def __init__(self, name, price, weight):
        super().__init__(name, price, weight)

class ACBus(bus):
    def __init__(self, name, price, seat,temperature):
        self.temperature=temperature
        super().__init__(name, price, seat)

    def __repr__(self) -> str:
        print(f'{self.seat}')
        return super().__repr__()

greenLine=ACBus('green',40000,40,16)
print(greenLine)

"""
1.simple inheritance: parent class-->child class (device-->phone) (device-->laptop)
2.milti-level inheritance:Grand-->parent-->child(vehicle-->bus-->ACBus) (vehicle-->Truck--> pickupRruck)
3.multiple inheritance:Student(Family,School,Sports)
4.Hybrid: Grand-->Father,uncle,Aunty -->child(Father,uncle)

"""