class calculator:
    brand='casio MS100'

    def add(self,num1,num2):
        return num1+num2

    def subtrac(self,num1,num2):
        return num1-num2

    def multi(self,num1,num2):
        return num1*num2

    def divide(self,num1,num2):
        return num1/num2

my_calcu=calculator()   
res=my_calcu.add(5,2)
print(res)
r=my_calcu.subtrac(5,2)
print(r)
ans=my_calcu.multi(5,3)
print(ans)
result=my_calcu.divide(15,3)
print(result)
