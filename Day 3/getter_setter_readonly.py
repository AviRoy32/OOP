# read only --> you can't set the value.value can't change.
# getter --> get a value of a property through a method.Most of the time,you will get the value of a private attribute.
# setter --> set a value a property through a method.most of he time,you will set the value of a private property.

class user:
    def __init__(self,name,age,money):
        self._name=name
        self._age=age
        self.__money=money
    
    #getter without any setter is randomly attribute
    @property
    def age(self):
        return self._age
    
    #getter
    @property
    def salary(self):
        return self.__money
    
    #setter
    @salary.setter
    def salary(self,value):
        if value<0:
            return 'value can not negative'
        else:
            self.__money+=value

shamsu=user('kopa',21,10000)
# print(shamsu.age())
print(shamsu.age)
#print(shamsu.salary())
print(shamsu.salary)
shamsu.salary=5000
print(shamsu.salary)

