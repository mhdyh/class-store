import time
import datetime

class Store:
    def __init__(self,products):
        self.products=products
        
    def buy(self):
        x=input("What do you want to buy?")
        self.products.append(x)
        print(self.products)

    def sell(self):
        i=input("What product you want to sell?")
        self.products.remove(i)
        print(self.products)

    def changing(self):
        y=input("What product do you remove?")
        g=input("What product do you replace?")
        self.products.remove(y)
        self.products.append(g)
        print(self.products)

    def show(self):
        print(self.products)

    def now_time(self):
        print(time.ctime())

    def now_date(self):
        print(datetime.datetime.today())


product1=Store([])
while True:
    print("you can choose services 0-6!")
    k=int(input("which service do you want?"))
    if k==0:
        print("Closed!")
        break
    elif k==1:
        product1.buy()
    elif k==2:
        product1.sell()
    elif k==3:
        product1.changing()
    elif k==4:
        product1.show()
    elif k==5:
        product1.now_time()
    elif k==6:
        product1.now_date()
    else:
        print("Inalid!!")
