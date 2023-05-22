blance=3000

def buy(items,price):
    global blance
    if blance>=price:
        blance-=price
        print(f'You have bought {items} and your blance is {blance} after buying')
    else:
        print('You have not enough money')

buy('pen',10000)