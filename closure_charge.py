def charge(price):

    def calc(num):
        return price * num
    return calc

child = charge(400)
adult = charge(1200)

#print(child)
#print(adult)
price1 = child(3)
price2 = adult(5)

print(f"子供三人{price1}円、大人５人{price2}円")
