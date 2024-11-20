class poribohon:
    def __init__(self,name,address):
        self.name=name
        self.bus=[]
        self.route=[]
        self.counter=[]
        self.drivers=[]
        self.supervisors=[]
        self.manager=[]
        self.fare=[]
class driver:
    def __init__(self,name,license,age):
        self.name=name
        self.license=license
        self.age=age

class counter:
    def __init__(self) -> None:
        pass
    def __init__(self,start,destination) -> None:
        pass
class passenger:
    pass
class supervisor:
    pass


red_mia=driver('a','b',32)
