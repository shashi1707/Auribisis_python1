class Product:
    def __init__(self,pid,name,price,brand):
        self.name=name
        self.pid=pid
        self.price=price
        self.brand=brand


    def ShowProductDetails(self):
        print("======{} | {} =======".format(self.name,self.pid))
        print("{} , {} ".format(self.price,self.brand))

class Shoe(Product):
    def __init__(self,pid,name,price,brand,shoesize):
        Product.__init__(self,pid,name,price,brand)
        self.shoesize=shoesize

    def ShowShoeDetail(self):
        Product.ShowProductDetails(self)
        print("{} ".format(self.shoesize))


class Mobile(Product):
    def __init__(self,pid,name,price,brand,os,ram):
        Product.__init__(self,pid,name,price,brand)
        self.os=os
        self.ram=ram

    def ShowMobileDetail(self):
        Product.ShowProductDetails(self)
        print("***{} | {} **".format(self.os,self.ram))

class LedTv(Product):
    def __init__(self,pid,name,price,brand,screensize,technology):
        Product.__init__(self,pid,name,price,brand)
        self.screensize=screensize
        self.technology=technology
    def ShowLedTvDetail(self):
        Product.ShowProductDetails(self)
        print("&&& {} | {} &&&".format(self.screensize,self.technology))

sRef = Shoe(101, "AlphaBounce", 8000, "Adidas", 8)
mRef = Mobile(201, "iPhoneX", 70000, "Apple", "iOS",4)
lRef = LedTv(301, "Samsung Curved", 50000, "Samsung", 50, "OLED")

sRef.ShowShoeDetail()
mRef.ShowMobileDetail()
lRef.ShowLedTvDetail()



