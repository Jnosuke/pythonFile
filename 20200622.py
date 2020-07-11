color_setA = {
    "blue",
    "yellow",
    "red"
}
color_setB = {"green", "blue", "black"}

print(color_setA)
print("gold" not in color_setA)

num2set = set(range(0, 20, 2))
num3set = set(range(0, 20, 3))

print(num2set)
print(num3set)

dataset = {101, 167, 103, 115, 189}
datalist = list(dataset)
print(datalist)
datalist.sort()
print(datalist)

fruits = set()
fruits.add("apple")
fruits.add("orange")
print(fruits)
fruits.remove("apple")
print(fruits)
fruits.discard("painappple")

str_set = set("My name is Kanathi")
print(str_set)
print(str_set.pop())

dataset = frozenset(["a", "b", "c"])
print(dataset)
print(type(dataset))
##dataset.add("f")


numbers = list(range(0, 10))
num_set = {num * 2 for num in numbers if num >= 5}
print(num_set)

a = {"リンゴ", "みかん", "桃", "イチゴ"}
b = {"イチゴ", "スイカ", "みかん", "バナナ"}
c = a|b
print(c)


set1 = {1, 2, 3}
list1 = [2, 4, 5, 6]
list2 = [3, 6, 9]
data = set1.union(list1, list2)
print(data)


d = a & b
print(d)

D = d
#D = a.intersection(b)
print(D)

print(d is D)

e = a - b
print(e)
print(a.difference(b))

g = a ^ b
print(g)
print(a.symmetric_difference(b))

data = {"red", "blue"}
data_ex = {"blue", "red"}
data2 = {"blue", "yellow"}
data3 = {"blue", "green"}
data4 = {"gold", "pinck"}
data_set = data.union(data2, data3, data4)
#data.update(data2, data3)
#data.intersection_update(data2)
print(data)

#data.difference_update(data2)
print(data)

print(data == data2)
print(data == data_ex)

print(data.isdisjoint(data2))
print(data.isdisjoint(data4))
print(data_set)
print(data_set.issubset(data))
print(data.issubset(data_set))
print(data_set.issuperset(data))

# under write dict,
stock = {"S" : 7, "X" : 8, "Z" : 12}
print(stock)
print(len(stock))


data = dict([("yellow", 3), ("blue", 5)])
print(data)
