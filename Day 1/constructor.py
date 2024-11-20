class phone:
    manufactured='china'
    
    def __init__(self,owner,brand,price):
        self.owner=owner
        self.brand=brand
        self.price=price

my_phone=phone('Avi Roy','samsung',14000)
print(my_phone.owner,my_phone.brand,my_phone.price)

her_phone=phone('ashasi','oppo',10000)
print(her_phone.owner,her_phone.brand,her_phone.price)
