file = "../fox.txt"
with open(file, "r", encoding="utf-8") as fileobj:
    while True:
        text = fileobj.read(10)
        if text:
            print(text)
        else:
            break
