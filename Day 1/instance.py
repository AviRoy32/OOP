class shop:
    shopping_mall='jamuna'
    def __init__(self,buyer):
        self.buyer=buyer
        self.cart=[]  #cart is an instance attribute

    def add_to_cart(self,item):
        self.cart.append(item)

avi=shop('Avi')
avi.add_to_cart('watch')
avi.add_to_cart('mouse')
print(avi.cart)


anik=shop('Anik')
anik.add_to_cart('pen')
anik.add_to_cart('pant')
print(anik.cart)
    