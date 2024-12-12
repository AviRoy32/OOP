class CPU:
    def __init__(self,cores):
        self.cores=cores

class RAM:
    def __init__(self,size):
        self.size=size

class HardDrive:
    def __init__(self,capacity):
        self.capacity=capacity

#computer has a cpu
#computer has a ram
#computer has a hard drive
class computer:
    def __init__(self,cores,ram_size,hard_capacity):
        self.cpu=CPU(cores)
        self.ram=RAM(ram_size)
        self.hard_disc=HardDrive(hard_capacity)


mac=computer(8,16,512)