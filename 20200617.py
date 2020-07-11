name = ["鈴木", "田中", "栗林", "山岡", "上田"]
for i, who in enumerate(name, 1) :
    print(f"{i}：{who}さん")


name1 = ["鈴木", "田中", "高瀬", "皆木氏", "神田"]
longname = []

for n1, n2 in zip(name, name1) :
    longname.append(n1 + n2)

print(longname)

nums = list(range(1, 7))
nums_double = [num**2 for num in nums]
print(nums_double)

group_list = [str + "組" for str in "ABCDEFG"]
print(group_list)

numbers = [2.1, 0.2, 0.3, 1.4, 3.1, 0.3, 1.6]
result = [num for num in numbers if 1 <= num < 2]
print(result)

numbers = [2.1, 0.2, "", "1.4", 3.1, 0.3, 1.6]
print(numbers)
numbers = [num for num in numbers if isinstance(num, (int, float))]
print(numbers)

numbers = [4, 12, 3, 0, 15, 16, 17, 56, 98]
result = [num  for num in numbers if num >= 5 if num %2 == 0]
print(result)

#ネスティングを複数使用
data = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
result = [num*2 for alist in data for num in alist]
print(result)

print("4" in numbers)

print("longname", longname)
name = "神田"
result = False
for item in longname :
    if name in item :
        result = True
        break

print(result)

print(longname.index("田中田中"))

print(numbers.count(0))


import random
print(random.choice(numbers))

import secrets

print(secrets.choice(numbers))

print(sum(numbers))
print(min(numbers))
print(max(numbers))


taple = 1, 2, 3
print(taple)
at = (1, 2)
a = [1, 2]

bt = (4, 5)
b = [4, 5]
print(at + bt)
print(a + b)

data = tuple(range(-5, 10))
print(data[::2])
print(data[1])

(a, b) = ((100,200,300), (100,200,300))
print(a)
print(b)

b = a
c = (100, 200, 300)
b = (1,  2, 3)
print(a)
print(b)

x = [1, 2, 3]
y = [4, 5, 6]
z = [7, 8, 9]
zip_obj = zip(x,y,z)
print(zip_obj)
xyz = list(zip_obj)
print(xyz)
print("="*30)

X = list(xyz[0])
Y = list(xyz[1])
Z = list(xyz[2])

print(X)
print(Y)
print(Z)
