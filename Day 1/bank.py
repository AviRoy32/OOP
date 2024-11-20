class bank:
    def __init__(self,balance):
        self.balance=balance
        self.min_withdraw=100
        self.max_withdraw=100000

    def get_balance(self):
        return self.balance
    
    def deposit(self,amount):
        if amount>0:
            self.balance+=amount

    def withdraw(self,amount):
        if amount< self.min_withdraw:
            print(f'very less amount.you can not withdraw below {self.min_withdraw}')
        elif amount>self.max_withdraw:
            print(f'very high amount.you can not withdraw above {self.max_withdraw}')
        else:
            self.balance-=amount
            print(f'here is your money {amount}')
            print(f'your balance after withdraw {self.balance}')


brac=bank(15000)
brac.withdraw(25)
brac.withdraw(1000000)
brac.withdraw(5000)


dbbl=bank(5000)
dbbl.deposit(3000)
dbbl.deposit(2000)
print(dbbl.get_balance())