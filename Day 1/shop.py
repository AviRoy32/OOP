class shop:
    cart=[]  #cart is an class attribute
    def __init__(self,buyer):
        self.buyer=buyer

    def add_to_cart(self,item):
        self.cart.append(item)

avi=shop('Avi')
avi.add_to_cart('glass')
avi.add_to_cart('mobile')
print(avi.cart)

anik=shop('Anik')
anik.add_to_cart('tea')
anik.add_to_cart('saban')
print(anik.cart)
       