class Flower:
    def __init__(self,name,price,stock):
        self.flower_name=name
        self.price_per_kg=price
        self.stock_available=stock
    def validate_flower(self):
        if(self.flower_name.lower() in ["orchid","rose","jasmine"]):
            return True
        else:
            return False
    def validate_stock(self,required_quantity):
        if(self.stock_available>=required_quantity):
            return True
        else:
            return False
    def sell_flower(self,required_quantity):
        if(self.validate_flower() and self.validate_stock(required_quantity)):
            self.stock_available-=required_quantity
        else:
            return False
    def check_level(self,required_quantity):
        if(self.stock_available>=required_quantity):
            return False
        else:
            return True
