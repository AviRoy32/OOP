class laptop:
    def __init__(self,brand,price,color,memory):
        self.brand=brand
        self.price=price
        self.color=color
        self.memory=memory
    def run(self):
        return f'Running laptop:{self.brand}'
    def coding(self):
        return f'learning python and practicing'
    
class phone:
    def __init__(self,brand,name,price,color,dual_size):
        self.brand=brand
        self.name=name
        self.price=price
        self.color=color
        self.dual_size=dual_size

        def phone_call(self,number,text):
            return f'sending SMS to :{number} with: {text}'
        
class camera:
    def __init__(self,brand,price,color,pixel):
        self.brand=brand
        self.price=price
        self.color=color
        self.pixel=pixel
    
    def run(self):
        pass

    def change_lens(self):
        pass 

