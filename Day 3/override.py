class person:
    def __init__(self,name,age,height,weight):
        self.name=name
        self.age=age
        self.height=height
        self.weight=weight

    def eat(self):
        print('vat mangso polao khay')

    def exercise(self):
        raise NotImplementedError

class cricketer(person):
    def __init__(self, name, age, height, weight,team):
        self.team=team
        super().__init__(name, age, height, weight)

    #override
    def eat(self):
        print('vegetables')

    def exercise(self):
        print('gym a poisa diya hudai gham joray')
    
    # + operator overload
    def __add__(self,other):
        return self.age + other.age
    
    # * operator overload
    def __mul__(self,other):
        return self.weight * other.weight
    
    #len overload
    def __len__(self):
        return self.height
    
    # > operator overload
    def __gt__(self,other):
        return self.age > other.age

sakib=cricketer('sakib',38,68,91,'BD')
mushi=cricketer('mushi',36,65,78,'BD')
sakib.eat()
sakib.exercise()

print(sakib+mushi)
print(sakib*mushi)
print(len(sakib))
print(sakib > mushi)

