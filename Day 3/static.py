class shopping:
    cart=[]  #class attribute #static attribute
    origin='china'
    def __init__(self,name,location):
        self.name=name     #instance attribute
        self.location=location

    def purchase(self,item,price,amount):
        remaining=amount-price
        print(f'buying: {item} for price: {price} and remaining: {remaining}')

    @classmethod
    def hudai_dekhi(self,item):
        print('kinmu na kono',item)

    @staticmethod
    def multiply(a,b):
        result= a*b
        print(result)


bashundara=shopping('basu en dhara', 'not popular location')
#bashundara.purchase('lungi',500,1000)
bashundara.hudai_dekhi('lungi')
shopping.hudai_dekhi('Lungi')
shopping.multiply(5,4) #static method

