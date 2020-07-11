key = ["yellow", "blue", "green"]
value = [3, 6, 5]
data = dict(zip(key, value))
print(data)

data1 = dict(yellow = 3, blue = 4, green = 5)
print(data1)

stock = dict.fromkeys(["S", "M", "L"], 0)
print(stock)

data = dict.fromkeys("abcd")
print(data)


data = {"yellow" : 3, "blue" : 4, "green" : 6}
data["blue"] = 10
data["white"] = 5
print(data)

print(data.setdefault("blue", 6))
data.setdefault("glold", 100)
print(data)


data = {"a" : 10, "b" : 20, "c" : 30}
newdata = {"a" : 15, "d" : 99}
data.update(newdata)
print(data)

del data["d"]
print(data)

from random import randint
keys = ["green", "red", "blue", "yellow"]
data = {key :randint(1, 100) for key in keys}
print(data)


unicode = {letter : ord(letter) for letter in "hello"}
print(unicode)

unicode_b = unicode.copy()
unicode_b["e"] = 0
print(unicode_b)
print(unicode)

import pprint
unicode_c = dict.fromkeys(unicode, 0)
pprint.pprint(unicode_c)


members = {"東京" : 21, "大阪" :  25, "福岡" : 58}
print(members.get("沖縄"))
for key in members:
    value = members[key]
    print(f"{key}の値は{value}")

print(members.keys())
keys = list(members.keys())
print(keys)

print(members.values())
print(sum(members.values()))

print(members.items())

for key, value in members.items():
    print(f"{key}の値が{value}")
members.pop("福岡")
print(members)

fruits = {"apple" : 7, "orange" : 5, "peach" : 6}
print(fruits.popitem())
print(fruits)
print(fruits.popitem())
print(fruits)

def hello():
    return "Hello!";

msg = hello()
print(msg)

def sum(value1, value2):
    value =  value1 + value2
    return value

sum_value = sum(1,3)
print(sum_value)

sum_value = sum(value1 = 1, value2 = 10)
print(sum_value)

def fruit(*args):
    print(args)

fruit("リンゴ", "バナナ")

def entry(name, gender, **kwargs):
    data = {"name" : name, "gender" : gender}
    data.update(kwargs)
    print(data)

entry(name= "木村", gender="men", old=12, like="バナナ")
