def call():
    print('calling someone,I do not know')
    return 'call done'
          
class phone:
    price=12000
    color='blue'
    brand='samsung'
    features=['camera','speaker','light']
    
    def call(self):
        print('calling one person')

    def send_sms(self,number,sms):
        text=f'sending SMS to:{number} and message:{sms}'
        return text

my_phone=phone()
print(my_phone.features)
my_phone.call()
result=my_phone.send_sms(54325,'I hate you')
print(result)
call()

