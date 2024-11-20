#encapsulation---> hide details
#access modifier---> public,private,protected

class bank:
    def __init__(self,holder_name,initial_deposit) -> None:
        self.holder_name=holder_name  #public
        self._branch='banani 11'      #protected
        self.__balance=initial_deposit #private

    def deposit(self,amount):
        self.__balance+=amount

    def get_balance(self):
        return self.__balance
    
    def withdraw(self,amount):
        if amount < self.__balance:
            self.__balance-=amount
            return amount


rafsan=bank('Avi',10000)
print(rafsan.holder_name)
rafsan.deposit(40000)
print(rafsan.get_balance())
print(rafsan._branch)

#print(dir(rafsan))
print(rafsan._bank__balance)  # private value jur kore dekte caile