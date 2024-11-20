#base class,parent class,common attribute+ functionality class
#derived class,child class,uncommon attribute+ functionality class
class device:
    def __init__(self,brand,price,color,origin) :
        self.brand=brand
        self.price=price
        self.color=color
        self.origin=origin
    
    def run(self):
        return f'Running laptop:{self.brand}'

class laptop:
    def __init__(self,memory,ssd):
        self.ssd=ssd
        self.memory=memory

    def coding(self):
        return f'learning python and practicing'
    
class phone(device):
    def __init__(self,brand,price,color,origin,dual_size):
        self.dual_sim=dual_size
        super().__init__(brand,price,color,origin)

    def phone_call(self,number,text):
        return f'sending SMS to :{number} with: {text}'
    
    def __repr__(self) -> str:
        return f'phone:{self.brand} {self.price} {self.dual_sim}'
        
class camera:
    def __init__(self,pixel):
        self.pixel=pixel

    def change_lens(self):
        pass 

    #inheritance
    myPhone=phone('Iphone',120000,'silver','china',True)
    print(myPhone.brand)
    print(myPhone)

