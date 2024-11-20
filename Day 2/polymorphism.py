#poly--> many
#morph-->shape

class animal:
    def __init__(self,name) -> None:
        self.name=name

    def make_sound(self):
        print('Animal making some sound')

class cat(animal):
    def __init__(self, name) -> None:
        super().__init__(name)

    def make_sound(self):
        print('meow meow')

class dog(animal):
    def __init__(self, name) -> None:
        super().__init__(name)

    def make_sound(self):
        print('geou geou')

class goat(animal):
    def __init__(self, name) -> None:
        super().__init__(name)

    def make_sound(self):
        print('beh beh')

don=cat('Real don')
don.make_sound()

shepard=dog('Local shepard')
shepard.make_sound()

mess=goat('L M')
mess.make_sound()

less=goat('gora gori')

animals=[don,shepard,mess,less]
for animal in animals:
    animal.make_sound()