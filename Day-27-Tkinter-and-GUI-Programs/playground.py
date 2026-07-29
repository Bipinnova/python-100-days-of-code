def add(*args):
    sum = 0
    for i in args:
        sum += i
    print(sum)
add(1, 2, 3, 4, 5)

def cal(n,**kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(kwargs)
    print(n)
    
    
cal(2, add=10,multiply=20)

class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        
        
my_car = Car()