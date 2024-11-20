from abc import ABC,abstractmethod
class animal(ABC):
    @abstractmethod
    def eat(self):
        print('I need food')
     
    @abstractmethod
    def move(self):
        pass

class monkey(animal):
    def __init__(self,name) -> None:
        self.category='Monkey'
        self.name=name
        super().__init__()

    def eat(self):
        print('I am eating banana')

    def move(self):
        print('hanging on the branches')

laika=monkey('lucky')
laika.eat()