odd_gen = (odd for odd in range(1, 6, 2))
print(next(odd_gen))
print(next(odd_gen))
print(next(odd_gen))

def test():
    n = 0
    while True:
        received = yield n
        if received:
            n = received
        else:
            n = n + 1

gen = test()
print(next(gen))
print(next(gen))

gen.send(10)
print(next(gen))

import subgenerator
gen = subgenerator.main_gen(3)
print(list(gen))

from car_class1 import Car
car1 = Car()
car2 = Car("red")

print(car1.color)
print(car2.color)
car1.color = "green"
print(car1.color)

from car_class2 import Car
car1 = Car()
car1.drive(15)
car1.drive(20)

from car_class3 import Car
print(Car.marker)
print(Car.count)

from car_class4 import Car
car1 = Car()
car2 = Car("red")
car3 = Car("blue")
print(car1.mynumber, car2.mynumber, car3.mynumber)

class Simple:
    pass

#print(Simple.x)
Simple.x = 100
print(Simple.x *2)

def hello(msg = "hello"):
    print(msg)

Simple.greeting = hello
Simple.greeting("おはよう")

obj = Simple()
obj.a = 123
print(obj.a)

class A:
    def hello(self):
        print("ハロー")

class B(A):
    def bye(self):
        print("グッバイ")

obj = B()
obj.hello()
obj.bye()

from override import Greet2
obj = Greet2()
obj.hello("井上")
obj.hell()

from super1 import Player
Player1 = Player("青木", 16, 4, "GK")
print(Player1.name)

from person import Person
man = Person("宇佐美")
man.who()
#man.

from goods_property import Goods
shoes = Goods(name="dream", price=6800)
print(shoes.name)
print(shoes.price)
shoes.name = "Dream 8"
print(shoes.name)
