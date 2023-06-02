def call():
    print("calling....")
    return 'call done'

class Phone:
    price=19000
    color='blue'
    brand='OnePlus'
    features=['camera','fm','games','picture']
    def call(self):
        print('calling ma')
    def send_sms(self,phone,sms):
        text=f'sending sms to:{phone} and msg is:{sms}'
        return text

my_phone=Phone()
print(my_phone.features)
my_phone.call()
result=my_phone.send_sms(1724232342,'Missing you')
print(result)