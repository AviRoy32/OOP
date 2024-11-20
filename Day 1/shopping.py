class shopping:
    def __init__(self,name):
        self.name=name
        self.cart=[]

    def add_to_cart(self,item,price,quantity):
        product={'item':item,'price':price,'quantity':quantity}
        self.cart.append(product)

    def checkout(self,amount):
        total=0
        for item in self.cart:
            #print(item)
            total+=item['price']*item['quantity']
        if total>amount:
            print(f'please provide {total-amount} more')
        else:
            extra=amount-total
            print(f'Here is your items and extra money {extra}')

avi=shopping('Avi Roy')
avi.add_to_cart('alu',50,6)
avi.add_to_cart('dim',12,24)
avi.add_to_cart('rice',50,5)

print(avi.cart)

avi.checkout(500)
avi.checkout(1500)
