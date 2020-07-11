colors = ["blue", "red", "yellow", "red", "green"]
print("削除前", colors)
target = "red"

while target in colors:
    colors.remove(target)

print(colors)

del colors[0]

print(colors)


message = "happy bath, day !"

messageList = message.split(",")

print(messageList)


result = "12, 24, 56, 78, 98, 51"
result_list = result.split(", ", 3)
print(result_list)

top = result.split(",", 3)[:3]
print(top)


members = ["Tom", "ken", "Jon"]
name = " and ".join(members)
print(name)


abc = ["a", "b", "c"]
xyz = ["x", "y", "z"]
az = abc + xyz
print(az)


data = [1, 2, 3]
newdata = ["2", "4", "62"]
data.extend(newdata)
print(data)
data.append(newdata)
print(data)

colors = ["blue", "yellow", "red","green"]
color = colors[:2]

print(color)

data_list = list(range(0, 26))
print(data_list)
print(data_list[::-1][::3])
data_list_1 = data_list
print(data_list)
data_list[0] = 100
print(data_list)
print(data_list_1)


num_a = 10
num_b = num_a
print(num_b)
num_a = 12
print(num_a)
print(num_b)


list_mother = list(range(10, 51, 10))
print(list_mother)
list_work = list_mother.copy()
print(list_work)

print(list_mother is list_work)

list_work.sort(reverse = True)
print(list_work)

text_list = ["peach", "ver3", "Python", "Pokemon", "ver2"]
text_list.sort()
print(text_list)
list_work.reverse()
print(list_work)

import random
numbers = list(range(0, 10))
random.shuffle(numbers)
print(numbers)

new_words = sorted(text_list, key=str.lower)
print(new_words)
