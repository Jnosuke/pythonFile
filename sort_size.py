def size(item):
    sizelist = ["XS", "S", "M", "L"]
    pos = sizelist.index(item)
    return pos

data = ["S", "L", "XS", "S", "M", "S"]
data.sort(key = size)
print(data)
