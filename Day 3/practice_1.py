class Person:
    def __init__(self, name, age, height, weight) -> None:
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

class Cricketer(Person):
    def __init__(self, name, age, height, weight) -> None:
        super().__init__(name, age, height, weight)

    # Overloading the '>' operator to compare age
    def __gt__(self, other):
        return self.age > other.age

# Creating instances
sakib = Cricketer('Sakib', 38, 68, 91)
musfiq = Cricketer('Rahim', 36, 68, 88)
kamal = Cricketer('Kamal', 39, 68, 94)
jack = Cricketer('Jack', 38, 68, 91)
kalam = Cricketer('Kalam', 37, 68, 95)

# Comparing players
players = [sakib, musfiq, kamal, jack, kalam]
oldest = players[0]
for player in players[1:]:
    if player > oldest:
        oldest = player

print(f"The oldest cricketer is {oldest.name} with age {oldest.age}.")
